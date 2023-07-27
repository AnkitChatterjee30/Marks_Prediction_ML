from flask import Flask,render_template,request
import marks as m
import numpy as np
app=Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def hello():
    if request.method =='POST':
        hrs=float(request.form['hours'])
        cos=float(request.form['courses'])
        marks_pred = m.marks_prediction(hrs, cos)
        mks = marks_pred[0]
    else:
        mks = 0
    return render_template("index.html", my_marks=mks)
@app.route('/submit',methods=['POST'])
def submit():
    if request.method =='POST':
        hrs=float(request.form['hours'])
        cos=float(request.form['courses'])
        naam=request.form['naam']
        marks_pred = m.marks_prediction(hrs, cos)
        mks = marks_pred[0]
    else:
        mks = 0
        naam=''
    return render_template("submit.html", my_marks=mks,boog=naam)
if __name__=='__main__':
    app.run(debug=True)