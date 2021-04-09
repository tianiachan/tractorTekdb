from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    # size = StringField('Size of Puppy (small, medium, large):')
    size = SelectField(u'Pick a size:',
                          choices=[('sm', 'small'), ('med', 'medium'),
                                   ('lg', 'large')])
    age = IntegerField('Age of Puppy (years):')
    breed = StringField('Breed of Puppy:')
    # activity_mode = StringField('Activity mode (couch potato, regular, hyper):')
    activity_mode = SelectField(u'Choose the activity mode:',
                          choices=[('cp', 'couch potato'), ('rg', 'regular'),
                                   ('hy', 'hyper')])
    submit = SubmitField('Add Puppy')

class AddOwnerForm(FlaskForm):

    name = StringField('Name of Foster Pawrent:')
    pup_id = IntegerField("Id of Puppy: ")
    email = StringField('Email: ')
    submit = SubmitField('Add Foster Pawrent')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Adopted Puppy:')
    submit = SubmitField('Remove Adopted Puppy')
