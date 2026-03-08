from tempLib import measure_temperature

def display(date, time_of_day, server_room, temperature):
    print(f"Die Temperatur im Serverraum beträgt um {time_of_day} Uhr laut Sensor: {temperature}.")

def main():
    measure_temperature(display)

if __name__ == "__main__":
    main()




