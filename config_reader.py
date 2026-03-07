import json

CONFIG_FILE = "tempConfig.json"
PATH_KEY = "path"
TEMPERATUR_UNIT_KEY = "unit"
PRECISION_KEY = "precision"
INTERVAL_KEY = "interval_seconds"

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

        return settings
        
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")