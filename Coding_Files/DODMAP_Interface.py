#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:04:39 2021

@author: denise
"""
import tkinter as tk
from tkinter import font as tkFont
HEIGHT = 700
WIDTH = 800

class RichText(tk.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        default_font = tkFont.nametofont(self.cget("font"))

        em = default_font.measure("m")
        default_size = default_font.cget("size")
        bold_font = tkFont.Font(**default_font.configure())
        italic_font = tkFont.Font(**default_font.configure())
        h1_font = tkFont.Font(**default_font.configure())

        bold_font.configure(weight="bold")
        italic_font.configure(slant="italic")
        h1_font.configure(size=int(default_size*2), weight="bold")

        self.tag_configure("bold", font=bold_font)
        self.tag_configure("italic", font=italic_font)
        self.tag_configure("h1", font=h1_font, spacing3=default_size)

        lmargin2 = em + default_font.measure("\u2022 ")
        self.tag_configure("bullet", lmargin1=em, lmargin2=lmargin2)

    def insert_bullet(self, index, text):
        self.insert(index, f"\u2022 {text}", "bullet")

class MAP_gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.TK.__init__(self, *args, **kwargs)

        #creating container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        self.frames = {}

        #iterating through page layouts
        for F in (DOD_Banner, Provider_Page, Patient_Page):
            frame = F(Container, self)
            self.frames[F] = frame

            frame.gridJ(row = =0, column = 0, sticky ="nsew")

        self.show_frame(DOD_Banner)
            #to display current frame
        def show_frame(self, cont):
            frame = self.frames[cont]
                frame.tkraise()


class DOD_Banner(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = )
root = tk.Tk()
window.title("DODMAP Interface")

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()


"You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only./n" \
"By using this IS (which includes any device attached to this IS), you consent to the following conditions:" \
"The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, " \
"COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and " \
"counterintelligence (CI) investigations.At any time, the USG may inspect and seize data stored on this IS." \
"Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose." \
"This IS includes security measures (e.g., authentication and access controls) to protect USG interests-not for your personal benefit or privacy." \
"Notwithstanding the above, using this IS does not constitute consent to PM, LE, or CI investigative " \
"searching or monitoring of the content of privileged communications, or work product, related to personal " \
"representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications " \
"and work product are private and confidential. See User Agreement for details.
frame = tk.Frame(root, bg = '#c8c8c8')
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
button = tk.Button(root, text = "Test button", bg = 'gray', fg = 'black')
button.pack()
# =============================================================================
# background_image = tk.PhotoImage(file = 'images.jpeg')
# background_label = tk.Label(root, image = background_image)
# background_label.place(relwidth = 1, relhegith = 1)
# =============================================================================

root.mainloop()


