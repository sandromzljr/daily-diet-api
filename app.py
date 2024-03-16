from flask import Flask, request, jsonify
from database import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "daily_diet"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app=app)

if __name__ == "__main__":
    app.run(debug=True)
