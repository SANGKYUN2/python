from flask import Flask
from routes import bbsRoute

app = Flask(__name__, template_folder='templates')
app.register_blueprint(bbsRoute.bp)

@app.route('/')

def index():
    return "hello"

if __name__ == '__main__':
    app.run(port=5000, debug=True)