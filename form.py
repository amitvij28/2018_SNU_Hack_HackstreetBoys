from flask_wtf import FlaskForm
from wtforms import SelectField

regionsVolume = [('IN','India'),('US','United States'),('EU','Europe'),('CH','China'),('SN','Singapore')]
countries=[('IN','India'),('CA','Canada'),('US','United States')]


class Volume(FlaskForm):
    region = SelectField('Region:',choices=regionsVolume)


class Trends(FlaskForm):
    country = SelectField('Country:',choices = countries)   
    state = SelectField('State:',choices=[])

