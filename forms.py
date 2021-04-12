from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField

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
                           ('PROD_008', 'PROD_008')])
    #stretch goal to find a way to populate this programmatically instead of hard coding
    week = SelectField(u'Select the week you want to enter',
                          choices=[('W0', 'W0'),
                           ('W1', 'W1'),
                           ('W2', 'W2'),
                           ('W3', 'W3'),
                           ('W4', 'W4'),
                           ('W5', 'W5'),
                           ('W6', 'W6'),
                           ('W7', 'W7'),
                           ('W8', 'W8'),
                           ('W9', 'W9'),
                           ('W10', 'W10'),
                           ('W11', 'W11'),
                           ('W12', 'W12'),
                           ('W13', 'W13'),
                           ('W14', 'W14'),
                           ('W15', 'W15'),
                           ('W16', 'W16'),
                           ('W17', 'W17'),
                           ('W18', 'W18'),
                           ('W19', 'W19'),
                           ('W20', 'W20'),
                           ('W21', 'W21'),
                           ('W22', 'W22'),
                           ('W23', 'W23'),
                           ('W24', 'W24'),
                           ('W25', 'W25'),
                           ('W26', 'W26'),
                           ('W27', 'W27'),
                           ('W28', 'W28'),
                           ('W29', 'W29'),
                           ('W30', 'W30'),
                           ('W31', 'W31'),
                           ('W32', 'W32'),
                           ('W33', 'W33'),
                           ('W34', 'W34'),
                           ('W35', 'W35'),
                           ('W36', 'W36'),
                           ('W37', 'W37'),
                           ('W38', 'W38'),
                           ('W39', 'W39'),
                           ('W40', 'W40'),
                           ('W41', 'W41'),
                           ('W42', 'W42'),
                           ('W43', 'W43'),
                           ('W44', 'W44'),
                           ('W45', 'W45'),
                           ('W46', 'W46'),
                           ('W47', 'W47'),
                           ('W48', 'W48'),
                           ('W49', 'W49'),
                           ('W50', 'W50'),
                           ('W51', 'W51')])
    # activity_mode = StringField('Activity mode (couch potato, regular, hyper):')
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
