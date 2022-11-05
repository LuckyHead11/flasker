from flask import Flask, render_template

#Create flask Instance
app = Flask(__name__)

#Create a route decorater
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html",name=name)


#Custtom error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)