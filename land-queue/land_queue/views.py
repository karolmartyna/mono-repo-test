import json
from flask import request, Blueprint
from land_queue.handlers.pull_request_handler import PullRequestHandler
from land_queue.handlers.installation_handler import InstallationHandler
from land_queue.handlers.integration_handler import IntegrationHandler
from land_queue.config import Config


views = Blueprint("webhook_views", __name__)


WEBHOOK_EVENT_HANDLERS = {
    "installation": InstallationHandler(),
    "integration_installation": InstallationHandler(),
    "pull_request": PullRequestHandler(Config),
}


@views.route("/webhooks", methods=["POST"])
def webhooks():
    github_event = request.headers.get("X-GitHub-Event")

    if github_event in WEBHOOK_EVENT_HANDLERS:
        handler = WEBHOOK_EVENT_HANDLERS[github_event]
        handler.process(request.data)
    else:
        print(f"Ups. Unhandleable Github event: {github_event}!")

    return "OK"


@views.route("/")
def index():
    return f'<tt><big><a href="/install">Install {Config.GH_APP_SLUG} to your repo.</a></big></tt>'


@views.route("/install")
def install():
    install_url = f"https://github.com/apps/{Config.GH_APP_SLUG}/installations/new"
    return redirect(install_url)


# https://cloud.google.com/appengine/docs/standard/python3/configuring-warmup-requests
@views.route("/_ah/warmup")
def warmup():
    return "", 200, {}
