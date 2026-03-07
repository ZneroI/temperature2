def read_file(path):
    file = open(path, "r")
    content = file.read()
    file.close()
    return content

    