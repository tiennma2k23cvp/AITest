
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer



from tkinter import *
import os
import sys
# import Register
# import Resend_Password
import UI.Register
import UI.Resend_Password
from Utils.Sources.authen import Auth
# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class login_frame(Frame):
    def __init__(self, parent, controller):
        self.parent = parent
        Frame.__init__(self, parent)
        self.configure(bg="#FFFFFF")

        # scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

        # def finddir(name, path):
        #     for root, dirs, files in os.walk(path):
        #         if name in files:
        #             return os.path.join(root, name)

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=480,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        # create canvas
        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            138.0,
            0.0,
            661.0,
            480.0,
            fill="#A9A9A9",
            outline="")

        # create hyperlink
        txt = canvas.create_text(
            435,
            397.0,
            anchor="nw",
            text="Register here",
            fill="#FFFFFF",
            font=("Lato ", 14 * -1)
        )
        canvas.tag_bind(txt, '<Enter>', lambda _: canvas.itemconfig(
            txt, fill="#BBBBBB"))
        canvas.tag_bind(txt, '<Leave>', lambda _: canvas.itemconfig(
            txt, fill="#FFFFFF"))
        canvas.tag_bind(txt, '<ButtonPress-1>',
                        lambda _: controller.show_frame(UI.Register.sign_up_frame))
        # def txt_on_click(e):
        #     txt.configure(fg="#666666")
        #     controller.show_frame(sign_up_frame)

        # txt = Label(self, text="Register here", font=(
        #     "Lato Regular", 14 * -1), fg="white", bg="#A9A9A9")
        # txt.place(x=430, y=393.77)
        # txt.bind('<Button-1>', txt_on_click)
        # txt.bind('<Enter>', lambda e: txt.configure(fg="#BBBBBB"))
        # txt.bind('<Leave>', lambda e: txt.configure(fg="white"))

        # forget pass
        forget_pass = Label(self, text="Forget password?", font=(
            "Lato Regular", 14 * -1), fg="white", bg="#A9A9A9")
        forget_pass.place(x=432, y=288)

        def fgpass_on_click(e):
            forget_pass.configure(fg="#666666")
            controller.show_frame(UI.Resend_Password.resend)

        forget_pass.bind('<Button-1>', fgpass_on_click)
        forget_pass.bind(
            '<Enter>', lambda e: forget_pass.configure(fg="#BBBBBB"))
        forget_pass.bind(
            '<Leave>', lambda e: forget_pass.configure(fg="white"))

        # create other text
        canvas.create_text(
            279.0,
            397.0,
            anchor="nw",
            text="Don’t have an account?",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        # create login button
        self.button_image_1 = PhotoImage(
            file=r"./UI/assets/frame1/button_1.png")
        self.button_image_2 = PhotoImage(
            file=r"./UI/assets/frame1/button_1_hover.png")
        # def button_1_onclick():
        #     button_1.configure(image=self.button_image_3)
        #     # nhảy sang home page tính sau

        button_1 = canvas.create_image(
            301.0,
            328.0,
            image=self.button_image_1,
            anchor='nw',
        )
        canvas.tag_bind(button_1, '<ButtonPress-1>',
                        lambda _: self.onLoginClick())

        # hover button
        canvas.tag_bind(button_1, '<Enter>', lambda _: canvas.itemconfig(
            button_1, image=self.button_image_2))
        canvas.tag_bind(button_1, '<Leave>', lambda _: canvas.itemconfig(
            button_1, image=self.button_image_1))

        # # place button
        # button_1.place(
        #     x=301.0,
        #     y=328.0,
        #     width=198.3193359375,
        #     height=54.0
        # )

        # create texts above textboxes
        canvas.create_text(
            248.0,
            141.0,
            anchor="nw",
            text="Username/Email*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            248.0,
            219.0,
            anchor="nw",
            text="Password*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            355.0,
            57.0,
            anchor="nw",
            text="LOGIN",
            fill="#FFFFFF",
            font=("Lato Regular", 29 * -1)
        )

        # create textboxes
        self.email = StringVar()
        self.password = StringVar()

        self.entry_image_1 = PhotoImage(
            file=r"./UI/assets/frame1/entry_1.png")
        entry_bg_1 = canvas.create_image(
            399.667236328125,
            183.09378051757812,
            image=self.entry_image_1
        )
        entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Lato"),
            textvariable=self.email
        )
        entry_1.place(
            x=257.2668390274048,
            y=159.0,
            width=284.80079460144043,
            height=46.18756103515625
        )

        self.entry_image_2 = PhotoImage(
            file=r"./UI/assets/frame1/entry_2.png")
        entry_bg_2 = canvas.create_image(
            399.667236328125,
            261.1086120605469,
            image=self.entry_image_2
        )
        entry_2 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=('Lato'),
            textvariable=self.password,
            show="*"
        )
        entry_2.place(
            x=257.2668390274048,
            y=237.01483154296875,
            width=284.8008556365967,
            height=46.18756103515625
        )

    def onLoginClick(self):
        if (Auth(self.email, self.password).UserAuth()):
            self.parent.parent.Authed.set(True)
            self.parent.parent.geometry('800x480')
            self.parent.parent.main.pack()
            self.parent.destroy()
