import json

from github import Github
from jwt import JWT, jwk_from_pem
from jwt.utils import get_int_from_datetime
import requests

from config import APP_ID, KEY_FILE
from datetime import datetime, timedelta, timezone


def generate_jwt_token() -> str:
    message = {
        "iss": APP_ID,
        "iat": get_int_from_datetime(datetime.now(timezone.utc)),
        "exp": get_int_from_datetime(
            datetime.now(timezone.utc) + timedelta(minutes=10)
        ),
    }
    with open(KEY_FILE, "rb") as fh:
        signing_key = jwk_from_pem(fh.read())

    return JWT().encode(message, signing_key, alg="RS256")


def fetch_cred(installation_id: str, jwt: str):
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Accept": "application/vnd.github.machine-man-preview+json",
    }
    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
    response = requests.post(url, headers=headers)
    return json.loads(response.content)


def get_gh_app(installation_id):
    jwt = generate_jwt_token()
    cred = fetch_cred(installation_id, jwt)
    return Github(cred["token"])
