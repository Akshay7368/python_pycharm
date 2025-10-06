import csv
from tkinter import *
from tkcalendar import DateEntry
root = Tk()
root.title('My sample')
root.geometry('400x400')

Label(root, text='student_id').grid(row=0, column=0)
st_ID = IntVar()
Entry(root, textvariable=st_ID).grid(row=0, column=1)
st_ID.set('')

Label(root, text='student_name').grid(row=1, column=0)
st_name = StringVar()

Entry(root, textvariable=st_name).grid(row=1, column=1)
st_name.set('')

Label(root, text='Mark1').grid(row=2, column=0)
Mark1 = IntVar()
Entry(root, textvariable=Mark1).grid(row=2, column=1)
Mark1.set('')

Label(root, text='Mark2').grid(row=3, column=0)
Mark2 = IntVar()
Entry(root, textvariable=Mark2).grid(row=3, column=1)
Mark2.set('')

Label(root, text='Mark3').grid(row=4, column=0)
Mark3 = IntVar()
Entry(root, textvariable=Mark3).grid(row=4, column=1)
Mark3.set('')

Label(root,text="DOB").grid(row=5, column=0)
dob = StringVar()
DateEntry(root,textvariable=dob).grid(row=5, column=1)

Label(root, text="Gender").grid(row=6, column= 0)
stggender = IntVar()
Radiobutton(root, text="Male", variable=stggender, value=1).grid(row=6, column=1)
Radiobutton(root, text="Female", variable=stggender, value=2).grid(row=6, column=2)


def Save_to_file():
    a = st_ID.get()
    b = st_name.get()
    c = Mark1.get()
    d = Mark2.get()
    e = Mark3.get()
    total = c+d+e
    do = dob.get()
    Avg = int(total / 3)
    if stggender.get() == 1:
        gender = "Male"
    else:
        gender = "Female"

    print(a, b, c, d, e, do, total, Avg, gender)

    with open('student_details.csv', mode='a', newline='') as file:
        w = csv.writer(file)
        w.writerow([a, b, c, d, e, total, Avg, do, gender])
    root.destroy()


Button(root, text="Submit", command=Save_to_file).grid(row=7, column=1)
root.mainloop()

