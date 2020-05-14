import json


class InstallationHandler:
    def process(self, data):
        payload = json.loads(data)
        action = payload['action']
        print(f"Processing installation: {action}")
