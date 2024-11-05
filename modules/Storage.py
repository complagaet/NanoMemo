import json
import os
from json import JSONDecodeError


class Storage:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Storage, cls).__new__(cls)
        return cls._instance

    def __init__(self, path, data_template, file_name="storage.json"):
        if hasattr(self, 'initialized') and self.initialized:
            return

        self.data = None
        self.file = None
        self.path = path
        self.data_template = data_template
        self.file_name = file_name
        self.full_path = os.path.join(path, file_name)
        self.initialized = True

        if not os.path.exists(self.path):
            os.makedirs(self.path)

        try:
            self.read()
        except JSONDecodeError:
            print("[Storage] Error parsing file")
            self.dump("dump")
            self.data = data_template
            self.write()
        except FileNotFoundError:
            self.data = data_template
            self.write()

    def read(self):
        self.file = open(self.full_path, 'r+')
        self.data = json.loads(self.file.read())
        self.file.close()

    def write(self):
        self.file = open(self.full_path, 'w+')
        self.file.write(json.dumps(self.data))
        self.file.close()

    def dump(self, dump_name):
        original = self.file = open(self.full_path, 'r+')
        dump = open(f"{self.path}{dump_name}_{self.file_name}", 'w')
        dump.write(original.read())
        original.close()
        dump.close()

    def reset(self):
        self.data = self.data_template
        self.write()