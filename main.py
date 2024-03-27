from flask import Flask, render_template, request
import pandas
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv("games.csv")
x = data.drop(columns=["games"])
y = data["games"]
model = DecisionTreeClassifier()
model.fit(x.values ,y)


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    # Initialize default values
    action = 0
    strategy = 0
    fantasy = 0
    adventure = 0

    if request.method == "POST":
        # Get form input values
        Aaction = request.form.get("action")
        Sstrategy = request.form.get("strategy")
        Ffantasy = request.form.get("fantasy")
        Aadventure = request.form.get("adventure")

        # Convert empty strings to default values or handle appropriately
        if Aaction:
            action = float(Aaction)
        if Sstrategy:
            strategy = float(Sstrategy)
        if Ffantasy:
            fantasy = float(Ffantasy)
        if Aadventure:
            adventure = float(Aadventure)

        # Make prediction using machine learning model
        predicted_value = model.predict([[action, strategy, fantasy, adventure]])

        return render_template("index.html", firstname=predicted_value[0])

    return render_template("index.html", firstname="")


if __name__ == "__main__":
    app.run(debug=True)
