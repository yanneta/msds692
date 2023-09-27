from flask import Flask


# creates an application object
app = Flask(__name__)


# add pages to home page
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

# if you are running the script 
if __name__ == '__main__':
    app.run()


