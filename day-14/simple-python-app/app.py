from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Change the host to '0.0.0.0' to listen on all network interfaces
    app.run(host='0.0.0.0', port=5000)
