from flask import Flask, request, jsonify
from database import db
from models.diet import Meal

app = Flask(__name__)
app.config["SECRET_KEY"] = "daily_diet"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app=app)

@app.route("/refeicao", methods=["POST"])
def create_meal():
    response_json = request.json
    meal_name = response_json.get("name")
    meal_description = response_json.get("description")
    meal_is_in_diet = response_json.get("is_diet")

    if meal_name:
        if not meal_is_in_diet:
            meal_is_in_diet = 0
        meal = Meal(name = meal_name, description = meal_description, is_diet = meal_is_in_diet)

        db.session.add(meal)
        db.session.commit()

        return jsonify({"message": "SUCESSO EM CRIAR UMA REFEIÇÃO - TEST"}), 200

    return jsonify({"message": "DADOS INVÁLIDOS - TEST"}), 400

@app.route("/refeicao/<int:id>", methods=["PUT"])
def update_meal(id):
    meal = Meal.query.get(id)
    response_json = request.json
    meal_name = response_json.get("name")
    meal_description = response_json.get("description")
    meal_is_in_diet = response_json.get("is_diet")

    if isinstance(None, type(meal)):
        return jsonify({"message": "NÃO FOI POSSÍVEL EDITAR ESTA REFEIÇÃO - TEST"}), 404

    if meal_name:
        if not meal_is_in_diet:
            meal_is_in_diet = 0
        meal.name = meal_name
        meal.description = meal_description
        meal.is_diet = meal_is_in_diet
        db.session.commit()

        return jsonify({"message": f"REFEIÇÃO {id} ALTERADA COM SUCESSO - TEST"}), 200

if __name__ == "__main__":
    app.run(debug=True)
