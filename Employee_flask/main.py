from flask import *
from crud_operationdb import *
app = Flask(__name__)
@app.route('/')
def openwebsite():
    name = 'Akshay'
    return render_template('home.html',name=name)

@app.route('/viewemp')
def viewallemp():
    rows = Employee_fetch()
    return render_template('empview.html',rows=rows)

@app.route('/viewdept')
def viewalldept():
    rows = department_fetch()
    return render_template('deptview.html',rows=rows)

@app.route('/adddepartment')
def adddept():
    return render_template('departmentadd.html')

@app.route('/savedepttodb',methods=['POST','GET'])
def save_deptdetails():
    if request.method == 'POST':
        name = request.form["dname"]
        print(name)
        msg = department_insert(name)
        print(msg)
    return render_template('sucess.html',msg=msg)


@app.route('/addemployee')
def addemp():
    return render_template('employeeadd.html')

@app.route('/saveemptodb',methods=['POST','GET'])
def save_empdetails():
    try:
        if request.method == 'POST':
            empname = request.form["ename"]
            emp_salary = request.form["esalary"]
            emp_email = request.form["eemail"]
            empdoj = request.form["eDOJ"]
            empdeptid = request.form["edeptID"]
            emplocation = request.form["elocation"]
            empgender = request.form["egender"]
            msg = Employee_insert(empname,emp_salary,emp_email,empdoj,empdeptid,emplocation,empgender)
    except:
        msg="Not Inserted Successfully"

    finally:
        return render_template('sucess.html', msg=msg)

@app.route('/<id>/dDelete')
def dept_delete(id):
    msg = single_dep_delete(id)
    return render_template('sucess.html',msg=msg)

@app.route('/<id>/eDelete')
def emp_delete(id):
    msg = single_emp_delete(id)
    return render_template('sucess.html',msg=msg)


@app.route('/<id>/dedit')
def dept_edit(id):
    rows = department_fetch_single(id)
    return render_template('department_update.html',rows=rows)

@app.route('/updatedepttodb',methods=['POST','GET'])
def update_dept():
    if request.method == 'POST':
        id = request.form['did']
        name = request.form['dname']
        print(name)
        msg = update_department(name,id)
        print(msg)
    return render_template('sucess.html',msg=msg)


@app.route('/<id>/eedit')
def employees_edit(id):
    rows=Employee_fetch_single(id)
    print(rows)
    return render_template('Employee_update.html',rows=rows)


@app.route('/updateemptodb',methods=['POST','GET'])
def update_employee_db():
    if request.method == 'POST':
        id= request.form['eid']
        name = request.form['ename']
        salary =request.form['esalary']
        email =request.form['eemail']
        doj=request.form['eDOJ']
        department_id=request.form['edeptID']
        location=request.form['elocation']
        gender=request.form['egender']
        print("_")
        msg = update_Employees(id,name,salary,email,doj,department_id,location,gender)
    return render_template('sucess.html',msg=msg)

if __name__ == '__main__':
    app.run()
