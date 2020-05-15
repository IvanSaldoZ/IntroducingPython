from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./templates")


@app.route('/')
def home():
    params = {
            'thing': request.args.get('thing'),
            'height': request.args.get('height'),
            'color': request.args.get('color')
              }
    return render_template("home.html", **params)


app.run(port=5000, debug=True)
