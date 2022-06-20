from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from sqlalchemy.orm import declarative_base
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from datetime import datetime
meta = MetaData() 



Base = declarative_base() 

# create a Flask instance
app = Flask(__name__) 

# add database 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flask_test'

# Secret key
app.config['SECRET_KEY'] = 'SECRET_KEY!!'

# db init
db = SQLAlchemy(app)

# create engine 
engine = create_engine('postgresql://localhost/flask_test')

# create model
class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # create a string
    def __repr__(self): 
        return self.name - self.email - self.created_at

# Create a form flask 
class UserForm(FlaskForm): 
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your email?',  validators=[DataRequired()])
    submit = SubmitField('Submit')

# Create a route decorator
@app.route('/', methods=['GET'])
def index():
    first_name = 'Tim'
    sentence = "This is a <strong>bold</strong>"
    favorite_pizza=['Pepperoni', 'Cheese', 'Mushrooms', 11]
    
    return render_template('index.html', 
                           first_name=first_name,
                           sentence=sentence,
                           favorite_pizza=favorite_pizza
                           )

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# Invalid URL
@app.errorhandler(404)
def page_not_found(error): 
    return render_template('404.html', error=error)

# Internal Server Error

@app.errorhandler(500)
def page_not_found(error): 
    return render_template('500.html', error=error)


@app.route('/name', methods=['GET', 'POST'])
def form():
    name = None
    email = None
    form = UserForm()
    # validate 
    if form.validate_on_submit(): 
        user = User.query.filter_by(email=form.email.data).first() 
        if user in None: 
            user = User(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.commit()
        name = form.name.data 
        email = form.email.data
        form.name.data = ''
        form.email.data = '' 
        flash("Form submitted successfully!") 
        
    return render_template('form.html', 
                           name=name, 
                           email = email, 
                           form=form)
    

meta.create_all(engine)