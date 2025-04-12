from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import ds1302
import time
import datetime

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)
ds = ds1302.DS1302(Pin(0),Pin(1),Pin(2))
# Set the date and time on the RTC
# ds.year(2025)  # Set the year to 2085
# ds.month(4)    # Set the month to January
# ds.day(12)     # Set the day to 17th
# ds.hour(00)    # Set the hour to midnight (00)
# ds.minute(00)  # Set the minute to 17
# ds.second(00)  # Set the second to 30

display = SSD1306_I2C(128, 64, i2c)

#display.invert(1)
display.contrast(100)
 
def read_temp():
     sensor_temp = machine.ADC(4)
     conversion_factor = 3.3 / (65535)
     reading = sensor_temp.read_u16() * conversion_factor 
     temperature = 27 - (reading - 0.706)/0.001721
     formatted_temperature = "{:.1f}".format(temperature)
     string_temperature = str("Temp:" + formatted_temperature)
     print(string_temperature)
     time.sleep(2)
     return string_temperature
    
def convert_time(time_string):
    hours, minutes = map(int, time_string.split(":"))
    meridian = "AM"
    if hours > 12:
        hours -= 12
        meridian = "PM"
    elif hours == 12:
        meridian = "PM"
    elif hours == 0:
        hours = 12
    return f"{hours:02}:{minutes:02} {meridian}"

while True:
      temperature = read_temp()
      display.text(temperature,0,14)
      t = str(ds.hour()) + ":" + str(ds.minute())
      display.text("Time="+convert_time(t),0,28)
      display.text("Date={}/{}/{}" .format(ds.month(), ds.day(),ds.year()),0,40)
      display.show()
      display.fill(0)
    
    
    

    

  
    

