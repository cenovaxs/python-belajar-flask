# linux/mac
# buat venv di vscode bash "python3 -m venv env"
# aktifkan venv "source flask_env/bin/activate"


# pip3 install flask

# windows
# buat venv di vscode bash "python -m venv env"

# aktifkan venv
# env bypass "Set-ExecutionPolicy -Scope CurrentUser Unrestricted"
# menjalankan (powershell) "env flask_env\Scripts\activate.ps1"

# jangan lupa di vs code open folder di flask_env agar tidak bentrok python env dengan yang asli

# pip install flask

# untuk manual
# set for windows, export for mac, linux
# to "set FLASK_APP=flasklearn.py"
# live view (debugger) "set FLASK_DEBUG=1"
# run "flask run"

# untuk melihat working directory python:
# import os
# print(os.getcwd())


from flask import Flask, render_template

app = Flask(__name__)

ganti = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Pujas Sutanto",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "May 25, 2019",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=ganti)


@app.route("/about")
def about():
    return render_template("about.html", title="about")


# jalan secara automatic run di terminal "python flaskblog.py"
if __name__ == "__main__":
    app.run(debug=True)
