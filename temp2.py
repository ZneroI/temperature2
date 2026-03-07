import time
import datetime
from temp import read_file
from config_reader import read_config

PATH_KEY = "path"
TEMPERATUR_UNIT_KEY = "unit"
PRECISION_KEY = "precision"
INTERVAL_KEY = "interval_seconds"

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

if __name__ == "__main__":
    settings = read_config()

    while True:
        try:
            raw = read_file(settings["path"])
            temp_c, temp_k, temp_f = parse_w1_temp(raw)
            time_of_day = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Die Temperatur im Serverraum beträgt um {time_of_day} Uhr laut Sensor: {temp_c} °C.")
            time.sleep(settings[INTERVAL_KEY])

        except KeyboardInterrupt:
            print("Temperaturmessung wird beendet.")
            print("Programm wird beendet")
            break

        except Exception as e:
            print(f"Error: {e}")
            break




