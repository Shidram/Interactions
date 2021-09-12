from flask import Flask, redirect, url_for, render_template, flash, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
# CSRFProtect(app)
db = SQLAlchemy(app)

class EmployeeModel(db.Model):
    __tablename__ = "employees"
    id = db.Column('id', db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100))
    date_of_joining = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    department= db.Column(db.String(100))
    address = db.Column(db.String(200))
    city = db.Column(db.String(100))

    def __init__(self,firstname,lastname,date_of_joining,department,address,city):
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_joining = date_of_joining
        self.department = department
        self.address = address
        self.city = city

@app.before_first_request
def create_table():
    db.create_all()
    
@app.route('/', methods=['GET','POST'], defaults={'page':1})
@app.route('/<int:page>', methods=['GET', 'POST'])
def get_employee(page):
    page = page
    pages = 5
    employees = EmployeeModel.query.order_by(EmployeeModel.id.asc()).paginate(page,pages,error_out=False)
    # search_fileds = ('firstname','lastname')
    if request.method == 'POST' and 'tag' in request.form:
        tag = request.form['tag']
        search = "%{}%".format(tag)
        employees = EmployeeModel.query.filter(EmployeeModel.firstname.like(search)).paginate(per_page=pages,error_out=True)
        return render_template('index.html', employees=employees,tag=tag)
    return render_template('index.html', employees=employees)

@app.route('/employee/add/',methods=['POST','GET'])
def create():
    if request.method == "POST":
        if not request.form["fName"] and not request.form["Doj"]:
            flash("Please enter all necessary fields")
        else:
            firstname = request.form["fName"]
            lastname = request.form["LName"]
            date_of_joining = request.form["Doj"]
            date_of_joining = datetime.strptime(date_of_joining,"%Y-%m-%d")
            department = request.form["Department"]
            address = request.form["Addr"]
            city = request.form["City"]

            employee = EmployeeModel(firstname,lastname,date_of_joining,department,address,city)
            db.session.add(employee)
            db.session.commit()
            flash("Employee added Successfully.")
            return redirect(url_for('get_employee'))
    return render_template('createpage.html')     

#This route is for Updating a employee info
@app.route('/update', methods = ['POST','GET'])
def update():
    if request.method == 'POST':
        my_data = EmployeeModel.query.get(request.form.get('id'))
        my_data.firstname = request.form['FName']
        my_data.lastname = request.form['LName']
        my_data.department = request.form['Department']
        db.session.commit()
        flash("Employee Updated Successfully")
        return redirect(url_for('get_employee')) 

#This route is for deleting a employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = EmployeeModel.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
    return redirect(url_for('get_employee'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')