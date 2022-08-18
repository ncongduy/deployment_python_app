from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Home page'

@app.route('/forum', methods=['GET','POST', 'PUT', 'DELETE'])
def forum():
    if request.method == 'POST':
        return 'Accepted'
    elif request.method == 'PUT':
        return 'Updated'
    elif request.method == 'DELETE':
        return 'Deleted'
    else:
        return 'Show articles'

if(__name__ == "__main__"):
    app.run()
