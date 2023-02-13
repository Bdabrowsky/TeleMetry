# Telemetry data visualizer for rocketry

## Installing

In order to run program you need python 3 with installed matplotlib 
```shell
pip install matplotlib
```
and pyserial
```shell
pip install pyserial
```

## Usage

To use this software you need a serial device which receives telemetry via radio and sends it in comma separated form, then run:

```shell
python Telemetry.py
```
**Keep in mind that in order to use this software properly you will ned to specify serial port in code**

After few seconds, window with tleemetry will pop up

## Data format

After opening window, 4 subplots should appear:
* First one visualizes accelerations on all 3 axis 
* Second plots altitude
* Third shows rocket angles such as PITCH, YAW and ROLL
* Last one is velocity in all axis

## All above software is made using funding from [Odkrywcy Diamentów](https://odkrywcydiamentow.com.pl/) grant program
![alt text](https://odkrywcydiamentow.com.pl/wp-content/uploads/2017/09/cropped-Odkrywcy_logo-1.png)
