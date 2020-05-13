# Land Queue

# Environment

        $ export GH_APP_SLUG="land-queue-test-app"
        $ export GH_APP_ID="64638"
        $ export GH_APP_KEY="<key here>"

# Github Integration

In order to get/update Github repository data we need a Github Application.

## Create and setup Github Application

- Go to GH Settings -> [Developer settings](https://github.com/settings/apps) -> New Github App.
- Setup Application.

```
Name: Land Queue App
Homepage URL: https://localhost:5000
Webhook URL: https://20fbc45a.ngrok.io/webhooks
Permissions:
X PullRequests
Subscribe For:
X PullRequests
```

- Generate private key for App. (TODO: Store it, config)
- Save APP_SLUG (you can find it in APP url ex. land-queue-app) in app config (TODO: for now in app.py)

## Install app

App can be to one repo or all repositories where user is admin.

- Go to [Land Queue App](https://github.com/settings/apps) -> Install App.
- Pick account with admin privileges for target repostory.
- Pick repository and Allow access.

# Development

## Requirements

- [Oya](https://oya.sh/)
- Python 3.7.5 + pyenv
- [Poetry](https://python-poetry.org/docs/#osx-linux-bashonwindows-install-instructions)
- Flask
- PyGithub

## Poetry how-to
Poetry is neat dependency manager for python.
1. Install poetry (preferably globally): `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`
2. Install all dependencies: `poetry install`
3. Install production dependencies: `poetry install --no-dev`

4. Add dependency: `poetry add requests`
5. Add dev dependency `poetry add --dev black`
6. Remove dependency `poetry remove requests`

## Setup

        $ oya run install  # install dependecies
        $ oya run start    # start project
