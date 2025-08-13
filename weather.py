from tkinter import *
import tkinter as tk
import pytz
from geopy.geocoders import Nominatim
from datetime import datetime,timedelta
import requests
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from tkinter import Tk,Label
from timezonefinder import TimezoneFinder
from tkinter import Tk, PhotoImage


def getweather():
  #long_let = Label(root,text="")
  #clock = Label(root,text = "")

  city= textfield.get()
  geolocator = Nominatim(user_agent="new")
  location = geolocator.geocode(city)
  obj=TimezoneFinder()
  result = obj.timezone_at(lat=location.latitude, lng=location.longitude)
  timezone.config(text=result)

  long_let.config(text=f"{round(location.latitude,4)}°N{round(location.longitude,4)}°E")
  home = pytz.timezone(result)
  local_time =datetime.now(home)
  current_time = local_time.strftime("%I:%M %p")
  clock.config(text=current_time)

  api_key = "acdae9378ee6487f33dd1dabfa51cd72"
  api = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
  json_data = requests.get(api).json()
  print(json_data)

  #current wheather from first forecast
  current = json_data['list'][0]
  temp = current['main']['temp']
  humidity = current['main']['humidity']
  pressure = current['main']['pressure']
  wind_speed= current['wind']['speed']
  description = current['weather'][0]['description']  
  
  t.config(text=f"{temp}°C")
  h.config(text=f"{humidity}%")
  p.config(text=f"{pressure}hPa")
  w.config(text=f"{wind_speed}m/s")
  d.config(text=f"{description}")

  #Daily forecast - pick 12 : 00 PM entries
  daily_data= []
  for entry in json_data['list'] : 
    if "12:00:00" in entry['dt_txt']:
      daily_data.append(entry)

  icons = []
  temps = []

  for i in range(5):
    if i >= len(daily_data):
      break
    icon_code = daily_data[i]['weather'][0]['icon']
    img = Image.open(f"icon/{icon_code}.jpeg").resize((50,50))
    icons.append(ImageTk.PhotoImage(img))
    temps.append((daily_data[i]['main']['temp_max'],daily_data[i]['main']['feels_like']))

  day_widget = {
    (firatimg,day1,day1temp),
    (second_img,day2,day2temp),
    (third_img,day3,day3temp),
    (four_img,day4,day4temp),
    (five_img,day5,day5temp),
  }

  for i,(img_label,day_label,temp_label) in enumerate(day_widget):
    if i >= len(icons):
      break
    img_label.config(image = icons[i])
    img_label.image = icons[i]
    temp_label.config(text=f"Day : {temps[i][0]}\nNight : {temps[i][1]}")
    future_date = datetime.now() + timedelta(days = i) 
    day_label.config(text=future_date.strftime("%A"))


root = Tk()
root.title("My Weather")
root.geometry("750x470+300+250")
root.resizable(False,False)
#root.state('zoomed')
root.config(bg="#202731")


##icon  
img = Image.open("18.jpg")
logo = ImageTk.PhotoImage(img,root) 
root.iconphoto(False, logo)

r_b = Image.open("17.jpeg ")
Round_box = ImageTk.PhotoImage(r_b)
Label(root,image=Round_box,bg="#202731").place(x=30,y=60)

#label
label1 = Label(root,text= "Tempreature",font=("Helvetica",11),fg="#323661",bg="#aad1c8")
label1.place(x=50,y=120)

label2 = Label(root,text= "Humidity",font=("Helvetica",11),fg="#323661",bg="#aad1c8")
label2.place(x=50,y=140)

label3 = Label(root,text= "Pressure",font=("Helvetica",11),fg="#323661",bg="#aad1c8")
label3.place(x=50,y=160)

label4 = Label(root,text= "Wind Speed",font=("Helvetica",11),fg="#323661",bg="#aad1c8")
label4.place(x=50,y=180)

label5 = Label(root,text= "Description",font=("Helvetica",11),fg="#323661",bg="#aad1c8")
label5.place(x=50,y=200)


#Search bar
search_img=Image.open("14.jpeg")
myimage = ImageTk.PhotoImage(search_img)
Label(root,image=myimage,bg="#202731").place(x=270,y=122)

weat_img=Image.open("19.jpeg")

weat= ImageTk.PhotoImage(weat_img)
Label(root,image=weat,bg="#333c4c").place(x=290,y=127)

