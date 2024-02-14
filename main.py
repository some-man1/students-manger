import sqlite3 ,tkinter
from datetime import datetime


#---------config windo-------
windo = tkinter.Tk()
windo.geometry("1300x600")
windo.title("studint manger")


#---------functions---------
def insert():
    name = input1.get()
    classx = input5.get()
    time = datetime.now().strftime("%d/%m/%Y")
    x = sqlite3.connect("student.db")
    course = x.cursor()
    course.execute('''
    CREATE TABLE IF NOT EXISTS studient (
        studint TEXT,
        class TEXT,
        time DATETIME
    )
    ''')
    course.execute("INSERT INTO studient(studint,class ,time) VALUES (?, ?, ?)", (name, classx,time,))
    x.commit()
    x.close()

def show():
    search = input2.get()
    connect = sqlite3.connect("student.db")
    cursor = connect.cursor()
    cursor.execute(f"SELECT rowid,* FROM studient WHERE studint LIKE '%{search}%'")
    values = cursor.fetchall()
    show_tabels.config(text="")
    for i in values:
        show_tabels.config(text=f"{i[0]}	{i[1]}		{i[2]}	{i[3]}")
    connect.commit()
    connect.close()

def delete():
    delete_value = input3.get()
    connect = sqlite3.connect("student.db")
    cursor = connect.cursor()
    cursor.execute('DELETE FROM studient WHERE studint = ?', (delete_value,))
    connect.commit()
    connect.close()


#---------labels,buttons---------
#-------labels,bttons, entry----
label1 = tkinter.Label(windo, text="Write the student name:",font=("Helvetica", 25))
label1.place(x=50, y=50)
input1 = tkinter.Entry(windo, width=40)
input1.place(x=500,y=55)
button1 = tkinter.Button(windo, text="add", width=30,command=insert).place(x=100,y=100)
#--------------------------
label5 = tkinter.Label(windo, text="class",font=("Helvetica", 25))
label5.place(x=1000, y=30)
input5 = tkinter.Entry(windo, width=20)
input5.place(x=1000,y=60)
#-------------------------
input2 = tkinter.Entry(windo, width=30)
input2.place(x=100, y=250)
button2 = tkinter.Button(windo, text="shearch about student", width=30,command=show).place(x=100, y=300)
#-------------------------
lebel3 = tkinter.Label(windo, text="id	 studint	 class	 time	",font=("Helvetica", 20))
lebel3.place(x=600, y=100)
lebel3 = tkinter.Label(windo, text="=====	 =====	 =====	 =====	",font=("Helvetica", 20))
lebel3.place(x=600, y=130)
show_tabels = tkinter.Label(windo, text="",font=("Helvetica", 20))
show_tabels.place(x=600, y=160)
#-----------------
label4 = tkinter.Label(windo, text="Delete a stdent",font=("Helvetica", 15))
label4.place(x=100, y=400)
input3 = tkinter.Entry(windo, width=30)
input3.place(x=100, y=430)
button3 = tkinter.Button(windo, text="Delete", command=delete)
button3.place(x=100, y=460)
#----------------
windo.mainloop()

