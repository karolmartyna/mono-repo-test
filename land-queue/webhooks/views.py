import json
from flask import request, Blueprint


from config import APP_ID, WEBHOOKS_LOG_FILE
from utils import log
from webhooks.authentication import get_gh_app

webhook_views = Blueprint("webhook_views", __name__)


def set_state(state, repo, pr_no, installation_id):
    gh = get_gh_app(installation_id)
    repo = gh.get_repo(repo)
    pull = repo.get_pull(pr_no)
    pull.set_labels(state)


@webhook_views.route("/webhooks", methods=["POST"])
def webhooks():
    log(WEBHOOKS_LOG_FILE, request.data)

    data = json.loads(request.data)
    repo = data["repository"]["full_name"]
    print("Webhooks PR action: ", data["action"], "; repo:", repo)

    if "pull_request" in data:
        sha = data["pull_request"]["head"]["sha"]
        pr_no = data["pull_request"]["number"]
        installation_id = data["installation"]["id"]

        set_state("Build added to queue", repo, pr_no, installation_id)

    return "OK"


@webhook_views.route("/", methods=["GET", "POST"])
def home():
    return "OK"
