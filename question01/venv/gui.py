# BSSD Midterm Project
# Scott Bing
# Image Analysis

from tkinter import *
from stenography import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageTk, ImageOps, ImageEnhance, ImageFont
import os


class Application(Frame):
    """ GUI application that displays the image processing
        selections"""

    def __init__(self, master):
        """ Initialize Frame - application constructor"""
        super(Application, self).__init__(master)

        Frame.__init__(self, master)
        self.master = master

        # set filename as global
        self.fileName = None

        self.grid()
        # open the application frame
        self.create_widgets()
        # self.create_initial_screen()

    # end application constructor

    def openFile(self):
        """Process the Open File Menu"""
        # reset the screen
        self.resetScreen()

        self.fileName = askopenfilename(parent=self,
                                        initialdir=os.getcwd(),
                                        filetypes=[("PNG files", ".png .PNG")],
                                        title='Choose an image.')
        print("fileName = ", self.fileName)
    # end def openFile(self):

    def resetScreen(self):
        """Clears the screen. Sets the screen
        back to its defaults"""
        # clear the message
        self.msg2show.set('')

        # reset radio buttons
        self.encode.deselect()
        self.decode.deselect()
        self.encode.select()

    # end def clearScreen(self):

    def create_widgets(self):
        """ Create and place screen widgets in the
        main application frame"""
        self.lblFont = font.Font(weight="bold")
        self.lblFont = font.Font(size=20)

        Label(self,
              text="Welcome to Steganography",
              wraplength=300,
              font=self.lblFont
              ).grid(row=0, column=0, columnspan=3, sticky=NSEW)

        animFont = font.Font(weight="bold")
        animFont = font.Font(size=21)

        # create a the open file button
        self.file_btn = Button(self,
                               text="Select an Image File",
                               command=self.openFile,
                               highlightbackground='#2E4149'
                               # font=btnFont
                               ).grid(row=1, column=0, sticky=W, pady=10, padx=5)

        Label(self,
              text="Select an Operation"
              ).grid(row=2, column=0, columnspan=2, sticky=W)

        self.codeValue = tk.StringVar()
        self.encode = tk.Radiobutton(self, text='Encode',
                                     variable=self.codeValue, value='E')
        self.encode.select()
        self.decode = tk.Radiobutton(self, text='Decode',
                                     variable=self.codeValue, value='D')

        self.encode.grid(column=0, row=3, sticky=W)
        self.decode.grid(column=0, row=4, sticky=W)

        Label(self,
              text="Encoded Message:"
              ).grid(row=5, column=0, sticky=W)
        self.msg_ent = Entry(self, width=35)
        self.msg_ent.grid(row=6, column=0, columnspan=2, padx=5, sticky=W)

        Label(self,
              text="Decoded Message:"
              ).grid(row=5, column=0, sticky=W)

        self.decoded_message = StringVar()
        Label(self,
              textvariable = self.decoded_message,
        ).grid(row=6, column=0, sticky=W)

        btnFont = font.Font(weight="bold")
        btnFont = font.Font(size=19)

        # create a the generate button
        self.generate_btn = Button(self,
                                   text="Run",
                                   command=self.processSelections,
                                   highlightbackground='#3E4149'
                                   # font=btnFont
                                   ).grid(row=7, column=0, sticky=W, pady=10, padx=5)

        # create a the clear screen button
        self.clear_btn = Button(self,
                                text="Clear",
                                command=self.resetScreen,
                                highlightbackground='#2E4149'
                                # font=btnFont
                                ).grid(row=7, column=1, sticky=W, pady=10, padx=5)

        self.msg2show = StringVar()
        Label(self,
              textvariable=self.msg2show,
              wraplength=500
              ).grid(row=10, column=0, columnspan=2, sticky=W, pady=4)

        self.errFont = font.Font(weight="bold")
        self.errFont = font.Font(size=20)
        self.err2show = StringVar()
        Label(self,
              textvariable=self.err2show,
              foreground="red",
              font=self.errFont,
              wraplength=200
              ).grid(row=9, column=0, sticky=NSEW, pady=4)

    # end def create_widgets(self):

    # process user selections
    def processSelections(self):
        """Processes user screen selections"""
        if self.codeValue.get() == 'E':
            self.newFileName = encode(self.fileName, self.msg_ent.get())
            self.msg2show.set("Encoded file: " + self.newFileName + " successfully created and encoded.")
        elif self.codeValue.get() == 'D':
            decode(self.fileName)
    # end def processSelections(self):


# main
def main():
    """Application Entry Point - the main
    driver code for the BSSD5410 Midterm Project"""
    root = Tk()
    root.resizable(height=None, width=None)
    root.title("BSSD 5410 Final Question #1")
    root.iconbitmap('William_Shakespeare.ico')
    root.geometry("450x350")
    app = Application(root)
    root.mainloop()


if __name__ == "__main__":
    main()
