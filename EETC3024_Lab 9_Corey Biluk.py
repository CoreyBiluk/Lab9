# EETG 3024 Advanced Embedded Systems
# Lab 9 - RPI Communication with Arduino
# Corey Biluk | W0425561
# March 1, 2021

from guizero import App, PushButton, Slider
from time import sleep
import serial

# Set up serial communication at 9600 baudrate and clear comms line. 
comms = serial.Serial('/dev/ttyUSB0', 9600)
comms.flush() 
sleep(3)
print("Serial Communication Started")

# Function to read slider 1 value and transmit that value to the Arduino
def servo1_control(sl1_value):
    #print(sl1_value)                                  # For testing purposes
    comms.flush()                                      # Flush serial comms line
    comms.write(str('servo1').encode('utf-8'))         # Send 'servo1' message to Arduino with utf-8 encoding
    comms.write(str("\n").encode('utf-8'))             # Send carriage return to signal end of communication
    comms.flush()                                      # Flush serial comms line
    comms.write(str(sl1_value).encode('utf-8'))        # Send slider 1 value to Arduino as a string
    comms.write(str("\n").encode('utf-8'))             # Send carriage return to signal end of communication
    sleep(0.25)                                        # Short delay to ensure all data sent properly

# Function to read slider 2 value and transmit that value to the Arduino
def servo2_control(sl2_value):
    #print(sl2_value)                                  # For testing purposes
    comms.flush()                                      # Flush serial comms line
    comms.write(str('servo2').encode('utf-8'))         # Send 'servo2' message to Arduino with utf-8 encoding
    comms.write(str("\n").encode('utf-8'))             # Send carriage return to signal end of communication
    comms.flush()                                      # Flush serial comms line
    comms.write(str(sl2_value).encode('utf-8'))        # Send slider 2 value to Arduino as a string
    comms.write(str("\n").encode('utf-8'))             # Send carriage return to signal end of communication
    sleep(0.25)                                        # Short delay to ensure all data sent properly

# Lists to save servo positions for recall
s1_pos = []
s2_pos = []

# Function to save servo postions into appended lists
def save_servo_positions(): 
    # When button is pressed, stores both servo positions by appending the lists
    s1_pos.append(slider1.value)
    s2_pos.append(slider2.value)

# Function to send saved positions to Arduino/servo
def recall_servo_positions():  
    # Loop to send position in lists to Arduino/servos
    for i in range(0, len(s1_pos)):

        comms.write(str('servo1').encode('utf-8'))     # Send 'servo1' message to Arduino with utf-8 encoding
        comms.write(str("\n").encode('utf-8'))         # Send carriage return to signal end of communication
        comms.flush()                                  # Flush serial comms line
        comms.write(str(s1_pos[i]).encode('utf-8'))    # Send servo 1 position to Arduino as a string
        comms.write(str("\n").encode('utf-8'))         # Send carriage return to signal end of communication
        comms.flush()                                  # Flush serial comms line

        comms.write(str('servo2').encode('utf-8'))     # Send 'servo2' message to Arduino with utf-8 encoding
        comms.write(str("\n").encode('utf-8'))         # Send carriage return to signal end of communication
        comms.flush()                                  # Flush serial comms line
        comms.write(str(s2_pos[i]).encode('utf-8'))    # Send servo 2 position to Arduino as a string
        comms.write(str("\n").encode('utf-8'))         # Send carriage return to signal end of communication
        comms.flush()                                  # Flush serial comms line

# Create App object
app = App(bg=(0,123,0), title = "Servo Control Faders")
# Create sliders and buttons
slider1 = Slider(app, start=0, end=180, width=400, command=servo1_control)
slider2 = Slider(app, start=0, end=180, width=400, command=servo2_control)
save_pos = PushButton(app, text="Save Positions", command=save_servo_positions)
recall_pos = PushButton(app, text="Recall Positions", command=recall_servo_positions)
# Display App
app.display()
# Close serial communications
comms.close()
