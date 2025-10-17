from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/api/v1/<station>/<date>')
# def station():
#     temperature = 23
#     return str(temperature)

@app.route('/api/v1/<word>')
def api(word):
    definition = word.upper()
    dict_response = {
        "word": word,
        "definition": definition
    }
    return dict_response


if __name__ == "__main__":
    app.run(debug=True)