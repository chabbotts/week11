from flask import Flask, Response, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("index.html", content=["Pri", "Tasha", "Charlotte"], cheese="Do you like Camembert?")

# we are rendering the index.html and pass the variable content the value of name.

# Below are the attempts to link the html pages to each other... if this is possible
@app.route("/pri")
def open_pri():
    # url = url_for('get_text')
    # f = open('templates/pri.html', 'r')
    return render_template("pri.html")


@app.route("/charlotte")
def open_charlotte():
    return render_template("charlotte.html")


@app.route("/tasha")
def open_tasha():
    return render_template("tasha.html")

#
# @app.route("/")
# def pri():
#     return render_template("pri.html", title="Pri's page")


# @app.route('/Picture')
# def picture():
#     return Response("Thank you for visiting", mimetype='text/plain')


# @app.route("/pri.html")
# def user():
#     return f"Hello {user}!"


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))


if __name__ == "__main__":
    app.run(debug=True, port=4001)