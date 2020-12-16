import tkinter as tk
import tkinter.font as tkFont
from datetime import date, timedelta



# Root Container
cal = tk.Tk()
calFontStyle = tkFont.Font(family="Lucida Grande", size="16")
headerFontStyle = tkFont.Font(family="Lucida Grande", size="20")
header_frame = tk.Frame(cal)
body_frame = tk.Frame(cal)

#Global variables
current_month = 12
current_year = 2020
first_day = date(current_year,current_month,1)

# UI Properties
days = [("Sun",0),("Mon",1), ("Tue",2), ("Wed",3), ("Thu",4), ("Fri",5), ("Sat",6)]
nav_button_props = {"bg":"black","fg":"white","width":10,"height":3,"borderwidth":2,"relief":"raised","font":calFontStyle}
header_label_props = {"font":headerFontStyle,"fg":"red"}
month_label_props = {"bg":"gray","fg":"black","width":10,"height":3,"borderwidth":2,"relief":"ridge","font":calFontStyle}
day_button_props = {"bg":"yellow","fg":"black","width":10,"height":3,"borderwidth":2,"relief":"raised","font":calFontStyle}

def onClickPreviousMonth():
    global current_month, current_year, first_day, body_frame
    current_year -= 1
    if current_month == 0:
        current_month = 12
    first_day = date(current_year, current_month, 1)
    body_frame.grid_forget()
    draw_body()

def draw_header():
    global current_month, first_day, body_frame, header_frame
    prev_button = tk.Button(header_frame,text="<<",command=onClickPreviousMonth,**nav_button_props).grid(row=0,column=0)
    month_label = tk.Label(header_frame,text=first_day.strftime("%B"),**header_label_props).grid(row=0,column=1,columnspan=5)
    next_button = tk.Button(header_frame,text=">>",**nav_button_props).grid(row=0,column=6)
    for day,col in days:
        tk.Label(header_frame,text=day,**month_label_props).grid(row=1,column=col)

def draw_body():
    global current_month, first_day, body_frame, header_frame
    for i in range(0,33):
        current_day = first_day + timedelta(days=i)
        if current_day.month != current_month:
            break
        button_text = current_day.strftime("%d")
        row = int(current_day.strftime("%U")) - int(first_day.strftime("%W"))
        column = int(current_day.strftime("%w"))
        tk.Button(body_frame,text=button_text,**day_button_props).grid(column=column,row=row)
    header_frame.grid(row=0,column=0)
    body_frame.grid(row=1,column=0)


if __name__ == "__main__":
    cal.config(background="white")
    cal.title("CALENDAR")
    draw_header()
    draw_body()



    cal.mainloop()