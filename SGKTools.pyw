import tkinter as tk
import tkinter.font as tkFont
import re

divert = ("pawn","wdist", "knight", "kdist", "bishop", "bdist", "rook", "rdist", "queen", "qdist", "king", "wdist", "boss", "all", "leader", "none", "inner", "contact", "decree", "grenade", "strafe", "scope", "{ n=", "<special>", "first_reload", "firepower", "firerange")
divert2 = ("Extra White Card", "Extra Black Card", "Card Name")

g = open("cards.txt", "w")

class App:
    def __init__(self, root):
        #setting title
        root.title("Shotgun king modding tools")
        #setting window size
        width=300
        height=240
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_148=tk.Button(root)
        GButton_148["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_148["font"] = ft
        GButton_148["fg"] = "#000000"
        GButton_148["justify"] = "center"
        GButton_148["text"] = "Generate"
        GButton_148.place(x=80,y=150,width=125,height=38)
        GButton_148["command"] = self.GButton_148_command

        GMessage_914=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_914["font"] = ft
        GMessage_914["fg"] = "#333333"
        GMessage_914["justify"] = "center"
        GMessage_914["text"] = "Generates a file with card name translations for the english.txt file"
        GMessage_914.place(x=0,y=0,width=295,height=163)

    def GButton_148_command(self):
        with open('script.lua') as f:
            brink = 1
            for line in f:
                if line.startswith("EXCLUDE={"):
                    brink = 0
                cont = re.findall('"(.*?)"', line)
                if brink == 1:
                    for word in cont:
                        if not word.startswith(divert2):
                            if not word.endswith(divert):
                                g.write(word + "::" + word + "\n")
        g.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
