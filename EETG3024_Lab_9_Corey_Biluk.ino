// EETG 3024 Advanced Embedded Stystems 
// Lab 9 - RPI Communication with Arduino
// Corey Biluk | W0425561 
// March 1, 2021

#include <Servo.h>

// Create Servo objects
Servo myservo1;
Servo myservo2;

// Variables
int val1 = 0;             // Initial values for servo1
int val2 = 0;             // Initial values for servo2
String servo_num;         // Variable to determine if comms are for servo 1 or 2
String pos_data;          // Variable to hold position data transfered from Pi


void setup() {
  Serial.begin(9600);     // Initialize Serial monitor/communications
  myservo1.attach(10);    // Attach servos to their digital pins on the Arduino
  myservo2.attach(5);     // Attach servos to their digital pins on the Arduino
}

void loop() {
  if(Serial.available() >0)                     // Wait for serial comm to be given an input
  {
    servo_num = Serial.readStringUntil('\n');   // Read serial comms up to "\n" and store in variable
    
    if (servo_num == "servo1")                  // if comms are for servo 1 do:
    {
      pos_data = Serial.readStringUntil('\n');  // read position data and store in variable
      val1 = pos_data.toInt();                  // convert from string to int 
      myservo1.write(val1);                     // write int value to servo
    }
    
    if (servo_num == "servo2")                  // if comms are for servo 2 do:
    {
      pos_data = Serial.readStringUntil('\n');  // read position data and store in variable 
      val2 = pos_data.toInt();                  // convert from string to int
      myservo2.write(val2);                     // write int value to servo 2
    } 
    
    Serial.flush();                              // Clear serial communication line
    delay(500);
     
  }
}
