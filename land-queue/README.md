# monorepo

# Github Integration

In order to get/update Github repository data we need a Github Application.

## Create and setup Github Application

- Go to GH Settings -> [Developer settings](https://github.com/settings/apps) -> New Github App.
- Setup Application.

```
Name: MonorepoApp
Homepage URL: https://localhost:5000
Webhook URL: https://20fbc45a.ngrok.io/webhooks
Permissions:
X PullRequests
Subscribe For:
X PullRequests
```

- Generate private key for App. (TODO: Store it, config)
- Save APP_ID in app config (TODO: for now in app.py)

## Install app

App can be to one repo or all repositories where user is admin.

- Go to [MonorepoApp](https://github.com/settings/apps) -> Install App.
- Pick account with admin privileges for target repostory.
- Pick repository and Allow access.

# Development

## Requirements

- [Oya](https://oya.sh/)
- Python 3.7.5 + pyenv
- Flask
- PyGithub

## Setup

        $ oya run install  # install dependecies
        $ oya run start    # start project
