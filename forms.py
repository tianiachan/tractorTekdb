from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, SubmitField

class AddForm(FlaskForm):
    #select field: 1st value is for into database, 2nd is what is displayed, in this case we want them the same
    # team_lead = SelectField(u'Select your Team Lead:',
    #                       choices=[('Evans, Gina', 'Evans, Gina'),
    #                        ('Lawson, Harry', 'Lawson, Harry'),
    #                        ('Bachmann, Jane', 'Bachmann, Jane'),
    #                        ('Clement, Beverly', 'Clement, Beverly'),
    #                        ('Allen, Maude','Allen, Maude')])
    #team lead not needed since matches the emp id

    #to be changed as we figure out if need the team lead id as well
    employeeid = SelectField(u'What is your employee id?',
                          choices=[('EMP244', 'EMP244'),
                           ('EMP256', 'EMP256'),
                           ('EMP234', 'EMP234'),
                           ('EMP267', 'EMP267'),
                           ('EMP290', 'EMP290')])
    prod_code = SelectField(u'Select the product code',
                          choices=[('PROD_001', 'PROD_001'),
                           ('PROD_002', 'PROD_002'),
                           ('PROD_003', 'PROD_003'),
                           ('PROD_004', 'PROD_004'),
                           ('PROD_005', 'PROD_005'),
                           ('PROD_006', 'PROD_006'),
                           ('PROD_007', 'PROD_007'),
                           ('PROD_008', 'PROD_008'),
                           ('ESP_001', 'ESP_001'),
                           ('ESP_002', 'ESP_002'),
                           ('ESP_003', 'ESP_003'),
                           ('ESP_004', 'ESP_004'),
                           ('ESP_005', 'ESP_005'),
                           ('ESP_006', 'ESP_006')])
    # dateEntered = DateField("Input the date in this format mm/dd/yyyy", format='%m/%d%Y')
    sales_quantity = IntegerField("How many units of the product was sold that week?")
    submit = SubmitField('Add Sales Information')

# class AddOwnerForm(FlaskForm):

#     name = StringField('Name of Foster Pawrent:')
#     pup_id = IntegerField("Id of Puppy: ")
#     email = StringField('Email: ')
#     submit = SubmitField('Add Foster Pawrent')

# class DelForm(FlaskForm):

#     id = IntegerField('Id Number of Adopted Puppy:')
#     submit = SubmitField('Remove Adopted Puppy')
