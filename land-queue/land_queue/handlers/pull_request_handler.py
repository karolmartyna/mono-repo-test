import json
import requests
from github import Github
from datetime import datetime, timedelta, timezone
from jwt import (JWT, jwk_from_pem)
from jwt.utils import get_int_from_datetime


def jwt_token(config):
    message = {
        'iss': config.GH_APP_ID,
        'iat': get_int_from_datetime(datetime.now(timezone.utc)),
        'exp': get_int_from_datetime(
            datetime.now(timezone.utc) + timedelta(minutes=10)),
    }
    signing_key = jwk_from_pem(config.GH_APP_KEY.encode())

    return JWT().encode(message, signing_key, alg='RS256')


def fetch_cred(installation_id, jwt):
    headers = {
        'Authorization': 'Bearer ' + jwt,
        'Accept': 'application/vnd.github.machine-man-preview+json'
    }
    url = 'https://api.github.com/app/installations/%s/access_tokens' % installation_id
    response = requests.post(url, headers=headers)
    return json.loads(response.content)


class PullRequestHandler:
    def __init__(self, config):
        self.config = config

    def process(self, data):
        payload = json.loads(data)
        action = payload['action']
        print(f"Processing pull_request: {action}")
        if action == 'opened' or action == 'reopened':
            self.update(payload)

    def update(self, payload):
        action = payload['action']
        repo = payload["repository"]["full_name"]
        pr_no = payload["pull_request"]["number"]
        installation_id = payload["installation"]["id"]
        label = f"{self.config.GH_APP_SLUG} processing pr {action}"
        self.set_label(label, repo, pr_no, installation_id)

    def set_label(self, label, repo, pr_no, installation_id):
        gh = self.get_gh_app(installation_id)
        repo = gh.get_repo(repo)
        pull = repo.get_pull(pr_no)
        pull.set_labels(label)

    def get_gh_app(self, installation_id):
        jwt = jwt_token(self.config)
        cred = fetch_cred(installation_id, jwt)
        return Github(cred['token'])
