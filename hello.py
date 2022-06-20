from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 

# create a Flask instance
app = Flask(__name__) 


app.config['SECRET_KEY'] = 'SECRET_KEY!!'

# Create a form flask 
class NameForm(FlaskForm): 
    name = StringField('What is your name', validators=[DataRequired()])
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
    form = NameForm()
    # validate 
    if form.validate_on_submit(): 
        name = form.name.data 
        form.name.data = ''
        flash("Form submitted successfully!") 
        
    return render_template('form.html', 
                           name=name, 
                           form=form)
    

