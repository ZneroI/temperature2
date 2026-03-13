def read_temp_sensor(path):
    file = open(path, "r")
    content = file.read()
    file.close()
    return content

    