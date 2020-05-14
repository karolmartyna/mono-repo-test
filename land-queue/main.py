from flask import Flask

from land_queue.views import views as bp_views

app = Flask(__name__)
app.register_blueprint(bp_views)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
