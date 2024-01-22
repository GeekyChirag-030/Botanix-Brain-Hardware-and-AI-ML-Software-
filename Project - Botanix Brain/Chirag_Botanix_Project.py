# def arduino():
    
#     # Read one line of sensor data from serial port
#     sensor_data = ser.readline().decode().strip()
#     # Split the sensor data into 5 fields using comma as delimiter
#     sensor_fields = sensor_data.split(',')
#     Global=sensor_fields

#     return Global

# # Open serial port to communicate with Arduino
# ser = serial.Serial('COM6', 9600)
# Li=arduino()
# print(Li)
# ser.close()


import tkinter
from tkinter import *  ##used for gui window
import customtkinter
from PIL import Image,ImageTk  #used for main location img
from pathlib import Path
from tkinter import Tk, Canvas, Entry,Text, Button, PhotoImage
from plotly.graph_objects import *
from plotly.subplots import *
from tkinter import *
from plotly.io import *
#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

from pathlib import Path
import pandas as pd
from PIL import Image,ImageTk
from tkinter import NW, Tk, Canvas, Entry, Text, Button, PhotoImage

#import serial
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

root = Tk()

Temperature = None
Humidity = None
Sun = None
Air_Moisture = None
Air_Quality = None

root.geometry('600x375')
root.title("Botanix Brain | Welcome")
root.config(bg="#fff")
root.resizable(False, False)

# def arduino():
    
#     # Read one line of sensor data from serial port
#     sensor_data = ser.readline().decode().strip()
#     # Split the sensor data into 5 fields using comma as delimiter
#     sensor_fields = sensor_data.split(',')
#     Global=sensor_fields

#     return Global

# # Open serial port to communicate with Arduino
# ser = serial.Serial('COM6', 9600)
# Li=arduino()
# print(Li)
# ser.close()

#----------------------------------------------destroying 2nd window and creating nextwindow-----------------------------------------
def destroy():
    window.destroy()

# ----------------------------------------------2nd interface-----------------------------------------------------------

