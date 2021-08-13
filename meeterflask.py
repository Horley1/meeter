from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from coords import Cafe
from bs4 import BeautifulSoup
import requests as req






class MetroForm(FlaskForm):
    fa = StringField("")
    fb = StringField("")
        
app = Flask(__name__)

app.config['SECRET_KEY'] = 'pr0tect1v3k3y'


@app.route('/', methods=['POST', 'GET'])
def index():
    form = MetroForm()
    if request.method == 'POST':
    	a=request.form.get('pointa')
    	b=request.form.get('pointb')
    	cafe = Cafe(a, b)
    	title = cafe.gen_pos()[0]['title']
    	address = cafe.gen_pos()[0]['address']
    	time = cafe.gen_pos()[0]['time']
    	url = cafe.gen_pos()[0]['url']   	
    	resp = req.get(url)
    	per = str(cafe.gen_pos()[2])
    	vtor = str(cafe.gen_pos()[3])
    	f_min="Ехать первому: "+per+" "+"мин."
    	sc_min="Ехать второму: "+vtor+" "+"мин."
    	soup = BeautifulSoup(resp.text, 'lxml')
    	menu= "Цитаты из меню:"
    	information="Информация о кофейне:"
    	espresso= "Эспрессо"+" "+soup.find_all("em")[0].text.split()[0]+'₽'
    	cappucino= "Капучино"+" "+soup.find_all("em")[1].text.split()[0]+'₽'
    	metro = "Метро" + " "+ cafe.gen_pos()[1]
    	template_context = dict(title=title, address=address, metro=metro, time=time, url=url, menu=menu, information=information, a=a, b=b, espresso=espresso, cappucino=cappucino, f_min=f_min, sc_min=sc_min)
    	return render_template('index.html', form=form, **template_context)
    return render_template('index.html', form=form)
    
if __name__ == "__main__":
    app.run()

