from pathlib import Path
from tkinter import Tk, Canvas, Entry,Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Desktop\sci_city_project\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("610x379")
window.configure(bg = "#FFFFFF")
canvas = Canvas( window,bg = "#FFFFFF",height = 379,width = 610,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.create_rectangle(10.0,4.0,610.0,379.0,fill="#FFFFFF",outline="")

canvas.create_rectangle(15.0,6.0,603.0,91.0,fill="#D9FFDA",outline="")

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(82.0,46.0,image=image_image_1)

canvas.create_rectangle(147.0,98.0, 603.0,375.0,fill="#D9FFDA",outline="")

canvas.create_text(165.0,112.0,anchor="nw",text="Temperature:-",fill="#000000",font=("Inter", 14 * -1))

canvas.create_text(
    165.0,
    174.0,
    anchor="nw",
    text="Humidity:-",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    421.0,
    174.0,
    anchor="nw",
    text="Air quality:-",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    165.0,
    236.0,
    anchor="nw",
    text="Sunlight:-",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    421.0,
    112.0,
    anchor="nw",
    text="Moisture:-",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(241.0,151.5,image=entry_image_1)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=174.0,
    y=141.0,
    width=134.0,
    height=19.0
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(496.0,151.5,image=entry_image_2)
entry_2 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
entry_2.place(x=429.0,y=141.0,width=134.0,height=19.0)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(241.0,213.5,image=entry_image_3)
entry_3 = Entry(bd=0,bg="#D9D9D9",fg="#000716", highlightthickness=0)
entry_3.place(x=174.0, y=203.0,width=134.0, height=19.0)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(496.0,209.5,image=entry_image_4)
entry_4 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
entry_4.place(x=429.0,y=199.0,width=134.0,height=19.0)

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(241.0,275.5, image=entry_image_5)
entry_5 = Entry( bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
entry_5.place( x=174.0,y=265.0, width=134.0,height=19.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: print("button_1 clicked"), relief="flat")
button_1.place(x=489.0, y=326.0,  width=97.0,height=29.0)

canvas.create_text(166.0,289.0,anchor="nw",text="(As descreate value either 0 or 1)",fill="#808080",font=("Inter", 12 * -1))

canvas.create_text(200.0,310.0,anchor="nw",text="(0=Shady, 1=Sunny)",fill="#808080",font=("Inter", 12 * -1))

canvas.create_rectangle(14.0,98.0,142.0,375.0,fill="#D9FFDA",outline="")

canvas.create_text(33.0,324.0,anchor="nw",text="Make sure the \n\n",fill="#808080",font=("Inter", 11 * -1))

canvas.create_text(453.0,48.0,anchor="nw",text="DATA READINGS",fill="#000000",font=("JostRoman Regular", 16 * -1))

canvas.create_text(40.0,338.0,anchor="nw",text="sensors are ",fill="#808080",font=("Inter", 11 * -1))

canvas.create_text(14.0,353.0,anchor="nw",text="     placed correctly.",fill="#808080",font=("Inter", 11 * -1))

window.resizable(False, False)
window.mainloop()
