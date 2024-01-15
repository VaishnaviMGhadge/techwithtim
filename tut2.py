from flask import Flask,render_template,redirect,url_for
app=Flask(__name__)




@app.route("/<name>/<address>/<email>")
def home(name,address,email):

    return render_template("home.html",content=[name,address,email])

if __name__=="__main__":
    app.run(debug=True)