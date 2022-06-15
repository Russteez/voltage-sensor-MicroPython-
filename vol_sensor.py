import urequests
import wifi
from machine import Pin, ADC
from time import sleep_ms

pin = Pin(35, Pin.IN)
vol_pin = ADC(pin)
vol_pin.atten(ADC.ATTN_11DB)

def vol_response():
    while True:
        try:
            vol = vol_pin.read() * 3.3 / 4095
            real_vol = vol * 5.264
            print(real_vol)
            response = urequests.post("http://192.168.1.1:1880/Voltage", data = str(real_vol))
            sleep_ms(1000)
        except OSError as error:
            wifi.connect()
            print(error)
        
if __name__ == "__main__":
    wifi.connect()
    vol_response()