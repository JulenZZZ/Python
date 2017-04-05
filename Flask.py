from flask import Flask
from flask import render_template
import test as t

app = Flask(__name__)
app.debug=True

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/opcion/<opc>")
def ida(opc):
    return t.print_zonas()





if __name__ == "__main__":
    app.run()
