# CIS_Final_Project
My final project for CIS2020: Fundamentals of Unix.

- Python code written on a Raspberry Pi 3B working with a breadboard and circuits in order to manipulate a sensor.
- This is a step-by-step instruction manual to create a working distance sensor with an intrusion detection system.
- The sensor will display the distance to the nearest object in meters and then will set off the 'alarm' (LED) when the object is closer than a defined amount of meters.

# Let's Begin!

  To make this project you will need:
  - A raspberry pi (I used a Pi 3b)
    - HDMI cords and power cords depending on need
  - Eight male-to-female jumper wires
  - One button switch
  - One breadboard
  - One ultrasonic distance sensor
  - One LED of your choosing (I used red)
  - One 330 Ohms resistor
  - One 570 Ohms resistor
  - One 370 Ohms resistor

**Warning!!** 

In order to make sure you don't damage your raspberry pi, you will need to disconnect if from all power before attempting the ciruits. Do not bend pins and do NOT forget about the resistors. The purpose of the resistors is to stop the LED and ultrasonic distance sensor from consuming too much power and overheating. Make sure your circuits are properly grounded as well.

![image](https://github.com/user-attachments/assets/d3f49746-357b-4710-9319-f7c58a4678df)

## Due to the fact that TinkerCad does not have a raspberry pi component, I have used a breadboard in its place. The breadboard on the left is the raspberry pi in this scenario.

# Steps

**1: Connect ultrasonic distance sensor**

![image](https://github.com/user-attachments/assets/87395e36-3438-4514-a80e-0f3998c8b786)

Connect the distance sensor just like this on the breadboard. The ground pin on the distance sensor is associated with the red jumper wire. That wire connects to the 6th pin on the pi, which is ground. 
The two resistors are combined to prevent the distance sensor from drawing too much power. I used the 330 Ohms resistor through the H2 and H6 pins on the breadboard. I have the 570 Ohmd resistor through H1 and H6. 
The trigger is connected via the green jumper wire in F3. The wire is then connected to the pi in pin 18, which is GPIO 24. 
The blue jumper wire is in F6 connects to pin 26 on the pi. This means Echo is GPIO 23. 
The white jumper wire needs to be connected from its spot on the breadboard (F4) to the 2nd pin on the pi, which is 5V. This gives the distance sensor power. 

**2: Connect LED**

![image](https://github.com/user-attachments/assets/040b6897-1aca-4a08-b620-fe5f465a1c14)

Imitate this set up on your breadboard. The LED is positioned with the Anode in D17, the cathode in D16. 
The red jumper wire is in C16 of the breadboard. It connects to the pi in pin 6, ground. 
The resistor is 370 Ohms. This stops the LED from drawing too much power. It is placed in C17 through C21.
The yellow wire is in B21, next to the end of the resistor. This connects to pin 7 on the pi, that is gpio 4.

**3: Connect Button**

![image](https://github.com/user-attachments/assets/32969208-21ff-4a5a-a756-e47864def5f3)

This is how the button should be set up. Make sure that your button is facing the exact direction displayed. If it is rotated then the button will not work. There should only be one hole between the legs towards the left like shown in the picture.










