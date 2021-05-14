from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/about.html')
def about():
    return render_template('about.html') 


@app.route('/Products.html')
def Products():
    return render_template('Products.html')

@app.route('/Baby Headband & Scrunchies.html')
def BabyHeadbandandScrunchies():
    return render_template('Baby Headband & Scrunchies.html')  

@app.route('/contact.html')
def contact():
    return render_template('contact.html') 

def write_to_file(data): #function for write in a database.txt file 
	with open('database.txt', mode='a') as database:
	  email = data ["email"]
	  subject = data ["subject"]
	  message = data ["message"]
	  file = database.write(f'\n{email},{subject},{message}') # write in a dictonary form 


def write_to_csv(data):  # csv stands for comma separated value ( to write our database in standardize way)
	with open('database.csv', mode='a') as database2: # mode ='a' open the text file for appending text
	  email = data ["email"]
	  subject = data ["subject"]
	  message = data ["message"]
	  csv_writer = csv.writer(database2, delimiter=',', quotechar='"' ,quoting=csv.QUOTE_MINIMAL)
	  csv_writer.writerow([email,subject,message]) # write in a list form

      

@app.route('/submit_form', methods=['POST', 'GET']) 
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data) # all the data entered by customer will store in this database.csv file 
		return redirect('/thankyou.html')
	else:
		return 'something went wrong. Try again!'

