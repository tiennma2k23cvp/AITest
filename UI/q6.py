from tkinter import *
from pathlib import Path
from Database_processing.User_db.update_login_first import *
from Utils.Sources.getdata_pickle import load_object
import UI.q5
from Utils.Sources.getdata_pickle import load_object
from Utils.Sources.savedata_pickle import save_object
import tkinter.messagebox as messagebox

OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/question")
def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

class q6(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.username = ""
        self.loadData()


        self.canvas = Canvas(
            self,
            bg="#FFFF0F",
            height=480,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack()

        def hovertxt(sometxt):
            self.canvas.tag_bind(sometxt, '<Enter>', lambda _: self.canvas.itemconfig(
                sometxt, fill="#999999"))
            self.canvas.tag_bind(sometxt, '<Leave>', lambda _: self.canvas.itemconfig(
                sometxt, fill="#646464"))

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            400.0,
            240.0,
            image=self.image_image_1
        )
        # #logo txt
        # home_txt=self.canvas.create_text(
        #     93,
        #     22,
        #     anchor="nw",
        #     text="EXERA",
        #     fill="#646464",
        #     font=("Lato", int(30))
        # )
        #back button
        button_1 = Button(
            self.canvas,
            text="Back",
            font=('Lato', 14),
            bg="#9E9E9E",
            fg="white",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.onBackClick(),
            relief="flat"
        )
        button_1.place(
            x = 0, 
            y = 0,
            width = 74,
            height = 43,
        )

        #next button
        button_2 = Button(
            self.canvas,
            text="Next",
            font=('Lato', 14),
            fg="white",
            bg="#636363",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.onNextClick(),
            relief="flat"
        )
        button_2.place(
            x = 726, 
            y = 437,
            width = 74,
            height = 43,
        )
        #entry
        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            353,
            255,
            image=self.entry_image_1,
            anchor = "nw"
        )
        self.entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#C7C7C7",
            fg="#000716",
            highlightthickness=0,
            font = ("Lato")
        )
        self.entry_1.place(
            x=359,
            y=255,
            width=75,
            height=42.0
        )
        #question txt
        q_txt=self.canvas.create_text(
            400, 
            205,
            anchor="center",
            text="How many times per week do you want to practice:",
            fill="#646464",
            font=("Lato", int(25) * -1, "bold")
        )

    def onNextClick(self):
        var = self.entry_1.get()
        flag = True
        self.alert_exist = False
        try: 
            float(var)
        except:
            flag = False
        if (flag): 
            print(self.username)
            update_login_first(self.username, False)
            self.parent.parent.Authed.set(True)
            self.parent.parent.geometry('800x480')
            self.parent.parent.main.pack()
            self.parent.destroy()
        else:
            messagebox.showerror('Error', 'You must enter a number!')

    def onBackClick(self):
        var = self.entry_1.get()
        flag = True
        self.alert_exist = False
        try: 
            float(var)
        except:
            flag = False
        if (flag): 
            self.parent.show_frame(UI.q5.q5)
        else:
            messagebox.showerror('Error', 'You must enter a number!')

    def loadData(self):
        __=load_object("Appdata/userData/data.pickle")
        if (__['status']==True):
            self.username = __['data']['username']