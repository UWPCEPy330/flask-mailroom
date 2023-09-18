import os
import base64

from flask import Flask, render_template, request, redirect, url_for

from model import Donation, Donor

app = Flask(__name__)
app.secret_key = b'\x9d\xd1u\x08%\xe0\xd0p\x9bEL\xf8JC\xa3\xf4J(hAh\xa4\xcdw\x12S*,u\xec\xb8\xb8'

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)
    
@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        donor = request.form['name']
        donor_db = Donor.select().where(Donor.name == donor)
        donation = request.form['donation']
        if donor_db:
            Donation(donor=donor_db, value=int(donation)).save()
            return redirect(url_for('all'))
        else:
            return render_template('create.jinja2')
    else:
        return render_template('create.jinja2')
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