def win():
    global window                    #Basically Make the Varibles Global So , We cAn Access There All Globally From Outside This Function Also                          
    global entry_1                  # Basically Make the Varibles Global So , We cAn Access There All Globally From Outside This Function Also 
    global entry_2                  # Basically Make the Varibles Global So , We cAn Access There All Globally From Outside This Function Also 
    global entry_3                  # Basically Make the Varibles Global So , We cAn Access There All Globally From Outside This Function Also 
    global entry_4                  # Basically Make the Varibles Global So , We cAn Access There All Globally From Outside This Function Also 
    global entry_5                  # Basically Make the Varibles Global So , We cAn Access There All Globally From Outside This Function Also 
     
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(
        r"D:\\Project Botanix Brain\\sci_city_project\\build\\assets\\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # global root
    
    Sec_Path = "D:\\Project Botanix Brain\\sci_city_project\\build\\assets\\frame0\\"
    root.destroy()
    window = Tk()
    window.title("Botanix Brain | Details")
    window.geometry("610x379")
    window.configure(bg="#FFFFFF")
    canvas = Canvas(window, bg="#FFFFFF", height=379, width=610, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    canvas.create_rectangle(10.0, 4.0, 610.0, 379.0, fill="#FFFFFF", outline="")

    canvas.create_rectangle(15.0, 6.0, 603.0, 91.0, fill="#D9FFDA", outline="")

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(82.0, 46.0, image=image_image_1)

    canvas.create_rectangle(147.0, 98.0, 603.0, 375.0, fill="#D9FFDA", outline="")

    canvas.create_text(165.0, 112.0, anchor="nw", text="Temperature:-", fill="#000000", font=("Inter", 14 * -1))

    canvas.create_text(
        165.0,
        174.0,
        anchor="nw",
        text="Sunlight:-",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    canvas.create_text(
        421.0,
        174.0,
        anchor="nw",
        text="Moisture:-",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    canvas.create_text(
        165.0,
        236.0,
        anchor="nw",
        text="Air Quality:-",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    canvas.create_text(
        421.0,
        112.0,
        anchor="nw",
        text="Humidity:-",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    entry_image_1 = PhotoImage(file=relative_to_assets(
        Sec_Path + "entry_1.png"))
    entry_bg_1 = canvas.create_image(241.0, 151.5, image=entry_image_1)
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0)
    
    entry_1.place(
        x=174.0,
        y=141.0,
        width=134.0,
        height=19.0
    )

    entry_image_2 = PhotoImage(file=relative_to_assets(
        Sec_Path + "entry_2.png"))
    
    entry_bg_2 = canvas.create_image(496.0, 151.5, image=entry_image_2)
    entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    
    
    entry_2.place(x=429.0, y=141.0, width=134.0, height=19.0)

    
    entry_image_3 = PhotoImage(file=relative_to_assets(
        Sec_Path + "entry_3.png"))
    
    entry_bg_3 = canvas.create_image(241.0, 213.5, image=entry_image_3)
    entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    
    entry_3.place(x=174.0, y=203.0, width=134.0, height=19.0)


    entry_image_4 = PhotoImage(file=relative_to_assets(
        Sec_Path + "entry_4.png"))
    entry_bg_4 = canvas.create_image(496.0, 209.5, image=entry_image_4)
    entry_4 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    
    entry_4.place(x=429.0, y=199.0, width=134.0, height=19.0)

    
    
    entry_image_5 = PhotoImage(file=relative_to_assets(
        Sec_Path + "entry_5.png"))
    
    entry_bg_5 = canvas.create_image(241.0, 275.5, image=entry_image_5)
    entry_5 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    
    entry_5.place(x=174.0, y=265.0, width=134.0, height=19.0)

    button_image_1 = PhotoImage(file=relative_to_assets(
        Sec_Path + "button_1.png"))
    
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, relief="flat", command=chrag)
    button_1.place(x=489.0, y=326.0, width=97.0, height=29.0)

    canvas.create_text(166.0, 289.0, anchor="nw", text="\nNote for Sunlight:(As descreate value either 0 or 1)", fill="#808080",
                       font=("Inter", 12 * -1))

    canvas.create_text(200.0, 310.0, anchor="nw", text="\n(0=shady, 1=sunny)", fill="#808080", font=("Inter", 12 * -1))
    canvas.create_rectangle(14.0, 98.0, 142.0, 375.0, fill="#D9FFDA", outline="")
    canvas.create_text(33.0, 324.0, anchor="nw", text="Make sure the \n\n", fill="#808080", font=("Inter", 11 * -1))
    canvas.create_text(453.0, 48.0, anchor="nw", text="DATA READINGS", fill="#000000",
                       font=("JostRoman Regular", 16 * -1))
    canvas.create_text(40.0, 338.0, anchor="nw", text="sensors are ", fill="#808080", font=("Inter", 11 * -1))

    canvas.create_text(14.0, 353.0, anchor="nw", text="     placed correctly.", fill="#808080", font=("Inter", 11 * -1))
    window.resizable(False, False)
    window.mainloop()

    
#---------------------------------------------chirag window-----------------------------------------------------------------------

def chrag():
    global Temperature                      #Make The Outside Function's Varible , Global , Which Menas Any Chnages Done To This Varible Will Becomes Globally                 
    global Humidity                 #Make The Outside Function's Varible , Global , Which Menas Any Chnages Done To This Varible Will Becomes Globally 
    global Sun                 #Make The Outside Function's Varible , Global , Which Menas Any Chnages Done To This Varible Will Becomes Globally 
    global Air_Moisture                 #Make The Outside Function's Varible , Global , Which Menas Any Chnages Done To This Varible Will Becomes Globally 
    global Air_Quality                 #Make The Outside Function's Varible , Global , Which Menas Any Chnages Done To This Varible Will Becomes Globally 
    
    
    Temperature = int(entry_1.get())            # Taking Direct Acess of Value of Entry Widget , Rather then Using Textvarible Attribute of Entry Widget      
    Humidity = int(entry_2.get())        # Taking Direct Acess of Value of Entry Widget , Rather then Using Text Varible Attribute of Entry Widget 
    Sun = int(entry_3.get())        # Taking Direct Acess of Value of Entry Widget , Rather then Using Text Varible Attribute of Entry Widget 
    Air_Moisture = int(entry_4.get())           # Taking Direct Acess of Value of Entry Widget , Rather then Using Text Varible Attribute of Entry Widget                        
    Air_Quality = int(entry_5.get())        # Taking Direct Acess of Value of Entry Widget , Rather then Using Text Varible Attribute of Entry Widget 

    Levels = ["Moderate", "Less Unhealthy", "Unhealthy", "V_UH"]
    print("\n\n Function Started Values Have: Temp {} , Humidity {} , Sun {} , Air_Moisture {},Air Quality{}".format(Temperature,Humidity,Sun,Air_Moisture,Air_Quality))

    if Sun == 0:
        Sun = 0 + 50
    elif Sun == 1:
        Sun *= 100

    Fig = make_subplots(rows=2, cols=3, specs=[[{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}],
                                               [{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}]])

    Fig.add_trace(Indicator(
        mode="gauge+number+delta",

        delta={'reference': 100, 'increasing': {'color': "red"}, 'decreasing': {'color': 'limegreen'}},
        value=Air_Quality
        , title={'text': 'Air Quality', 'font': {'size': 35}, 'align': 'center'}

        , gauge={'axis': {'range': [0, 500], "tickmode": "array",
                          "tickvals": ['50', '100', '150', '200', '300', '500'],
                          "ticktext": ["Good" if i == 0 else "Hazardous" if i == 5 else Levels[i - 1] for i in range(6)],
                          'tickfont': {'size': 16}, 'tickwidth': 2, 'tickangle': 0},

                 'steps': [{'range': [0, 50], 'color': 'lightgreen'},
                           {'range': [50, 100], 'color': 'yellow'}
                     , {'range': [100, 150], 'color': 'orange'},
                           {'range': [150, 200], 'color': 'red'},
                           {'range': [200, 300], 'color': 'blueviolet'},
                           {'range': [300, 500], 'color': 'purple'}],

                 'bar': {
                     'color': 'darkgreen',
                     'thickness': 0.6},

                 'threshold': {
                     'line': {'color': 'red', 'width': 8},
                     'thickness': 0.7,
                     'value': 499},

                 'borderwidth': 2, 'bordercolor': 'black'}
    ), row=1, col=1)

    Fig.add_trace(Indicator(
        mode="gauge+number+delta",

        value=Sun
        , title={'text': 'Sunlight', 'font': {'size': 35}, 'align': 'center'}

        , gauge={'axis': {'range': [0, 100], "tickmode": "array",
                          "tickvals": ['50', '100'],
                          "ticktext": ["Shaddy" if i == 0 else "Sunny" for i in range(2)],
                          'tickfont': {'size': 16}, 'tickwidth': 2, 'tickangle': 0},

                 'steps': [{'range': [0, 50], 'color': 'yellow'},
                           {'range': [50, 100], 'color': 'orange'}],

                 'bar': {
                     'color': 'darkgreen',
                     'thickness': 0.6},

                 'threshold': {
                     'line': {'color': 'green', 'width': 8},
                     'thickness': 0.7,
                     'value': 99},

                 'borderwidth': 2, 'bordercolor': 'black'}
    ), row=2, col=2)

    Fig.add_trace(Indicator(
        mode="gauge+number+delta",

        delta={'reference': 40, 'increasing': {'color': "red"}, 'decreasing': {'color': 'limegreen'}},
        value=Temperature
        , title={'text': 'Temperature', 'font': {'size': 35}, 'align': 'center'}

        , gauge={'axis': {'range': [0, 60], "tickmode": "array",
                          "tickvals": ['0', '10', '20', '30', '40', '50', '60'],

                          'tickfont': {'size': 16}, 'tickwidth': 2, 'tickangle': 0},

                 'steps': [{'range': [0, 10], 'color': 'lightgreen'},
                           {'range': [10, 20], 'color': 'yellow'},
                           {'range': [20, 30], 'color': 'orange'},
                           {'range': [30, 40], 'color': 'red'},
                           {'range': [40, 50], 'color': 'blueviolet'},
                           {'range': [50, 60], 'color': 'purple'}],

                 'bar': {
                     'color': 'darkgreen',
                     'thickness': 0.6},

                 'threshold': {
                     'line': {'color': 'red', 'width': 8},
                     'thickness': 0.7,
                     'value': 59},

                 'borderwidth': 2, 'bordercolor': 'black'}
    ), row=1, col=3)

    Fig.add_trace(Indicator(
        mode="gauge+number+delta",

        delta={'reference': 30, 'increasing': {'color': "red"}, 'decreasing': {'color': 'limegreen'}},
        value=Humidity
        , title={'text': 'Humidity', 'font': {'size': 35}, 'align': 'center'}

        , gauge={'axis': {'range': [0, 100], "tickmode": "array",
                          "tickvals": ['0', '20', '40', '60', '80', '100'],

                          'tickfont': {'size': 16}, 'tickwidth': 2, 'tickangle': 0},

                 'steps': [{'range': [0, 20], 'color': 'lightgreen'},
                           {'range': [20, 40], 'color': 'yellow'}
                     , {'range': [40, 60], 'color': 'orange'},
                           {'range': [60, 80], 'color': 'red'},
                           {'range': [80, 100], 'color': 'blueviolet'}],

                 'bar': {
                     'color': 'darkgreen',
                     'thickness': 0.6},

                 'threshold': {
                     'line': {'color': 'red', 'width': 8},
                     'thickness': 0.7,
                     'value': 99},

                 'borderwidth': 2, 'bordercolor': 'black'}
    ), row=2, col=1)

    Fig.add_trace(Indicator(
        mode="gauge+number+delta",
        value=Air_Moisture
        , title={'text': 'Air Moisture', 'font': {'size': 35}, 'align': 'center'}

        , gauge={'axis': {'range': [0, 100], "tickmode": "array",
                          "tickvals": ['0', '20', '40', '60', '80', '100'],

                          'tickfont': {'size': 16}, 'tickwidth': 2, 'tickangle': 0},

                 'steps': [{'range': [0, 20], 'color': 'blueviolet'},
                           {'range': [20, 40], 'color': 'red'}
                     , {'range': [40, 60], 'color': 'orange'},
                           {'range': [60, 80], 'color': 'yellow'},
                           {'range': [80, 100], 'color': 'lightgreen'}],

                 'bar': {
                     'color': 'darkgreen',
                     'thickness': 0.6},

                 'threshold': {
                     'line': {'color': 'green', 'width': 8},
                     'thickness': 0.7,
                     'value': 99},

                 'borderwidth': 2, 'bordercolor': 'black'}
    ), row=2, col=3)
    print("\n\n\t Function in Middle")
    try:
        Fig.update_layout(width=1375, height=540)
        print("\n\n\t Function in Middle1")
        Window = tkinter.Toplevel()
        print("\n\n\t Function in Middle2")
        Window['bg'] = 'white'
        Window.resizable(True, True)

        Fr = Frame(Window)
        Lab = Label(Fr, text="Botanix Brain - Dashboard", font=("Times New Roman", 35, "bold"), bg="#d9ffda", cursor="hand2",
                    fg='black', bd=5, highlightthickness=5, highlightcolor="grey", relief="groove")

        Fr.grid(row=0, column=0)
        Lab.pack(pady=10, padx=10)
        print("\n\n\t Function in Middle3")
        renderers.default = 'png'
        img_bytes = to_image(Fig, format='png')
        
        PNG_Plot = PhotoImage(data=img_bytes)
        
        Lab = Label(Window, bg='white')
        Lab.config(image=PNG_Plot)
        print("\n\n\t Function in Middle41")
        Lab.image = PNG_Plot
        print("\n\n\t Function in Middle42")
        Lab.grid(row=1, column=0)

        Button(Window, text="     Get Details      ➡    ", font=("Arial", 20, "italic", "bold"), bg="#d9ffda",
            activebackground="blue", activeforeground="yellow", relief="sunken", bd=5, highlightcolor="black",
            highlightthickness=5,command=four).grid(row=2, column=0)
        
        print("\n\n\t Function in End")
        Window.mainloop()
    except Exception as E:
        print("This Exception Occured : {}".format(E))

#-------------------------------------------4th window------------------------------------------------------------------------


def four():
    # global Temperature
    # global Humidity
    # global Sun
    # global Air_Moisture
    # global Air_Quality
    
    # Temp=int(input("\n\n Enter Temperature --> "))
    # Humi=int(input("\n\n Enter Humdity --> "))
    # Sunlight=int(input("\n\n Enter Sunlight --> "))
    # Moisture=int(input("\n\n Enter Moisture --> "))
    # Quality=int(input("\n\n Enter Air Quality --> "))

    Inputs=[Temperature,Humidity,Sun,Air_Moisture,Air_Quality]

    data = pd.read_csv('Fruits_Dataset_Shuffled.csv')
    
    x = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100,random_state=42)
    model.fit(x_train, y_train)  # Train the Machine Learbing Model

    # Y_Pred=model.predict(x_test)

    Data = np.array(Inputs).reshape(1, -1)   
    
    Out = model.predict(Data)

    Output = Out[0].lower()

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(
        r"D:\\Project Botanix Brain\\ui4\\assets\\frame0")


    DataFrame = pd.read_csv("Fruits.csv")

    M = DataFrame[DataFrame['Fruit Name'].str.lower().str.strip() == Output]
    
    Fruit_Path = "ui4\\assets\\frame0\\fruits\\"
    #PC_Path = "C:\\Users\\HP\\Desktop\\"
    Another_Path="ui4\\assets\\frame0\\"
    
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)



    fontv = "Jost"

    win = tkinter.Toplevel()
    win.title("Botanix Brain | Fruit Description")
    win.geometry("856x648")
    win.configure(bg="#FFFFFF")

    canvas = Canvas(
        win,
        bg="#FFFFFF",
        height=648,
        width=856,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        3.0,
        5.0,
        851.0,
        643.0,
        fill="#6CB52C",
        outline="")

    canvas.create_rectangle(
        532.0,
        17.0,
        841.0,
        306.0,
        fill="#D9FFDA",
        outline="")

    if Output.lower() == 'apple':
        image_fruit = ImageTk.PhotoImage(Image.open(
        Fruit_Path + "1.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    elif Output.lower() == 'mango':
        image_fruit = ImageTk.PhotoImage(Image.open(
       Fruit_Path + "2.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )

    elif Output.lower() == 'banana':
        image_fruit = ImageTk.PhotoImage(Image.open(
         Fruit_Path + "5.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    elif Output.lower() == 'mousambi':

        image_fruit = ImageTk.PhotoImage(Image.open(
         Fruit_Path + "10.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    elif Output.lower() == 'pear':
        image_fruit = ImageTk.PhotoImage(Image.open(
        Fruit_Path + "11.png"))
        
        canvas.create_image(
            57,
            5.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    elif Output.lower() == 'guava':
        image_fruit = ImageTk.PhotoImage(Image.open(
        Fruit_Path + "12.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    elif Output.lower() == 'lemon':
        image_fruit = ImageTk.PhotoImage(Image.open(
         Fruit_Path + "15.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    elif Output.lower() == 'orange':
        image_fruit = ImageTk.PhotoImage(Image.open(
         Fruit_Path + "3.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    elif Output.lower() == 'cherries':
        image_fruit = ImageTk.PhotoImage(Image.open(
         Fruit_Path + "13.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    elif Output.lower() == 'kiwi':
        image_fruit = ImageTk.PhotoImage(Image.open(
         Fruit_Path + "4.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    elif Output.lower() == 'pomegranate':
        
        image_fruit = ImageTk.PhotoImage(Image.open(
         Fruit_Path + "6.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    
    elif Output.lower() == 'dragonfruit':
        
        image_fruit = ImageTk.PhotoImage(Image.open(
         Fruit_Path + "7.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    elif Output.lower() == 'blueberry':
        
        image_fruit = ImageTk.PhotoImage(Image.open(
         Fruit_Path + "9.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    elif Output.lower() == 'jamun':
        image_fruit = ImageTk.PhotoImage(Image.open(
         Fruit_Path + "14.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    elif Output.lower() == 'strawberry':
        image_fruit = ImageTk.PhotoImage(Image.open(
        Fruit_Path + "8.png"))
        
        canvas.create_image(
            575.0,
            41.0,
            # 841.0,
            # 306.0,
            anchor=NW,
            image=image_fruit
        )
    canvas.create_rectangle(
        14.0,
        18.0,
        519.0,
        306.0,
        fill="#D9FFDA",
        outline="")

    canvas.create_rectangle(
        14.0,
        318.0,
        841.0,
        631.0,
        fill="#D9FFDA",
        outline="")

    canvas.create_text(
        378.0,
        325.0,
        anchor="nw",
        text="Description",
        fill="#000000",
        font=(fontv + " Bold", 20 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets(
         Another_Path + "entry_1.png"))
    
    entry_bg_1 = canvas.create_image(
        428.0,
        486.0,
        image=entry_image_1
    )
    entry_1 = Text(win,
        bd=0,
        bg="#C9FFCA",
        fg="#000716",
        highlightthickness=0
        , font=("Times New Roman", 15))

    entry_1.insert("end", f"\n\n{M.iloc[0]['Description']})")

    entry_1.place(
        x=43.0,
        y=354.0,
        width=770.0,
        height=262.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets(
         Another_Path + "image_1.png"))
    
    image_1 = canvas.create_image(
        764.0,
        582.0,
        image=image_image_1
    )

    canvas.create_text(
        33.0,
        141.0,
        anchor="nw",
        text="Scientific Name :",
        fill="#000000",
        font=(fontv, 20 * -1)
    )

    canvas.create_text(
        33.0,
        181.0,
        anchor="nw",
        text="Sunlight Requirements :",
        fill="#000000",
        font=(fontv, 20 * -1)
    )

    canvas.create_text(
        33.0,
        224.0,
        anchor="nw",
        text="Temperature Range :",
        fill="#000000",
        font=(fontv, 20 * -1)
    )

    canvas.create_text(
        233.0,
        26.0,
        anchor="nw",
        text="Details",
        fill="#000000",
        font=(fontv + " Bold", 20 * -1)
    )

    canvas.create_text(
        33.0,
        58.0,
        anchor="nw",
        text="Fruit Name : ",
        fill="#000000",
        font=(fontv, 20 * -1)
    )

    canvas.create_text(
        33.0,
        264.0,
        anchor="nw",
        text="Soil Moisture Concentration : ",
        fill="#000000",
        font=(fontv, 20 * -1)
    )

    canvas.create_text(
        33.0,
        99.0,
        anchor="nw",
        text="Fruit Family :",
        fill="#000000",
        font=(fontv, 20 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets(
             Another_Path + "entry_2.png"))
    
    entry_bg_2 = canvas.create_image(
        329.5,
        71.5,
        image=entry_image_2
    )
    entry_2 = Entry(win,
        bd=0,
        bg="#C9FFCA",
        fg="#000716",
        highlightthickness=0
        , font=("Times New Roman", 15, "bold"))

    entry_2.insert("end", M.iloc[0]['Fruit Name'].capitalize())

    entry_2.place(
        x=162.0,
        y=55.0,
        width=335.0,
        height=31.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets(
            Another_Path + "entry_3.png"))
    
    entry_bg_3 = canvas.create_image(
        333.0,
        116.5,
        image=entry_image_3
    )
    entry_3 = Entry(win,
        bd=0,
        bg="#C9FFCA",
        fg="#000716",
        highlightthickness=0
        , font=("Times New Roman", 15, "bold"))
    entry_3.insert("end", M.iloc[0]['Family Name'])

    entry_3.place(
        x=169.0,
        y=100.0,
        width=328.0,
        height=31.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets(
            Another_Path + "entry_4.png"))
    
    entry_bg_4 = canvas.create_image(
        348.0,
        156.5,
        image=entry_image_4
    )
    entry_4 = Entry(win,
        bd=0,
        bg="#C8FFCA",
        fg="#000716",
        highlightthickness=0
        , font=("Times New Roman", 15, "bold"))

    entry_4.insert("end", M.iloc[0]['Scientific Name'])
    entry_4.place(
        x=199.0,
        y=140.0,
        width=298.0,
        height=31.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets(
            Another_Path + "entry_5.png"))
    
    entry_bg_5 = canvas.create_image(
        373.0,
        197.5,
        image=entry_image_5
    )
    entry_5 = Entry(win,
        bd=0,
        bg="#C8FFCA",
        fg="#000716",
        highlightthickness=0
        , font=("Times New Roman", 15, "bold"))
    entry_5.insert("end", M.iloc[0]['Sunlight Requirement'])

    entry_5.place(
        x=249.0,
        y=181.0,
        width=248.0,
        height=31.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets(
            Another_Path + "entry_6.png"))
    
    entry_bg_6 = canvas.create_image(
        398.5,
        280.5,
        image=entry_image_6
    )
    entry_6 = Entry(win,
        bd=0,
        bg="#C8FFCA",
        fg="#000716",
        highlightthickness=0
        , font=("Times New Roman", 15, "bold"))
    entry_6.insert("end", M.iloc[0]['Soil Moisture Concentration'])
    
    entry_6.place(
        x=300.0,
        y=264.0,
        width=197.0,
        height=31.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets(
            Another_Path + "entry_7.png"))
    
    entry_bg_7 = canvas.create_image(
        360.5,
        239.5,
        image=entry_image_7
    )
    entry_7 = Entry(win,
        bd=0,
        bg="#C8FFCA",
        fg="#000716",
        highlightthickness=0
        , font=("Times New Roman", 15, "bold"))

    entry_7.insert("end", M.iloc[0]['Temperature Range'])

    entry_7.place(
        x=224.0,
        y=223.0,
        width=273.0,
        height=31.0
    )
    win.resizable(False, False)
    win.mainloop()

#-------------------------------------------------main window work-------------------------------------------------------#


canvas = Canvas(root, height=375, width=600)
canvas.create_rectangle(0,0,238,600,fill="#d9ffda", outline="#d9ffda")
canvas.config(bg="white")
canvas.pack()

label = Label(root, text="Cultivate your passion  for plants with\n the knowledge and tools provided\n by Botanix brain.", font=("Heebo", "14"), bg="white")
label.place(x=258, y=138)

label = Label(root, text="WELCOME TO\n BOTANIX BRAIN", font=("Space Grotesk", 20,"bold"),bg="white")
label.place(x=290, y=20)

copy_right_label=Label(root,text="©This project is copyright by BxB team",bg="white",fg="grey") ##d6c4d0
copy_right_label.place(x=310,y=350)

img= ImageTk.PhotoImage(Image.open("sci_city_project\\s.png"))
canvas.create_image(-30,20,anchor=NW,image=img)
canvas.pack()

button = customtkinter.CTkButton(master=root,text="Let's start",width=120, height=32,border_width=0,corner_radius=8,fg_color="green",cursor="hand2",command=win) #hover_color(blue)
button.place(x=460,y=300)

root.mainloop()