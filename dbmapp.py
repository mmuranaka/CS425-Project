import tkinter
import mysql.connector
from tkinter import*
from tkinter import ttk


root = tkinter.Tk()
root.title('BANKING')
root.geometry("1000x300")

#main_frame = Frame(root)
#main_frame.pack(fill = BOTH, expand=1)

#my_canvas = Canvas(main_frame)
#my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

#scrolliewolie = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
#scrolliewolie.pack(side=RIGHT, fill=Y)

#my_canvas.configure(yscrollcommand=scrolliewolie.set)
#my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

#creates connection to db
conn = mysql.connector.connect(
    host = "127.0.0.1", 
    user = "root",
    passwd = "Tymczenko",
    database = "bankingDB"
)

c = conn.cursor()

#employee_id = Entry(root, width=30)
#employee_id.grid(row=0, column=1, padx=20)
#fname = Entry(root, width=30)
#fname.grid(row=1, column=1, padx=20)
#sname = Entry(root, width=30)
#sname.grid(row=2, column=1, padx=20)
#salary = Entry(root, width=30)
#salary.grid(row=3, column=1, padx=20)
#position = Entry(root, width=30)
#position.grid(row=4, column=1, padx=20)
#ssn = Entry(root, width=30)
#ssn.grid(row=5, column=1, padx=20)
#address_id = Entry(root, width = 30)
#address_id.grid(row=6, column=1, padx=20)
#branch_id = Entry(root, width = 30)
#branch_id.grid(row=7, column=1, padx=20)
#
#employee_id_label = Label(root, text = "Employee ID")
#employee_id_label.grid(row=0, column=0)
#fname_label = Label(root, text = "First Name")
#fname_label.grid(row=1, column=0)
#sname_label = Label(root, text = "Last Name")
#sname_label.grid(row=2, column=0)
#salary_label = Label(root, text = "Salary")
#salary_label.grid(row=3, column=0)
#position_label = Label(root, text = "Position")
#position_label.grid(row=4, column=0)
#ssn_label = Label(root, text = "SSN")
#ssn_label.grid(row=5, column=0)
#address_id_label = Label(root, text = "Address ID")
#address_id_label.grid(row=6, column=0)
#branch_id_label = Label(root, text = "Branch ID")
#branch_id_label.grid(row=7, column=0)

def query1():
    conn = mysql.connector.connect(host = "127.0.0.1", user = "root",passwd = "Tymczenko",database = "bankingDB")
    c = conn.cursor()
    c.execute("SELECT Count(*) as OPEN from account")
    rows = c.fetchall()
    conn.commit()
    output = ""
    for row in rows:
        output += str(row) + "\n"
    conn.close()
    newWindow = Toplevel(root)
    newWindow.title("Output")
    newWindow.geometry("500x200")
   
    query_label = tkinter.Label(newWindow, text = output).pack()
    
def query2():
    conn = mysql.connector.connect(host = "127.0.0.1", user = "root",passwd = "Tymczenko",database = "bankingDB")
    c = conn.cursor()
    c.execute("""Select fname, sname from customer 
                join address on customer.address_id=address.address_id 
                where address.state like 'UT'""")
    rows = c.fetchall()
    conn.commit()
    output = ""
    for row in rows:
        output += str(row) + "\n"
    conn.close()
    newWindow = Toplevel(root)
    newWindow.title("Output")
    newWindow.geometry("500x200")
   
    query_label = tkinter.Label(newWindow, text = output).pack()



    #query_label = tkinter.Label(root, text = output)
    #query_label.grid(column = 1, row = 1)
    
def query3():
    conn = mysql.connector.connect(host = "127.0.0.1", user = "root",passwd = "Tymczenko",database = "bankingDB")
    c = conn.cursor()
    c.execute("""Select count(*) as WORKERS 
              from final_employee 
              where branch_id = 778 
              group by branch_id""")
    rows = c.fetchall()
    conn.commit()
    output = ""
    for row in rows:
        output += str(row) + "\n"
    conn.close()
    newWindow = Toplevel(root)
    newWindow.title("Output")
    newWindow.geometry("500x200")

    query_label = tkinter.Label(newWindow, text = output).pack()
   
def query4():
    conn = mysql.connector.connect(host = "127.0.0.1", user = "root",passwd = "Tymczenko",database = "bankingDB")
    c = conn.cursor()
    c.execute("""SELECT account.account_num, account_type.type
                from account
                join customer on account.customer_id = customer.customer_id
                join account_type on account.type = account_type.type
                where customer.fname like 'Benjamin' AND customer.sname like 'Allen'""")
    rows = c.fetchall()
    conn.commit()
    output = ""
    for row in rows:
        output += str(row) + "\n"
    conn.close()
    newWindow = Toplevel(root)
    newWindow.title("Output")
    newWindow.geometry("500x200")
   
    query_label = tkinter.Label(newWindow, text = output).pack()

