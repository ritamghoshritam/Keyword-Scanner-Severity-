from flask import Flask, render_template, url_for ,request,flash,send_file,redirect
from werkzeug import secure_filename
import os
import urllib.request
from app import app
from werkzeug.utils import secure_filename
from severity import validation
from mail_send import emailing,third_party_email
from mail_receive import receive

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

userid=0
password=0
send_to=""
send_from=""
subj=""
mess=""
send_file=0

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


	
@app.route('/')
def upload_form():
    flash("login page")
    return render_template('login.html')


@app.route('/',methods=['POST','GET'])
def login_page():
    
    if request.method=="POST":
        global userid
        global password
        global send_to
        global send_from
        global subj
        global mess
        global send_file
        #send_file = request.files['f']
        #send_file.save(secure_filename(send_file.filename))
        userid=request.form["uid"]
        password=request.form["psw"]
        send_to=request.form["to"]
        send_from=request.form["from"]
        subj=request.form["sub"]
        mess=request.form["msg"]
        print(send_to)
        #print(send_file)
        #flash("submitted")
        #return render_template('login.html')
        
        if 'f' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['f']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            s=validation(filename)
            if s>=80:
                    #flash("Severity is high! File cant be sent")
                    third_party_email(subj,mess,userid,send_to,password,filename)
                    i=receive()
                    if i==True:
                            j=emailing(subj,mess,userid,send_to,password,filename)
                            if j==True:
                                    flash("Mail sent successfully!")
                            else:
                                    flash("Wrong ID or Password!")
                          
                    else:
                            flash("Message cant be send")
            else:
                    i=emailing(subj,mess,userid,send_to,password,filename)
                    if i==True:
                            flash("Mail sent successfully!")
                    else:
                            flash("Wrong ID or Password!")
            return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)
        
    #else:
        #flash("login page")
        #return render_template('login.html')
'''
@app.route('/sending/',methods=['POST','GET'])
def compose_page():
    
    if request.method=="POST" or request.method=="GET":
        global send_to
        global send_from
        global subj
        global mess
        global send_file
        send_to=request.form["to"]
        send_from=request.form["from"]
        subj=request.form["sub"]
        mess=request.form["msg"]
        print(mess)
        print(send_to)
        print("hi")
        #send_file = request.files['file']
        #print(send_file)

        flash("mail sent")
        return render_template("compose.html")

    else:
        print("hi2")
        flash("compose the mail")
        return render_template("compose.html")
    
    flash("Compose the Mail")
    return render_template('compose.html')

'''




if __name__=="__main__":
    app.run(debug=True)