textfield=tk.Entry(root,justify="center",width=15,font=("poppins",25,"bold"),bg="#333c4c",border=0,fg="white")
textfield.place(x=370,y=130)

search_icon=Image.open("20.jpeg")

s_i= ImageTk.PhotoImage(search_icon)
myimage_icon=Button(root,image=s_i,borderwidth=0,cursor="hand2",bg="#333c4c",command=getweather).place(x=640,y=135)


#bottom box
frame=Frame(root,height=180,width=900,bg="#7094d4")
frame.pack(side=BOTTOM)

#boxes
first_box=Image.open("15.jpeg")
f_b= ImageTk.PhotoImage(first_box)
second_box=Image.open("16.jpeg")
s_b= ImageTk.PhotoImage(second_box)

Label(frame,image=f_b,bg="#7094d4").place(x=30,y=20)
Label(frame,image=s_b,bg="#7094d4").place(x=300,y=30)
Label(frame,image=s_b,bg="#7094d4").place(x=400,y=30)
Label(frame,image=s_b,bg="#7094d4").place(x=500,y=30)
Label(frame,image=s_b,bg="#7094d4").place(x=600,y=30)


#clock
clock=Label(root,font=("Helvetica",20),bg="#202731",fg="white")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20),bg="#202731",fg="white")
timezone.place(x=500,y=20)

long_let=Label(root,font=("Helvetica",10),bg="#202731",fg="white")
long_let.place(x=500,y=50)


#thpwd
t=Label(root,font=("Helvetica",9),bg="#333c4c",fg="white")
t.place(x=150,y=120)
h=Label(root,font=("Helvetica",9),bg="#333c4c",fg="white")
h.place(x=150,y=140)
p=Label(root,font=("Helvetica",9),bg="#333c4c",fg="white")
p.place(x=150,y=160)
w=Label(root,font=("Helvetica",9),bg="#333c4c",fg="white")
w.place(x=150,y=180)
d=Label(root,font=("Helvetica",9),bg="#333c4c",fg="white")
d.place(x=150,y=200)


#first cell
firstframe=Frame(root,width=230,height=132,bg="#323661")
firstframe.place(x=35,y=315)

firatimg=Label(firstframe,bg="#323661")
firatimg.place(x=1,y=15)

day1=Label(firstframe,font=("arial 20"),bg="#323661",fg="white")
day1.place(x=100,y=5)

day1temp=Label(firstframe,font=("arial 15 bold"),bg="#323661",fg="white")
day1temp.place(x=100,y=50)

#second cell
secondframe=Frame(root,width=70,height=115,bg="#eeefea")
secondframe.place(x=305,y=325)

second_img=Label(secondframe,bg="#eeefea",fg="#000")
second_img.place(x=7,y=20)

day2=Label(secondframe,bg="#eeefea",fg="#000")
day2.place(x=10,y=5)

day2temp=Label(secondframe,bg="#eeefea",fg="#000")
day2temp.place(x=2,y=70)

#third cell
thirdframe=Frame(root,width=70,height=115,bg="#eeefea")
thirdframe.place(x=405,y=325)

third_img=Label(thirdframe,bg="#eeefea",fg="#000")
third_img.place(x=7,y=20)

day3=Label(thirdframe,bg="#eeefea",fg="#000")
day3.place(x=10,y=5)

day3temp=Label(thirdframe,bg="#eeefea",fg="#000")
day3temp.place(x=2,y=70)

#fourth cell
fourframe=Frame(root,width=70,height=115,bg="#eeefea")
fourframe.place(x=505,y=325)

four_img=Label(fourframe,bg="#eeefea",fg="#000")
four_img.place(x=7,y=20)

day4=Label(fourframe,bg="#eeefea",fg="#000")
day4.place(x=10,y=5)

day4temp=Label(fourframe,bg="#eeefea",fg="#000")
day4temp.place(x=2,y=70)

#fifth cell
fiveframe=Frame(root,width=70,height=115,bg="#eeefea")
fiveframe.place(x=605,y=325)

five_img=Label(fiveframe,bg="#eeefea",fg="#000")
five_img.place(x=7,y=20)

day5=Label(fiveframe,bg="#eeefea",fg="#000")
day5.place(x=10,y=5)

day5temp=Label(fiveframe,bg="#eeefea",fg="#000")
day5temp.place(x=2,y=70)

root.mainloop() 
