import tkinter as tk
from tkinter import font
import requests

#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
#607ae93f92e656457337f332062cbc6f

HEIGHT = 600
WIDTH = 600
root = tk.Tk()
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH,bg='#B9BFC0')
canvas.pack()


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str='City: %s \nCondtitions: %s \nTemprature (F): %s'%(name,desc,temp)

    except:

        final_str = 'Error !'


    return final_str


def getweather(city):

    weather_key='607ae93f92e656457337f332062cbc6f'
    url ='https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key,'q':city,'units':'imperial' }
    response = requests.get(url,params=params)
    weather = response.json()

    label['text'] = format_response(weather)




if __name__ == '__main__':

 frame = tk.Frame(root,bg='#2C5D69',bd=5)
 frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')
 entry=tk.Entry(frame,font=40)
 entry.place(relwidth=0.65,relheight=1)

 lower_frame=tk.Frame(root,bg='#2C5D69',bd=10)
 lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

 label=tk.Label(lower_frame,font=('Modren',30))
 label.place(relwidth=1,relheight=1)

 button = tk.Button(frame,text='Enter City',font=40,command=lambda : getweather(entry.get()))
 button.place(relx=0.7,relheight=1,relwidth=0.3)
 root.mainloop()

