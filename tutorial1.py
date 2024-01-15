from flask import Flask,render_template,redirect,url_for
app=Flask(__name__)


@app.route('/')
def home():
    return "hello and welcome"


@app.route("/<name>")
def getdata(name):
    return f'{name}'

@app.route("/admin")

def admin():
    return redirect(url_for("home.html"))



if __name__=="__main__":
    app.run(debug=True)