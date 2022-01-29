# this is the code for scrabble club system
import tkinter
import mysql.connector
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox

root = Tk()
root.geometry("600x400")
root.title("Scrabble Club")

# function for inserting new player to the club
def insert():
    first_name = e_first.get()
    last_name = e_last.get()
    phone = e_number.get()
    mail = e_mail.get()
    id1 = e_id.get()
    try:
        if first_name == "" or last_name == "" or phone == "" or mail == "" or id1 == "":
            messagebox.showinfo("Create status", "All fields are required")
        else:
            con = mysql.connector.connect(host="localhost",user="root",passwd="ATG99iTP@",database="scrabble")
            cursor = con.cursor()
            cursor.execute(
                "INSERT INTO player_details VALUES('" + id1 + "','" + first_name + "','" + last_name + "','" + phone + "','" + mail + "')")
            cursor.execute("commit")

            e_first.delete(0, 'end')
            e_last.delete(0, 'end')
            e_number.delete(0, 'end')
            e_mail.delete(0, 'end')
            e_id.delete(0, 'end')
            messagebox.showinfo("Create status", "Created successfully")

    except Exception as e:
        print(e)
        messagebox.showinfo("Create status", "Details Invalid or Player id already exists")
        con.rollback()
        con.close()

def update(): #function for updating player
    first_name = e_first.get()
    last_name = e_last.get()
    phone = e_number.get()
    mail = e_mail.get()
    id1 = e_id.get()
    try:
        if first_name == "" or last_name == "" or phone == "" or mail == "" or id1 == "":
            messagebox.showinfo("Update status", "All fields are required")
        else:
            con = mysql.connector.connect(host="localhost",user="root",passwd="ATG99iTP@",database="scrabble")
            cursor = con.cursor()
            cursor.execute(
            "UPDATE player_details SET first_name='" + first_name + "',last_name='" + last_name + "',phone_no='" + phone + "',email_id='" + mail + "' where mem_id='" + id1 + "'")
            cursor.execute("commit")

            e_first.delete(0, 'end')
            e_last.delete(0, 'end')
            e_number.delete(0, 'end')
            e_mail.delete(0, 'end')
            e_id.delete(0, 'end')
            messagebox.showinfo("Update status", "updated successfully")

    except Exception as e:
        print(e)
        messagebox.showinfo("Create status", "Details Invalid")
        con.rollback()
        con.close()

first_name = Label(root, text="First Name", font=('bold', 10))
first_name.place(x=20, y=30)
e_first = Entry()
e_first.place(x=150, y=30)

last_name = Label(root, text="Last Name", font=('bold', 10))
last_name.place(x=20, y=60)
e_last = Entry()
e_last.place(x=150, y=60)

number = Label(root, text="Phone number", font=('bold', 10))
number.place(x=20, y=90)
e_number = Entry()
e_number.place(x=150, y=90)

email_id = Label(root, text="Email ID", font=('bold', 10))
email_id.place(x=20, y=120)
e_mail = Entry()
e_mail.place(x=150, y=120)

player_id = Label(root, text="Player ID", font=('bold', 10))
player_id.place(x=20, y=150)
e_id = Entry()
e_id.place(x=150, y=150)

insert = Button(root, text="Create", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=200)
update = Button(root, text="Update", font=("italic", 10), bg="white", command=update)
update.place(x=100, y=200)

# for players profile screen
mydb=mysql.connector.connect(host="localhost",user="root",passwd="ATG99iTP@",database="scrabble")
cursor=mydb.cursor()

options=[]
sql="SELECT mem_id,first_name,last_name FROM player_details"
cursor.execute(sql)
ids=cursor.fetchall()
for i in ids:
    options.append(str(i[0])+"-"+i[1]+"-"+i[2])
