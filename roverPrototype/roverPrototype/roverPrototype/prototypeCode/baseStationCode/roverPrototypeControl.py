#!/usr/bin/env python

import socket
import pygame

# UDP CONSTANTS
TARGET_IP = "192.168.1.51"
UDP_PORT = 8888
MAX_BUFFER_SIZE = 24

# UDP Defaults message
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = ""


def joy2value(value, half_control=False):
    if half_control:
        value /= 2.0
    if abs(value ) < 0.05:
        value = 0
    return value


def float256(value, low, high):
    value = 256 * (value - low) / (high - low)
    value = max([value, 0])
    value = min([value, 255])
    return int(value)


# Main
if __name__ == '__main__':
    try:
        # Joystick
        pygame.joystick.init()
        pygame.display.init()
        joystick = []
        joynum = 1
        print(str(joynum) + " joysticks connected.")
        pygame.joystick.Joystick(0).init()
        while len(joystick) < joynum:
            pygame.event.pump()
            if pygame.joystick.Joystick(0).get_button(0):
                    joystick.append(pygame.joystick.Joystick(0))
                    pygame.time.wait(500)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', UDP_PORT))
        sock.settimeout(0.01)
        # Main Loop
        while True:
            # Get and convert joystick value, print
            pygame.event.pump()
            angle = joy2value(joystick[0].get_axis(0), True)
            speed = joy2value(joystick[0].get_axis(1), (not joystick[0].get_button(0)))
            angle = float256(angle, -1, 1)
            speed = float256(speed, -1, 1)
            print("ANGLE: " + str(ord(chr(angle))))
            print("SPEED: " + str(ord(chr(speed))))
            message = ''.join([chr(angle), chr(speed)])
            # Send data over UDP, print recv
            sock.sendto(message, (TARGET_IP, UDP_PORT))
            pygame.time.wait(100)

    except KeyboardInterrupt:
        pygame.quit()

