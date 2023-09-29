from flask import Flask


# creates an application object
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Everyone!</h1>'

# add dynamic pages
@app.route('/<name>')
def index_name(name):
    return '<h1>Hello {}!</h1>'.format(name)

# if you are running the script 
if __name__ == '__main__':
    app.run()


