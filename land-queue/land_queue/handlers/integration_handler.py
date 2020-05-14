import json


class IntegrationHandler:
    def process(self, data):
        payload = json.loads(data)
        action = payload['action']
        print(f"Processing integration: {action}")
