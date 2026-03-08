from tempLib import measure_temperature

def archive(date, time_of_day, server_room, temperature):

        log = {
        "Datum": date,
        "Uhrzeit": time_of_day,
        "Serverraum": server_room,
        "Temperatur": temperature
        }

        with open("archive.txt", "a", encoding="utf-8") as archive_file:
            archive_file.write(str(log) + "\n")


def main():
    measure_temperature(archive)


if __name__ == "__main__":
    main()

