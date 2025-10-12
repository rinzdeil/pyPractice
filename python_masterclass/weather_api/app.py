from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Check this line for typos
    return render_template('index.html') 

@app.route("/about/")
def about():
    return render_template("about.html")

app.run(debug=True)
# Common typo: return render_template('Index.html') 
# when the file is 'index.html'