def parse_w1_temp(text):
    lines = text.strip().splitlines()

    # verify CRC
    if not lines[0].strip().endswith("YES"):
        raise ValueError("CRC check failed")

    # extract temperature
    temp_str = lines[1].split("t=")[1]
    temp_c = int(temp_str) / 1000
    temp_f = temp_c * 9 / 5 + 32

    return temp_c, temp_f


data = open("systembus.txt").read()

c, f = parse_w1_temp(data)

print(f"Die Temperatur beträgt {c:.2f} °C/ " f"{f:.2f} °F")
