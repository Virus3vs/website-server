from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def pages_name(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
    	data = request.form.to_dict()
    	with open('database.csv', 'a', newline='') as database:
    		email = data["email"]
    		subject = data["subject"]
    		message = data["message"]
    		csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    		csv_writer.writerow([email,subject,message])
    	return 'form submitted'
    else:
    	'prooblom'

#@app.route('/components.html')
#def components():
#	return render_template('components.html')

