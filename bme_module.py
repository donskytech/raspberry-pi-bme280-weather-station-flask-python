import smbus2
import bme280
import time
import math

class BME280Module:
    SEA_LEVEL_PRESSURE_HPA = 1013.25
    PORT = 1
    ADDRESS = 0x76
    
    def __init__(self):
        self.bus = smbus2.SMBus(BME280Module.PORT)
        self.calibration_params = bme280.load_calibration_params(self.bus, BME280Module.ADDRESS)
        
        
    def get_sensor_readings(self):
        sample_reading = bme280.sample(self.bus, BME280Module.ADDRESS, self.calibration_params)
        temperature_val = sample_reading.temperature
        humidity_val = sample_reading.humidity
        pressure_val = sample_reading.pressure

        # Altitude calculation
        altitude_val = 44330 * (1.0 - math.pow(pressure_val / BME280Module.SEA_LEVEL_PRESSURE_HPA, 0.1903))
        
        return (temperature_val, pressure_val, humidity_val, altitude_val)
    
