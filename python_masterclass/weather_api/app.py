from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/stations/')
def index():
    return render_template('stations.html') 

@app.route('/words/')
def index():
    return render_template('words.html') 

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    return render_template("api.html")

if __name__ == "__main__":
    app.run(debug=True)