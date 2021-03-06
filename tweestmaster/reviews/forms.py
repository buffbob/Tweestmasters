from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.fields.html5 import IntegerRangeField, DecimalRangeField




class ReviewForm(FlaskForm):
    entertainment_score = IntegerRangeField('Entertainment Value', default=0)
    style_score = IntegerRangeField("Style Value", default=0)
    content = TextAreaField("Comments")
    submit = SubmitField('Submit')

