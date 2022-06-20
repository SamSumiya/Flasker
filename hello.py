from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__) 

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