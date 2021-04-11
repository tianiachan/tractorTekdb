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
    #stretch goal to find a way to populate this programmatically instead of hard coding
    week = SelectField(u'Select the week you want to enter',
                          choices=[('00', 'W0'),
                           ('01', 'W1'),
                           ('02', 'W2'),
                           ('03', 'W3'),
                           ('04', 'W4'),
                           ('05', 'W5'),
                           ('06', 'W6'),
                           ('07', 'W7'),
                           ('08', 'W8'),
                           ('09', 'W9'),
                           ('10', 'W10'),
                           ('11', 'W11'),
                           ('12', 'W12'),
                           ('13', 'W13'),
                           ('14', 'W14'),
                           ('15', 'W15'),
                           ('16', 'W16'),
                           ('17', 'W17'),
                           ('18', 'W18'),
                           ('19', 'W19'),
                           ('20', 'W20'),
                           ('21', 'W21'),
                           ('22', 'W22'),
                           ('23', 'W23'),
                           ('24', 'W24'),
                           ('25', 'W25'),
                           ('26', 'W26'),
                           ('27', 'W27'),
                           ('28', 'W28'),
                           ('29', 'W29'),
                           ('30', 'W30'),
                           ('31', 'W31'),
                           ('32', 'W32'),
                           ('33', 'W33'),
                           ('34', 'W34'),
                           ('35', 'W35'),
                           ('36', 'W36'),
                           ('37', 'W37'),
                           ('38', 'W38'),
                           ('39', 'W39'),
                           ('40', 'W40'),
                           ('41', 'W41'),
                           ('42', 'W42'),
                           ('43', 'W43'),
                           ('44', 'W44'),
                           ('45', 'W45'),
                           ('46', 'W46'),
                           ('47', 'W47'),
                           ('48', 'W48'),
                           ('49', 'W49'),
                           ('50', 'W50'),
                           ('51', 'W51')])
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
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
