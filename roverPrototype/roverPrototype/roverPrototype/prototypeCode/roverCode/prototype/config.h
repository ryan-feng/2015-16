// MOTOR CONTROL CONSTANTS //
#define FRONT_RIGHT_MOTOR_PIN
#define FRONT_LEFT_MOTOR_PIN
#define BACK_RIGHT_MOTOR_PIN
#define BACK_LEFT_MOTOR_PIN
#define TALON_NEUTRAL_FREQUENCY 1500
#define FRONT_RIGHT_PIN   5
#define FRONT_LEFT_PIN    3
#define BACK_RIGHT_PIN    9
#define BACK_LEFT_PIN     6

// ETHERNET COMMUNICATION CONSTANTS //
#define UDP_PORT         8888
#define DESTINATION_PORT 8888
#define TIMEOUT          1000

// SERIAL COMMUNICATION CONSTANTS //
#define BAUD_RATE 9600

// STEERING EQUATION CONSTANTS //
#define FEEDBACK_POTENTIOMETER_PIN A0
#define VERTICAL_WHEEL_SEPARATION  27.6 // in
#define LATERAL_WHEEL_SEPARATION   22.4 // in
#define MAX_TURN_ANGLE 45 // degrees
#define TUNING_CONSTANT 1 // constant for error correction
