import datetime
import time

from temp import read_file
from temp2 import parse_w1_temp
from config_reader import read_config

PATH_KEY = "path"
TEMPERATUR_UNIT_KEY = "unit"
PRECISION_KEY = "precision"
INTERVAL_KEY = "interval_seconds"
CELSIUS = "celsius"
KELVIN = "kelvin"
FAHRENHEIT = "fahrenheit"


def record_temperature():
    TIMER = 10
    SERVERRAUM = "S1"
    settings = read_config()

    while True:
        try:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            time_of_day = datetime.datetime.now().strftime("%H:%M:%S")
            raw_output = read_file(settings[PATH_KEY])
            temperature = get_temperature(raw_output, settings[TEMPERATUR_UNIT_KEY], settings[PRECISION_KEY])

            log = {
                "Datum": date,
                "Uhrzeit": time_of_day,
                "Serverraum": SERVERRAUM,
                "Temperatur": temperature
            }

            with open("archive.txt", "a", encoding="utf-8") as archive_file:
                archive_file.write(str(log) + "\n")

            time.sleep(settings[INTERVAL_KEY])

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
        value = temperature_kelvin
        suffix = "K"
    elif unit.lower() == FAHRENHEIT:
        value = temperature_fahrenheit
        suffix = "°F"
    else:
        raise ValueError(f"Invalid temperature unit: {unit}.")

    value =  round(value, precision)
    return f"{str(value)} {suffix}"


if __name__ == "__main__":
    record_temperature()

