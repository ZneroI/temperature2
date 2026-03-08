import json
import time
import datetime

from temp import read_file

CONFIG_FILE = "tempConfig.json"
PATH_KEY = "path"
TEMPERATUR_UNIT_KEY = "unit"
PRECISION_KEY = "precision"
INTERVAL_KEY = "interval_seconds"
CELSIUS = "celsius"
KELVIN = "kelvin"
FAHRENHEIT = "fahrenheit"
SERVERRAUM = "S1"


def parse_w1_temp(text):
    lines = text.strip().splitlines()

    # verify CRC
    if not lines[0].strip().endswith("YES"):
        raise ValueError("CRC check failed")

    # extract temperature
    temp_str = lines[1].split("t=")[1]
    temp_c = int(temp_str) / 1000
    temp_f = temp_c * 9 / 5 + 32

    return temp_c, temp_c + 273.15, temp_f


def measure_temperature(callback):
    settings = read_config()

    while True:
        try:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            time_of_day = datetime.datetime.now().strftime("%H:%M:%S")
            raw_output = read_file(settings.path)
            temperature = get_temperature(raw_output, settings.unit, settings.precision)
            
            callback(date, time_of_day, SERVERRAUM, temperature)

            time.sleep(settings.interval)

        except KeyboardInterrupt:
            print("Temperaturmessung wird beendet.")
            print("Programm wird beendet")
            break

        except Exception as e:
            print(f"Error: {e}")
            break

def get_temperature(raw_output, unit, precision):
    temperature_celsius, temperature_kelvin, temperature_fahrenheit = parse_w1_temp(raw_output)
    
    value = None
    suffix = None

    if unit.lower() == CELSIUS:
        value = temperature_celsius
        suffix = "°C"
    elif unit.lower() == KELVIN:
        value = temperature_kelvinf
        suffix = "K"
    elif unit.lower() == FAHRENHEIT:
        value = temperature_fahrenheit
        suffix = "°F"
    else:
        raise ValueError(f"Invalid temperature unit: {unit}.")

    value =  round(value, precision)
    return f"{str(value)} {suffix}"

class Settings:
    def __init__(self, settings_dict):
        self.path = settings_dict[PATH_KEY]
        self.unit = settings_dict[TEMPERATUR_UNIT_KEY]
        self.precision = settings_dict[PRECISION_KEY]
        self.interval = settings_dict[INTERVAL_KEY]

def read_config():    
    try:
        file = open(CONFIG_FILE, "r")
        content = file.read()
        settings = json.loads(content)
        file.close()
        
        if not PATH_KEY in settings:
            raise ValueError(CONFIG_FILE + " with " + PATH_KEY + " property is required.")
        if not TEMPERATUR_UNIT_KEY in settings:
            raise ValueError(CONFIG_FILE + " with " + TEMPERATUR_UNIT_KEY + " property is required.")
        if not PRECISION_KEY in settings:
            raise ValueError(CONFIG_FILE + " with " + PRECISION_KEY + " property is required.")
        if not INTERVAL_KEY in settings:
            raise ValueError(CONFIG_FILE + " with " + INTERVAL_KEY + " property is required.")

        return Settings(settings)
        
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return None