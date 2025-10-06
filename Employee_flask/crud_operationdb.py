import sqlite3

from ipywidgets.embed import dependency_state


def department_insert(dname):
        conn = sqlite3.connect('empflask.db')
        cur = conn.cursor()
        dep_ins = f"insert into department(Department_name) Values('{dname}')"
        cur.execute(dep_ins)
        conn.commit()
        cur.close()
        return f"{dname} Inserted Successfully"

# department_insert('Manager')

def Employee_insert(ename,Salary,Email,Doj,Did,loc,gen):
    conn = sqlite3.connect('empflask.db')
    cur = conn.cursor()
    dep_ins = f"insert into Employees(Emp_name,Emp_Salary,Emp_Email,Emp_Doj,Department_id,Location,Gender) Values('{ename}',{Salary},'{Email}','{Doj}',{Did},'{loc}','{gen}')"
    cur.execute(dep_ins)
    conn.commit()
    cur.close()
    return "Inserted Successfully"

# Employee_insert('Arun',30000,'Ar@gmail.com','2025-01-01',1,'Mumbai','Male')


def department_fetch():
    conn = sqlite3.connect('empflask.db')
    curr = conn.cursor()
    dsql = f"select * from Department"
    fet = curr.execute(dsql).fetchall()
    for row in fet:
        print(row)
    return fet

# department_fetch()

def Employee_fetch():
    conn = sqlite3.connect('empflask.db')
    curr = conn.cursor()
    dsql = f"select * from Employees"
    fet = curr.execute(dsql).fetchall()
    for row in fet:
        print(row)
    return fet

# Employee_fetch()


def department_fetch_single(did):
    conn = sqlite3.connect('empflask.db')
    curr = conn.cursor()
    dsql = f"select * from Department where Department_id = {did}"
    fet = curr.execute(dsql).fetchall()
    return fet
# department_fetch(2)


def Employee_fetch_single(eid):
    conn = sqlite3.connect('empflask.db')
    curr = conn.cursor()
    dsql = f"select * from Employees where Emp_id = {eid}"
    fet = curr.execute(dsql).fetchall()
    return fet

# Employee_fetch(2)


def Department_delete():
    conn = sqlite3.connect('empflask.db')
    cur = conn.cursor()
    delsql = f"delete from Department"
    cur.execute(delsql)
    conn.commit()
    cur.close()


def Employee_delete():
    conn = sqlite3.connect('empflask.db')
    cur = conn.cursor()
    delsql = f"delete from Employees"
    cur.execute(delsql)
    conn.commit()
    cur.close()


def single_dep_delete(did):
    conn = sqlite3.connect('empflask.db')
    cur = conn.cursor()
    delsql = f"delete from Department where Department_id = {did}"
    cur.execute(delsql)
    conn.commit()
    cur.close()
    return f"Department id: {did} Deleted Successfully"


def single_emp_delete(eid):
    conn = sqlite3.connect('empflask.db')
    cur = conn.cursor()
    delsql = f"delete from Employees where Emp_id = {eid}"
    cur.execute(delsql)
    conn.commit()
    cur.close()
    return f"Employee id: {eid} Deleted Successfully"


def update_department(dname, did):
    conn = sqlite3.connect('empflask.db')
    cur = conn.cursor()
    upsql = f"update Department set Department_name = '{dname}' where Department_id = {did}"
    cur.execute(upsql)
    conn.commit()
    cur.close()
    return "Updated Sucessfully"

#update_department('Team leader', 3)


def update_Employees(eid,ename,salary,email,doj,did,loc,gen):
    conn = sqlite3.connect('empflask.db')
    cur = conn.cursor()
    upsql = f"update Employees set Emp_name ='{ename}', Emp_Salary = {salary},Emp_Email = '{email}', Emp_Doj = '{doj}',  Department_id = {did}, Location = '{loc}', Gender ='{gen}'  where Emp_id = '{eid}'"
    cur.execute(upsql)
    conn.commit()
    cur.close()
    return "Updated Sucessfully"
#update_Employees('Hyderabad', 'Akshay')












