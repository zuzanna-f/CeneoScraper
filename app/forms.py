from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class ProductForm(FlaskForm):
    product_code = StringField(
        "Podaj kod produktu do pobrania opinii", 
        validators=[
            DataRequired(message="Musisz podać kod produktu"),
            Length(min=8, max=8, message="Kod produktu musi mieć 8 znaków"),
            Regexp(regex="^[0-9]+$", message="Kod produktu może zawierać tylko cyfry")
        ]
    )
    submit = SubmitField("Pobierz")