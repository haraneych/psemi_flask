from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    list = range(0,10)
    dict = {
        "好きな色":"青",
        "好きなゲーム":"スプラトゥーン3",
        "好きな県":"宮城県"
        }
    flag = True
    return render_template('index.html',list = list, dict = dict, flag = flag) 


if __name__ == "__main__":
    app.run(port = 8080) 