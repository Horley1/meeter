from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from coords import Cafe

class MetroForm(FlaskForm):
    fa = StringField("")
    fb = StringField("")
        
app = Flask(__name__)

app.config['SECRET_KEY'] = 'pr0tect1v3k3y'


@app.route('/', methods=['POST', 'GET'])
def index():
    form = MetroForm()
    if request.method == 'POST':
    	a=request.form.get('metroa')
    	b=request.form.get('metrob')
    	cafe = Cafe(a, b)
    	title = cafe.gen_pos()[0]['title']
    	address = cafe.gen_pos()[0]['address']
    	time = cafe.gen_pos()[0]['time']
    	url = cafe.gen_pos()[0]['url']
    	metro = cafe.gen_pos()[1]
    	template_context = dict(title=title, address=address, metro=metro, time=time, url=url)
    	return render_template('index.html', form=form, **template_context)
    return render_template('index.html', form=form)
    
if __name__ == "__main__":
    app.run()

