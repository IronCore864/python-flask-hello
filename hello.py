import os

from flask import Flask
import epsagon


epsagon.init(
    token=os.environ['EPSAGON_TOKEN'],
    app_name='Epsagon Application',
    metadata_only=False
)

app = Flask(__name__)
epsagon.flask_wrapper(app)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
