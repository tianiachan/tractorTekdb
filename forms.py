from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField

class AddForm(FlaskForm):

    team_lead = SelectField(u'Select your Team Lead:',
                          choices=[('ge', 'Evans, Gina'),
                           ('lh', 'Lawson, Harry'),
                           ('jb', 'Bachmann, Jane'),
                           ('bc', 'Clement, Beverly'),
                           ('ma', 'Allen, Maude')])

    #to be changed as we figure out if need the team lead id as well
    employeeid = SelectField(u'What is your employee id?',
                          choices=[('244', 'EMP244'),
                           ('256', 'EMP256'),
                           ('234', 'EMP234'),
                           ('267', 'EMP267'),
                           ('290', 'EMP290')])
    prod_code = SelectField(u'Select the product code',
                          choices=[('001', 'PROD_001'),
                           ('002', 'PROD_002'),
                           ('003', 'PROD_003'),
                           ('004', 'PROD_004'),
                           ('005', 'PROD_005'),
                           ('006', 'PROD_006'),
                           ('007', 'PROD_007'),
                           ('008', 'PROD_008')])
    week = StringField('Breed of Puppy:')
    # activity_mode = StringField('Activity mode (couch potato, regular, hyper):')
    sales_quantity = SelectField(u'Choose the activity mode:',
                          choices=[('cp', 'couch potato'), ('rg', 'regular'),
                                   ('hy', 'hyper')])
    submit = SubmitField('Add Sales Information')

# class AddOwnerForm(FlaskForm):

#     name = StringField('Name of Foster Pawrent:')
#     pup_id = IntegerField("Id of Puppy: ")
#     email = StringField('Email: ')
#     submit = SubmitField('Add Foster Pawrent')

# class DelForm(FlaskForm):

#     id = IntegerField('Id Number of Adopted Puppy:')
#     submit = SubmitField('Remove Adopted Puppy')
