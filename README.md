# Door-Security-Alarm-controlled-by-Google-Assistant-IoT-
IoT based Door Security Alarm controlled by Google Assistant

# Why ?
In the world that is advancing rapidly with technology where cars could drive on their own and drones could capture your food, burglary should not be of much concern but the above statistics just proves it wrong. In this project we will build our own security system which can detect if a door/window is opened. The alarm can be activated or de-activated through voice commands via Google assistant and when an intrusion is detected it will also send a mail to you and your relatives warning them about it. Cool thing is that entire thing runs on cloud so it can be controlled from anywhere in the world.

# How-To
The Bolt development board is based out of the famous ESP8266 Wi-Fi module from Espressif semi-conductor. But here it has its own Bolt firmware running inside it, this helps us to access the GPIO pins (Digital Read/Write, Analog Read, PWM Write) etc through an API provided by bolt. Because of this fact the Bolt can be programmed with JavaScript, HTML or even Python. As Python is easy to work on i stick to python.

# Components required
-- Bolt Development Board
-- Breadboard
-- Hall effect sensor (A3144)
-- LED
-- Capacitor (50V, 10uF)
-- Resistor 10K
-- Magnet
-- Connecting wires
