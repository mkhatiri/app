import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<center><h1>Hello, m2i!  (2025)</h1></center>'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
