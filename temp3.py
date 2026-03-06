import datetime
import time
import temp2
import temp


from temp import read_file
from temp2 import parse_w1_temp

TIMER = 10
SERVERRAUM = "S1"

raw_output = temp.read_file()
temp2.parse_w1_temp(raw_output)

while True:
    try:
        raw_output = temp.read_file()
        c, f = temp2.parse_w1_temp(raw_output)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dictionary = {
            "timestamp": timestamp,
            "serverraum": SERVERRAUM,
            "temperature_c": c
        }
        with open("archive.txt", "a") as archive_file:
            archive_file.write(str(dictionary) + "\n")
            archive_file.close()
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(TIMER)

