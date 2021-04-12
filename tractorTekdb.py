import os
from forms import  AddForm 
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from config import username, password, secretKey
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = secretKey

# connect to database
basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mys:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@localhost/tractorTekSales'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#instantiate objects needed
db = SQLAlchemy(app)
# Migrate(app,db)

class tractorSales(db.Model):
    # manually set name of table  to puppies
    __tablename__ = 'weeklySales'
    # set column names
    id = db.Column(db.Integer,primary_key = True)
    # team_lead = db.Column(db.Text)
    employeeid = db.Column(db.Text)
    prod_code = db.Column(db.Text)
    # week = db.Column(db.Text)
    dateEntered = db.Column(db.Date)
    sales_quantity = db.Column(db.Integer)
    # dateEntered = db.Column(db.Integer)
    # owners = db.relationship('Owner',backref='weeklySales',uselist=False)

    # pass in values needed to initiate a puppy objt
    def __init__(self, employeeid, prod_code, sales_quantity, dateEntered):
        # self.team_lead = team_lead
        self.employeeid = employeeid
        self.prod_code = prod_code
        self.dateEntered = dateEntered
        self.sales_quantity = sales_quantity

    #this method is what is called if need a string representation of the object
    def __repr__(self):
        # if self.owners:
        #     return f"Week id: {self.id} | Team Lead: {self.team_lead} | Sales Quantity: {self.sales_quantity}"
        # else:
            return f"Week id: {self.id} | Emp_id: {self.employeeid} | Prod_Code: {self.prod_code} Sales Quantity: {self.sales_quantity}"

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
        # team_lead = form.team_lead.data
        employeeid = form.employeeid.data
        prod_code = form.prod_code.data
        dateEntered = form.dateEntered.data
        sales_quantity = form.sales_quantity.data

        # Add new Puppy to database
        new_week = tractorSales( employeeid, prod_code, dateEntered, sales_quantity)
        db.session.add(new_week)
        db.session.commit()

        return redirect(url_for('list_sales'))

    return render_template('add.html',form=form)

#function to add ownder if at add owner route
# @app.route('/add_owner', methods=['GET', 'POST'])
# def add_owner():

#     form = AddOwnerForm()

#     if form.validate_on_submit():
#         name = form.name.data
#         email = form.email.data
#         pup_id = form.pup_id.data
#         # Add new owner to database
#         new_owner = Owner(name, email, pup_id)
#         db.session.add(new_owner)
#         db.session.commit()

#         return redirect(url_for('list_sales'))

    # return render_template('add_owner.html',form=form)

#display a list of the puppies and owners if it is owned by any owners
@app.route('/list')
def list_sales():
    # Grab a list of puppies from database.
    sales = tractorSales.query.all()
    print(sales)
    return render_template('list.html', sales=sales)

#delete a puppy if no longer needed =(
# @app.route('/delete', methods=['GET', 'POST'])
# def del_pup():

#     form = DelForm()

#     if form.validate_on_submit():
#         id = form.id.data
#         pup = Puppy.query.get(id)
#         db.session.delete(pup)
#         db.session.commit()

#         return redirect(url_for('list_sales'))
#     return render_template('delete.html',form=form)


#if im called main, run me
if __name__ == '__main__':
    app.run(debug=True)#make false if this was actually deployed

