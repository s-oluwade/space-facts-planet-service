from flask import Flask, jsonify
import random

app = Flask(__name__)

facts = [
    "Mars has the tallest volcano in the solar system, Olympus Mons.",
    "Venus is the hottest planet in our solar system.",
    "Jupiter has the shortest day of all the planets."
]

@app.route('/planet-fact', methods=['GET'])
def get_planet_fact():
    fact = random.choice(facts)
    return jsonify({"fact": fact})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