def lookupPlayer(event):
    var=mycombo.get()
    pid=var.split("-")[0]
    pid1=var.split("-")[1]
    pid2= var.split("-")[2]
    query=("""
            SELECT *
            FROM(WITH cte AS(
            SELECT player, SUM(Win) AS Won, SUM(Loss) AS Lost, SUM(score) AS Score
            FROM
            ( SELECT player1 AS player, 
                CASE WHEN player1_score > player2_score THEN 1 ELSE 0 END AS Win, 
                CASE WHEN player1_score < player2_score THEN 1 ELSE 0 END AS Loss, player1_score AS score
            FROM score_details
            UNION ALL
            SELECT player2 AS player,
                CASE WHEN player2_score > player1_score THEN 1 ELSE 0 END AS Win, 
                CASE WHEN player2_score < player1_score THEN 1 ELSE 0 END AS Loss, player2_score AS score
            FROM score_details
            ) t
            GROUP BY player
            ORDER By Won, Lost DESC, Score)
            SELECT player_details.first_name,player_details.last_name,cte.Won,cte.lost 
            FROM player_details
            INNER JOIN cte
            ON player_details.mem_id=cte.player
            where player=%s)A
            CROSS JOIN (WITH cte1 AS(
                        SELECT max(player1_score) AS Heighest,game_id,player2 FROM score_details
                        WHERE player1=%s
                        GROUP BY game_id,player2
                        UNION ALL
                        SELECT max(player2_score) AS Heighest,game_id,player1 FROM score_details
                        WHERE player2=%s
                        GROUP BY game_id,player1)
                        SELECT cte1.Heighest,player_details.first_name AS Against,game_details.game_date,game_details.game_place
                        FROM game_details
                        INNER JOIN cte1
                        ON game_details.game_id=cte1.game_id
                        INNER JOIN player_details ON cte1.player2=player_details.mem_id
                        WHERE heighest=  ( SELECT Max(Heighest) FROM cte1 ))B
                        CROSS JOIN  (WITH cte2 AS(
                                    SELECT avg(player1_score) AS AVERAGE FROM score_details
                                    WHERE player1=%s
                                    UNION ALL
                                    SELECT avg(player2_score) AS Average FROM score_details
                                    WHERE player2=%s)
                                    SELECT TRUNCATE(avg(average),0) AS Average FROM cte2)C""")
    cursor.execute(query,(pid[0],pid[0],pid[0],pid[0],pid[0]))
    rows=cursor.fetchall()
    pfirst.set(pid1)
    plast.set(pid2)
    pwon.set(0)
    plost.set(0)
    phigh.set(0)
    pvs.set('')
    pgame.set('')
    pdate.set('')
    pavg.set(0)
    for i in rows:
        plast.set(i[1])
        pwon.set(i[2])
        plost.set(i[3])
        phigh.set(i[4])
        pvs.set(i[5])
        pgame.set(i[6])
        pdate.set(i[7])
        pavg.set(i[8])


opts=StringVar()
pfirst=StringVar()
plast=StringVar()
pwon=IntVar()
plost=IntVar()
phigh=IntVar()
pvs=StringVar()
pgame=StringVar()
pdate=StringVar()
pavg=IntVar()
wrapper=LabelFrame(root,text="Player Lookup")
wrapper2=LabelFrame(root,text="Player Details")
wrapper.pack(padx=400,pady=30,fill="both")
wrapper2.pack(padx=400,pady=30,fill="both")

Label(wrapper,text="Select Player").grid(padx=50,pady=0)
mycombo=ttk.Combobox(wrapper,textvariable=opts)
mycombo['values']=options
mycombo.grid(row=0,column=1,padx=50,pady=30)
mycombo.current(0)
mycombo.bind("<<ComboboxSelected>>",lookupPlayer)



lbl1=Label(wrapper2,text="First Name")
lbl1.grid(row=0,column=0,padx=10,pady=10)
entl = Entry(wrapper2,textvariable=pfirst,state='readonly')
entl.grid(row=0, column=1, padx=10, pady=10)

