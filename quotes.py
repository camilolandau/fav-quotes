from flask import Flask ,render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:T%r4e3w2q1@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://ddziwoqhejthyf:caed3eb89c726569e8b42181d2a997168c3bf44285687bd02815030ad90dc3db@ec2-54-204-96-190.compute-1.amazonaws.com:5432/d3frpg3nibirkj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods =['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata =Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))
