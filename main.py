from flask import Flask, render_template, url_for, request
import csv


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<url>')
def navigate(url):
    try:
        return render_template (url)
    except:
        return render_template ('after_submit.html', submit_text = f"404 OOPS Looks like this {url} page Doesn't Exists")

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method =='POST':
        get_email = request.form['email']
        get_subject = request.form['subject']
        get_message = request.form['message']
        # with open('database.txt','a') as database:
        #     database.write(f'\n{get_email}, {get_subject}, {get_message}')
        
        try:
            with open('database.csv', newline="", mode='a') as database:
                header_writer = csv.DictWriter(database,fieldnames=["E-Mail", "Subject", "Message"])
                header_writer.writeheader()
                write_to_database = csv.writer(database,delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE,escapechar=' ')
                    
                write_to_database.writerow([get_email,get_subject,get_message])
                database.close()
                submit_text = 'Thanks for Contacting Me, I will Reply you soon! '  
                return render_template ("after_submit.html", submit_text = submit_text)
            
        except:
            submit_text = 'OOPS Something Went Wrong'
            return render_template("after_submit.html",submit_text = submit_text)
    else:
        return 'Something Went Wrong Please Try Again'


if __name__ == '__main__':
    app.run(debug=True)

