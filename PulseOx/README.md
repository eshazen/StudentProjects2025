# Pulse Ox BME Sr Design

This is the second pass at this.  The first team built a breadboard
version with Arduino Uno, 3 LEDs (Red, IR, Green) and an OPT101
optical detector module.

The goal of the second team is to add the green LED functionality to
compensate for melanin content in skin of various tones.

## Meeting 2025-02-27

Suggested next steps:

* Use an Arduino Uno and essentially the circuit from last year
* Build a soldered prototype on a shield like [this one](https://a.co/d/aV1Rrll).
* The shield would have the resistors for the LEDs and an 8 pin (2x4)
  header connector

Connections from Arduino shield to optical unit via 8 pin ribbon
cable:

1.  Red LED anode
2.  IR LED anode
3.  Green LED anode
4.  LED GND
5.  Photodiode VCC (5V)
6.  Photodiode GND
7.  Photodiode Output
8.  N/C

A shielded cable might be needed.  One option for this would be a Mini
DIN 8 pin such as [this one](https://a.co/d/c0LhOXC).



