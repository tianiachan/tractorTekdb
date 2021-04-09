import os
from forms import  AddForm , DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import username, password, secretKey
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = secretKey

# connect to database
basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mys:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@localhost/puppydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#instantiate objects needed
db = SQLAlchemy(app)
# Migrate(app,db)

class Puppy(db.Model):
    # manually set name of table  to puppies
    __tablename__ = 'puppies'
    # set column names
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    size = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)
    activity_mode = db.Column(db.Text)
    owners = db.relationship('Owner',backref='puppies',uselist=False)

    # pass in values needed to initiate a puppy objt
    def __init__(self,name,size,age,breed, activity_mode):
        self.name = name
        self.size = size
        self.age = age
        self.breed = breed
        self.activity_mode = activity_mode

    #this method is what is called if need a string representation of the object
    def __repr__(self):
        if self.owners:
            return f"Puppy id: {self.id} | Name: {self.name} | Foster Pawrent: {self.owners.name}"
        else:
            return f"Puppy id: {self.id} | Name: {self.name} | Foster Pawrent: ---"

class Owner(db.Model):

    __tablename__ = 'owners'

    #set column names
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    # We use puppies.id because __tablename__='puppies'
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,email,puppy_id):
        self.name = name
        self.puppy_id = puppy_id
        self.email = email

    def __repr__(self):
        return f"Owner Name: {self.name}"

#create all tables
db.create_all()

#home page
@app.route('/')
def index():
    return render_template('home.html')

#function to add puppy if at add puppy route
@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    #check that the values passed in are the correct data values using this method
    if form.validate_on_submit():
        name = form.name.data
        size = form.size.data
        age = form.age.data
        breed = form.breed.data
        activity_mode = form.activity_mode.data

        # Add new Puppy to database
        new_pup = Puppy(name, size, age, breed, activity_mode)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html',form=form)

#function to add ownder if at add owner route
@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():

    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        pup_id = form.pup_id.data
        # Add new owner to database
        new_owner = Owner(name, email, pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_owner.html',form=form)

#display a list of the puppies and owners if it is owned by any owners
@app.route('/list')
def list_pup():
    # Grab a list of puppies from database.
    puppies = Puppy.query.all()
    print(puppies)
    return render_template('list.html', puppies=puppies)

#delete a puppy if no longer needed =(
@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html',form=form)


#if im called main, run me
if __name__ == '__main__':
    app.run(debug=True)#make false if this was actually deployed

