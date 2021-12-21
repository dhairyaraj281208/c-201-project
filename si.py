from tkinter import *
window=Tk()

# add widgets here


window.title('SI Calculator')
window.geometry("380x400")
window.configure(bg='green')

#function for button
   
def calculate_si():
    p = int(principal_entry.get())
    r = int(rate_entry.get())
    t = int(time_entry.get())
    si = p*r*t/100
    
    result_label.destroy()

    msg=""
    
    
    output_message=Label(result_frame,text="SI is "+str(si), bg = "lightgreen", font=("Calibri", 12), width=42)
    output_message.place(x=20,y=40)
    output_message.pack()

app_label=Label(window, text="SI CALCULATOR", fg = "black", bg = "lightgreen", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)


principal_label=Label(window, text="Enter Principal (₹)", fg = "black", bg = "lightgreen", font=("Calibri", 12))
principal_label.place(x=20, y=140)

principal_entry=Entry(window, text="", bd=2, width=15)
principal_entry.place(x=150, y=142)

time_label=Label(window, text="Enter Time", fg = "black", bg = "lightgreen", font=("Calibri", 12))
time_label.place(x=20, y=185)

time_entry=Entry(window, text="", bd=2, width=15)
time_entry.place(x=150, y=187)

rate_label=Label(window, text="Enter Rate (%)", fg = "black", bg = "lightgreen", font=("Calibri", 12))
rate_label.place(x=20, y=210)

rate_entry=Entry(window, text="", bd=2, width=15)
rate_entry.place(x=150, y=212)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "cyan",bd=4,command=calculate_si)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "lightgreen", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightgreen", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()


window.mainloop()