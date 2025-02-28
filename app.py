from flask import Flask 

app = Flask(__name__)


@app.route('/app', defaults={'my_path': ''})
@app.route('/app/<path:my_path>')
def index(my_path): 
    return "Hello "+my_path
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
