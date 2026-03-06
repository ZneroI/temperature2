import json

CONFIG_FILE = "tempConfig.json"
PATH_KEY = "path"

def read_file():
    path = read_config()
    file = open(path, "r")
    content = file.read()
    file.close()
    return content

def read_config():    
    try:
        file = open(CONFIG_FILE, "r")
        content = file.read()
        settings = json.loads(content)
        file.close()
        
        if not PATH_KEY in settings:
            raise AttributeError(CONFIG_FILE + " with " + PATH_KEY + " property is required.")

        return settings[PATH_KEY]
        
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")

    
    
