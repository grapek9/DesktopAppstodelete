import tkinter as tk
from tkinter import *
def runHelpWindowGUI():
	class helpWindow(tk.Frame):
		def __init__(self,master=None):
			tk.Frame.__init__(self,master,width=0,height=0)
			self.pack()
			self.grid(row=30,column=30)
			self.createWidgets()
			master.minsize(width=640,height=480)
			master.maxsize(width=640,height=480)
			master.title("FileExplorer by grapek9")
		def createWidgets(self):
			mainframe = tk.Frame(self,bg="orange",width=640,height=480)
			mainframe.grid(row=1,column=0)
			mainframe.pack()
			frame1 = tk.Frame(mainframe,width=640)
			frame1.grid(row=0,column=0,columnspan=60)
			path = tk.Entry(frame1,width=100)
			path.grid(row=0,column=0)
			helpButton = tk.Button(frame1,text="Help",command="openHelpWindow")
			helpButton.grid(row=0,column=1)
			#frame1.pack()
			frame2 = tk.Frame(mainframe,bg="green",width=100,height=100)
			frame2.grid(row=1,column=0)
			#frame2.pack()	
		def openHelpWindow():
			
			pass
	root= tk.Tk()
	app = helpWindow(master=root)
	app.mainloop()
	print("done?")