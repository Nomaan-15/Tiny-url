from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import pyshorteners

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class ShortenForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def shorten_url():
    form = ShortenForm()
    shortened_url = None

    if form.validate_on_submit():
        url = form.url.data
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(url)

    return render_template('index.html', form=form, shortened_url=shortened_url)

if __name__ == '__main__':
    app.run(debug=True)
