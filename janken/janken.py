from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("janken.html")

@app.route("/rock")
def rock():
    return render_template("rock.html",number = random.randint(1,3))

@app.route("/paper")
def paper():
    return render_template("paper.html",number = random.randint(1,3))

@app.route("/scissors")
def scissors():
    return render_template("scissors.html",number = random.randint(1,3))

if __name__=="__main__":
    app.run(host='0.0.0.0')


