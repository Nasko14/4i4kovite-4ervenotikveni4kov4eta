from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homePage.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.methods=="POST":
        email = request.form["email"]
        password = request.form["pass"]
        user=request.form["user"]
        return redirect(url_for("bee_request"))
    else:
        return render_template("login.html")

@app.route("/bee_request")
def bee_request():
    return render_template("bee_request.html")

@app.route("/login_signin")
def login_signin():
    return render_template("login_signin.html")

if __name__ == "__main__":
    app.run()
