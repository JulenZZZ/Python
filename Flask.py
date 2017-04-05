from flask import Flask,render_template

app = Flask(__name__)
app.debug=True

@app.route("/")
def hello():
    
    return render_template("index.html")

@app.route("/ida")
def ida():
    print("Esta es la funcion de ida.")

if __name__ == "__main__":
    app.run()
