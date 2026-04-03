from flask import Flask
from app.routes.task_routes import task_blueprint

app = Flask(__name__)

app.register_blueprint(task_blueprint)

@app.route("/")
def home():

    return {
        "message": "Jenkins CI/CD Demo"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)