def query5():
    conn = mysql.connector.connect(host = "127.0.0.1", user = "root",passwd = "Tymczenko",database = "bankingDB")
    c = conn.cursor()
    c.execute("""SELECT account.account_name, transaction.amount
                from transaction
                join account on transaction.account_num = account.account_num
                where transaction.trans_type like 'Deposit' and amount<100
                order by transaction.amount DESC""")
    rows = c.fetchall()
    conn.commit()
    output = ""
    for row in rows:
        output += str(row) + "\n"
    conn.close()
    newWindow = Toplevel(root)
    newWindow.title("Output")
    newWindow.geometry("500x500")
    scroll_bar = tkinter.Scrollbar(newWindow)
    scroll_bar.pack(side = tkinter.RIGHT)
    query_label = tkinter.Label(newWindow, text = output).pack()

    

def query6():
    conn = mysql.connector.connect(host = "127.0.0.1", user = "root",passwd = "Tymczenko",database = "bankingDB")
    c = conn.cursor()
    c.execute("""SELECT *
                 from final_employee
                 order by salary DESC
                 limit 1""")
    rows = c.fetchall()
    conn.commit()
    output = ""
    for row in rows:
       output += str(row) + "\n"
    conn.close()
    newWindow = Toplevel(root)
    newWindow.title("Output")
    newWindow.geometry("500x200")
  
    query_label = tkinter.Label(newWindow, text = output).pack()
  

def query7():
    conn = mysql.connector.connect(host = "127.0.0.1", user = "root",passwd = "Tymczenko",database = "bankingDB")
    c = conn.cursor()
    c.execute("""Select address.street, count(*) as OCCURENCES
                from address
                group by street
                order by occurences desc
                limit 1""")
    rows = c.fetchall()
    conn.commit()
    output = ""
    for row in rows:
        output += str(row) + "\n"
    conn.close()
    newWindow = Toplevel(root)
    newWindow.title("Output")
    newWindow.geometry("500x200")
    
    query_label = tkinter.Label(newWindow, text = output).pack()
    
        
def query8():
    conn = mysql.connector.connect(host = "127.0.0.1", user = "root",passwd = "Tymczenko",database = "bankingDB")
    c = conn.cursor()
    c.execute("""SELECT address.state
                from address
                join branch on branch.address_id = address.address_id
                group by state
                order by count(*) desc
                limit 1""")
    rows = c.fetchall()
    conn.commit()
    output = ""
    for row in rows:
         output += str(row) + "\n"
    conn.close()
    newWindow = Toplevel(root)
    newWindow.title("Output")
    newWindow.geometry("500x200")
    
    query_label = tkinter.Label(newWindow, text = output).pack()
   
    
def query9():
    conn = mysql.connector.connect(host = "127.0.0.1", user = "root",passwd = "Tymczenko",database = "bankingDB")
    c = conn.cursor()
    c.execute("""SELECT account.balance
                from account
                join customer on customer.customer_id = account.customer_id
                where customer.fname like 'Maria' and customer.sname like 'Garcia' and account.type like 'money market'""")
    rows = c.fetchall()
    conn.commit()
    output = ""
    for row in rows:
       output += str(row) + "\n"
    conn.close()
    newWindow = Toplevel(root)
    newWindow.title("Output")
    newWindow.geometry("500x200")

    query_label = tkinter.Label(newWindow, text = output).pack()
    
    
def query10():
    conn = mysql.connector.connect(host = "127.0.0.1", user = "root",passwd = "Tymczenko",database = "bankingDB")
    c = conn.cursor()
    c.execute("""SELECT transaction.date 
                from transaction
                group by date
                order by count(*) desc
                limit 3""")
    rows = c.fetchall()
    conn.commit()
    output = ""
    for row in rows:
        output += str(row) + "\n"
    conn.close()
    newWindow = Toplevel(root)
    newWindow.title("Output")
    newWindow.geometry("500x200")
  
    query_label = tkinter.Label(newWindow, text = output).pack()
    


#query1
query1_button = tkinter.Button(root, 
                    text="Output the number of rows in the account relation. Call the result column OPEN",
                    command= query1)
query1_button.pack()

#query2
query2_button = tkinter.Button(root, 
                    text="Output the first and last name of the customers' whopse address resides in the state of Utah",
                    command= query2)
query2_button.pack()

#query3
query3_button = tkinter.Button(root, 
                    text="Output the amount of workers at branch_id 778 and call the resulting WORKERS",
                    command= query3)
query3_button.pack()

#query4
query4_button = tkinter.Button(root, 
                    text="Output the account number and corresponding account type for account's owned by customers named Benjamin Allen",
                    command= query4)
query4_button.pack()

#query5
query5_button = tkinter.Button(root, 
                    text="Output the account name for deposit transactions less than $100 and the amount is decreasing order",
                    command= query5)
query5_button.pack()

#query6
query6_button = tkinter.Button(root, 
                    text="Output the row for the highest earning employee in the banking database",
                    command= query6)
query6_button.pack()

#query7
query7_button = tkinter.Button(root, 
                    text="Output the most popular street name in  the database and the amount of occurences of that street name, labeling that column as OCCURRENCES",
                    command= query7)
query7_button.pack()

#query8
query8_button = tkinter.Button(root, 
                    text="Output the state with the most branches in the database",
                    command= query8)
query8_button.pack()

#query9
query9_button = tkinter.Button(root, 
                    text="Output the balance of Maria Garcia's money market account",
                    command= query9)
query9_button.pack()

#query10
query10_button = tkinter.Button(root, 
                    text="Output the 3 most common transaction dates",
                    command= query10)
query10_button.pack()






root.mainloop()