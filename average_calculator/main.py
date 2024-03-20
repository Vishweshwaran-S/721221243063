from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///numbers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class number(db.Model):
    numbers=db.Column(db.Integer,primary_key=True)
    windowPrevState=db.Column(db.Integer)
    windowCurrState=db.Column(db.Integer)
    avg=db.Column(db.Float)

    def __init__(self,number):
        return f'<number {self.avg}>'
    
@app.route('/e',methods=['POST'])
def average():
    data=request.json()
    numbers=data.get('numbers')
    windowPrevState=data.get('windowPrevState')
    windowCurrState=data.get('windowCurrState')
    avg=generate_avg()
    new_number=number(numbers=numbers,windowPrevState=windowPrevState,windowCurrState=windowCurrState)
    db.session.add(new_number)
    db.session.commit()

    return jsonify({'numbers':numbers,'windowPrevState':windowPrevState,'windowCurrState':windowCurrState,'avg':avg})

def generate_avg(numbers):
    a=0
    for n in numbers:
        a+=n
    return a/len(numbers)







    

if __name__=='__main__':
    app.run(debug=True)