lbl2=Label(wrapper2,text="Last Name")
lbl2.grid(row=1,column=0,padx=10,pady=10)
ent2 = Entry(wrapper2,textvariable=plast,state='readonly')
ent2.grid(row=1, column=1, padx=10, pady=10)

lbl3=Label(wrapper2,text="Games Won")
lbl3.grid(row=2,column=0,padx=10,pady=10)
ent3 = Entry(wrapper2,textvariable=pwon,state='readonly')
ent3.grid(row=2, column=1, padx=10, pady=10)

lbl4=Label(wrapper2,text="Games Lost")
lbl4.grid(row=3,column=0,padx=10,pady=10)
ent4 = Entry(wrapper2,textvariable=plost,state='readonly')
ent4.grid(row=3, column=1, padx=10, pady=10)

lbl5=Label(wrapper2,text="Heighest Score")
lbl5.grid(row=4,column=0,padx=10,pady=10)
ent5 = Entry(wrapper2,textvariable=phigh,state='readonly')
ent5.grid(row=4, column=1, padx=10, pady=10)

lbl6=Label(wrapper2,text="Against")
lbl6.grid(row=5,column=0,padx=10,pady=10)
ent6 = Entry(wrapper2,textvariable=pvs,state='readonly')
ent6.grid(row=5, column=1, padx=10, pady=10)

lbl7=Label(wrapper2,text="Game Date")
lbl7.grid(row=6,column=0,padx=10,pady=10)
ent7 = Entry(wrapper2,textvariable=pgame,state='readonly')
ent7.grid(row=6, column=1, padx=10, pady=10)

lbl8=Label(wrapper2,text="Game place")
lbl8.grid(row=7,column=0,padx=10,pady=10)
ent8 = Entry(wrapper2,textvariable=pdate,state='readonly')
ent8.grid(row=7, column=1, padx=10, pady=10)

lbl9=Label(wrapper2,text="Average Score")
lbl9.grid(row=8,column=0,padx=10,pady=10)
ent9 = Entry(wrapper2,textvariable=pavg,state='readonly')
ent9.grid(row=8, column=1, padx=10, pady=10)




# for leader board
mydb1=mysql.connector.connect(host="localhost",user="root",passwd="ATG99iTP@",database="scrabble")
cursor1=mydb1.cursor()
query1=("""
        SELECT *
        FROM (WITH cte AS
        (SELECT COUNT(player1) AS Numberofgames,player1 AS player FROM score_details
        WHERE player1=%s
        UNION ALL
        SELECT COUNT(player2) AS Numberofgames,player2 AS player FROM score_details
        WHERE player2=%s)
        SELECT player_details.first_name,player_details.last_name,SUM(Numberofgames)
        FROM cte,player_details WHERE player_details.mem_id=cte.player 
        GROUP BY player)A
        CROSS JOIN (SELECT TRUNCATE((AVG(player1_score)+AVG(player1_score))/2,0) AS average FROM
                    (SELECT player1_score FROM score_details WHERE player1=2 ORDER BY player1_score DESC)A
                        CROSS JOIN (SELECT player2_score FROM score_details WHERE player2=%s ORDER BY player1_score DESC limit 10)B)C""")
cursor1.execute(query1,(1,1,1))
rows=cursor1.fetchall()

frm=Frame(root)
frm.pack(side=tkinter.BOTTOM,padx=20,expand="yes")
tv=ttk.Treeview(frm,columns=(1,2,3,4),show="headings",height=4)
lblt=Label(root,text="LEADER BOARD",padx=80)
lblt.pack(expand="no")
tv.pack()
tv.heading(1,text="First Name")
tv.heading(2,text="Last Name")
tv.heading(3,text="Games Played")
tv.heading(4,text="Average Score")

for i in rows:
    tv.insert('','end',values=i)
root.attributes('-fullscreen', True)
mydb1.close()
root.mainloop()

