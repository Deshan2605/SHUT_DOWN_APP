from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1") # 1 means it will shut down after 1 second

def restart_time():
    os.system("shutdown /r /t 20") # 20 means it will shut down after 20 seconds

def logout():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s /t 1")

st=Tk()
st.title("Shut Down App")
st.geometry("500x500")
st.config(bg="Black")

r_button=Button(st,text="Restart",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart) # relief is for change the properties when it get's hovered
r_button.place(x=180,y=60,height=50,width=150)

rt_button=Button(st,text="Restart Time",font=("Times New Roman",19,"bold"),relief=RAISED,cursor="plus",command=restart_time) # relief is for change the properties when it get's hovered
rt_button.place(x=180,y=170,height=50,width=150)

lg_button=Button(st,text="Log Out",font=("Times New Roman",19,"bold"),relief=RAISED,cursor="plus",command=logout) # relief is for change the properties when it get's hovered
lg_button.place(x=180,y=270,height=50,width=150)

st_button=Button(st,text="Shut Down",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown) # relief is for change the properties when it get's hovered
st_button.place(x=180,y=370,height=50,width=150)


st.mainloop()