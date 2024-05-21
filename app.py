from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Routes for the pages 

@app.route("/")
def home():
    return render_template('base.html')

@app.route("/rih4krc")
def rih4krc():
    return render_template('rih4krc.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/404")
def contact():
    return render_template('404.html')



if __name__ == "__main__":
    app.run(debug=True)
