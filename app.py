from flask import Flask
app = Flask(__name__)

@app.route('/checkouts/new')
def new_checkout():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
