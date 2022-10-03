def compile_config(config_path):
    import re
    import json


    class config_entry:
        def __init__(self, name, timezone, path, order, regex_dict):
            self.name = name
            self.timezone = timezone
            self.path = path,
            self.order = order
            self.regex_dict = regex_dict

    
    try:
        f = open(config_path)
    except:
        print("Cannot open config path")
        exit()
    try:
        data = json.load(f)
        regex_dict = data
        config_to_return = config_entry(data['title'], data['meta']['timezone'], data['meta']['directory'], data['parser_meta']['order'])
    except:
        print("Error parsing JSON config")