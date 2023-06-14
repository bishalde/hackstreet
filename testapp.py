from flask import *
import os

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def hello_world():
    return render_template("indexfake.html")

@app.route('/bpfake',methods=['POST','GET'])
def bpfakes():
    return render_template("bpfake.html")


app.run(debug=True)