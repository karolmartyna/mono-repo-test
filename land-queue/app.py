from flask import Flask
from webhooks.views import webhook_views

app = Flask(__name__)
app.register_blueprint(webhook_views)


if __name__ == "__main__":
    app.run()
