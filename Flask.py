from flask import Flask
from flask import render_template
import test as t


app = Flask(__name__)
app.debug=True


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/opcion/<opc>")
def p_(opc):
    if opc=="ida":
        print("Has seleccionado ida.")
        return t.print_zonas()
    elif opc=="idayvuelta":
        return t.idayvuelta()

    elif opc=="mensual":
        return t.mensual()


if __name__ == "__main__":
    app.run()
