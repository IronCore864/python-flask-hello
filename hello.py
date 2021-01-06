import os

from flask import Flask
import epsagon


token=os.getenv('EPSAGON_TOKEN', default="")

epsagon.init(
    token=token,
    app_name='Python Hello Flask',
    metadata_only=False
)

app = Flask(__name__)
epsagon.flask_wrapper(app)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
