from flask import Flask, render_template, request, redirect, url_for
import datetime
app = Flask(__name__)
app.debug = True

# everything is stored in this dictionary
dict = {}

@app.route('/')
def basic_info():
    return render_template('basic_info.html')

# incomplete: Auto-generate Ref number (eg: SMC2021-number > [COMM][AY]-[NUM][T/C/E])
@app.route('/claims', methods = ['POST', 'GET'])
def claims():
    print(request.form)
    dict.update(request.form)
    if request.method == 'POST':
        return render_template('claims.html')

@app.route('/receipt_acknowledgement', methods = ['POST', 'GET'])
def formA_input():
    # print(request.form)
    dict.update(request.form)
    return render_template('formA_input.html')

# incomplete!
@app.route('/formA', methods = ['POST', 'GET'])
def formA():
    dict.update(request.form)
    print(dict)
    datetimeobject = datetime.datetime.strptime(dict["date"], '%Y-%m-%d')
    date = datetimeobject.strftime('%d/%m/%Y')

    if dict["reasonack"] == "not_issued":
        reasonack = "NO RECEIPT WAS ISSUED"
    elif dict["reasonack"] == "lack_info":
        reasonack = "ORIGINAL RECEIPT LACK INFORMATION ON SUPPLIER"
    elif dict["reasonack"] == "damage":
        reasonack = "RECEIPT DAMANGED BEYOND SALVAGE"
    else:
        reasonack = "ORIGINAL RECEIPT LACK INFORMATION ON SUPPLIER/RECEIPT DAMANGED BEYOND SALVAGE/NO RECEIPT WAS ISSUED"
    
    if dict["remarks"] == "":
        remarks = "___"
        print(remarks)
        print('got it')
    else: 
        remarks = dict["remarks"]

    return render_template('formA.html', date= date, input_dict= dict, reasonack= reasonack, remarks= remarks)

# incomplete!
@app.route('/formA1')
def formA1():
    return render_template('formA1.html')

# incomplete!
@app.route('/formA2')
def formA2():
    return render_template('formA2.html')

# incomplete: Auto-generate Code number
# IF GOT TIME: Make this a downloadable form through button click, on this html list the things they need to prepare for WQ
@app.route('/formB', methods = ['POST', 'GET'])
def formB():
    dict.update(request.form)
    name = dict["name"]
    matric = dict["matric"]
    contact = dict["contact"]
    event = dict["event"]
    ref = dict["ref"]
    old_date = dict["date"]
    datetimeobject = datetime.datetime.strptime(old_date, '%Y-%m-%d')
    date = datetimeobject.strftime('%d/%m/%Y')

    print(dict)
    if request.method == 'POST':
        return render_template('formB.html', name = name, matric = matric, contact = contact, event = event, ref = ref, date = date)

# incomplete!
@app.route('/formC')
def formC():
    return render_template('formC.html')

# incomplete!
@app.route('/formD')
def formD():
    return render_template('formD.html')


# incomplete!
@app.route('/formE')
def formE():
    return render_template('formE.html')

# IN PROGRESS: Upload receipts (https://www.tutorialspoint.com/flask/flask_file_uploading.htm)
# IN PROGRESS: Mail? For those that need approval first (https://www.tutorialspoint.com/flask/flask_mail.htm)
# Deployment (https://www.tutorialspoint.com/flask/flask_deployment.htm)

if __name__ == '__main__':
   app.run(debug = True)