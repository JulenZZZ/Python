from flask import Flask,render_template

app = Flask(__name__)
app.debug=True

@app.route("/")
def hello():
    name="Julen"
    name2="Zulaika"
    return render_template("index.html", name=name,name2=name2)

if __name__ == "__main__":
    app.run()