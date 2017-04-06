from flask import Flask
from flask import render_template
from test import print_zonas


app = Flask(__name__)
app.debug=True

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/opcion/<opc>")
def ida(opc):
    return print_zonas()

@app.route("/opcion/<opc>")
def idayvuleta(opc):
    return print_zonas()

@app.route("/opcion/<opc>")
def mensual(opc):
    return "este es el mensual." 


if __name__ == "__main__":
    app.run()
