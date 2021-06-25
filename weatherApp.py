import requests,json
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk ,Image

api_key = "2ab7d9bcfd04e3b729b3c625953c887c"

def weather():
    city=cit.get()
    if city=='':
        return messagebox.showerror('Error','Enter City Name')
    else:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        cityname = city
        complete_url = base_url + "appid=" + api_key + "&q=" + cityname 
        response = requests.get(complete_url) 
        x = response.json()  
        if x["cod"] != "404": 
  
            y = x["main"] 
            currenttemp = y["temp"] 
            currentpressure = y["pressure"] 
            currenthumidiy = y["humidity"]
            z = x["weather"] 
            weather_description = z[0]["description"]  
            Label(root,bg='#dfebe7',fg="#107358",text='Temperature: '+str(round(currenttemp-272.15))+' degree celsius').place(x=2,y=90)
            Label(root,bg='#dfebe7',fg="#3a49e8",text='Atmospheric Pressure: '+str(currentpressure)+' hPa').place(x=2,y=120)
            Label(root,bg='#dfebe7',fg='#8c9416',text='Humidity: '+str(currenthumidiy)+'%').place(x=2,y=150)
            Label(root,bg='#dfebe7',fg="#31ad15",text='Description: '+str(weather_description)).place(x=2,y=180)
        else: 
            return messagebox.showerror('Error','No City Found')
root= Tk()
root.geometry('400x400')
root['bg']='#dfebe7'
root.title('Real Time Weather Detection App 2.0 ')
cit=StringVar()
Label(root,bg='#dfebe7',text='Weather of your city',font='Helvetica 12 bold').grid(row=1,column=3)

Label(root,bg='#dfebe7',text='Enter City:',fg='red').grid(row=2,column=1)
Entry(root,bg='#51e8b2',fg="#6b1813",width=15,textvariable=cit,).grid(row=2,column=2)
Button(root,text='Proceed',bg="#9ef7f0",fg="#4a1ee8",activebackground='green',command=weather).grid(row=3,column=3)
img = ImageTk.PhotoImage(Image.open("umbrella.png"))
photo = Label(root,image=img)
photo.place(x=112,y=210)
root.mainloop()
