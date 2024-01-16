from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit",methods=['GET','POST'])
def subsubmitmit():
    if(request.method=='POST'):
        firstname=str(request.form.get("firstName"))
        lastName=str(request.form.get("lastName"))
        email=str(request.form.get("email"))
        country=str(request.form.get("country"))
        gender=str(request.form.get("gender"))
        return f'{firstname} {lastName} {email} {country} {gender}'
    else:
        return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)