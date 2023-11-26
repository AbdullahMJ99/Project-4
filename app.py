from flask import Flask, render_template
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')




if __name__ == '__main__':
    app.run()