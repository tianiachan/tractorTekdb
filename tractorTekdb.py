import os
from forms import  AddForm 
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
#legacy code
# from flask_migrate import Migrate
from config import username, password, secretKey
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = secretKey

# connect to database
basedir = os.path.abspath(os.path.dirname(__file__))
#legacy code
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mys:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@localhost/tractorTekSales'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#instantiate objects needed
db = SQLAlchemy(app)
#legacy code
# Migrate(app,db)

class tractorSales(db.Model):
    # manually set name of table  to puppies
    __tablename__ = 'tractor_sales'
    # set column names
    emp_id = db.Column(db.Text, primary_key = True)
    item_id = db.Column(db.Text, primary_key = True)
    year = db.Column(db.Integer)
    week = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Integer)

    # pass in values needed to initiate a puppy objt
    def __init__(self, emp_id, item_id, year, week, quantity):
        self.emp_id = emp_id
        self.item_id = item_id
        self.year = year
        self.week = week
        self.quantity = quantity

    #this method is what is called if need a string representation of the object
    def __repr__(self):
            return f"Week: {self.week} | Emp_id: {self.emp_id} | Prod_Code: {self.item_id} Sales Quantity: {self.quantity}"

#create all tables
db.create_all()

#home page
@app.route('/')
def index():
    return render_template('home.html')

#function to add weekly sales 
@app.route('/add', methods=['GET', 'POST'])
def add_weeklySales():
    form = AddForm()

    #check that the values passed in are the correct data values using this method
    if form.validate_on_submit():
        #error checking for quantity
        if form.quantity.data < 1 or form.quantity.data > 200:
            flash("Please enter valid quantity between 1 and 200")
            return redirect(url_for('add_weeklySales'))
        emp_id = form.emp_id.data
        item_id = form.item_id.data
        year = form.year.data
        week = form.week.data
        quantity = form.quantity.data

        # Add new week to database
        new_week = tractorSales( emp_id, item_id, year, week, quantity)
        db.session.add(new_week)
        db.session.commit()
        #went through, show list
        return redirect(url_for('list_sales'))

    return render_template('add.html',form=form)

#display a list of entered sales data
@app.route('/list')
def list_sales():
    sales = tractorSales.query.all()
    print(sales)
    return render_template('list.html', sales=sales)

#if im called main, run me
if __name__ == '__main__':
    app.run(debug=True)#make false if this was actually deployed

