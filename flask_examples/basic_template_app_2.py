from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    some_name = "Pepe"
    return render_template('basic_2.html', name=some_name)

if __name__ == "__main__":
    app.run(debug=True)


