from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/experiencias")
def experiencias():
    perfil = request.args.get("perfil", "turista")
    return render_template("experiencias.html", perfil=perfil)

@app.get("/ruta")
def ruta():
    ruta = request.args.get("ruta", "clasicos")
    return render_template("ruta.html", ruta=ruta)

@app.get("/feedback")
def feedback():
    return render_template("feedback.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)