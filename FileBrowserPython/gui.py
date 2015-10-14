import tkinter as tk
def runGui():
	class MainWindow(tk.Frame):
		def __init__(self,master=None):
			tk.Frame.__init__(self,master,width=0,height=0)
			self.pack()
			self.grid(row=30,column=30)
			self.createWidgets()
			master.minsize(width=640,height=480)
			master.maxsize(width=666,height=666)
			master.title("FileExplorer by grapek9")
		def createWidgets(self):
			mainframe = tk.Frame(self,bg="orange",width=640,height=480)
			mainframe.grid(row=1,column=0)
			mainframe.pack()
			frame1 = tk.Frame(mainframe,bg="red",width=100,height=100)
			frame1.grid(row=0,column=0)
			#frame1.pack()
			frame2 = tk.Frame(mainframe,bg="green",width=100,height=100)
			frame2.grid(row=1,column=1)
			#frame2.pack()

			
	root= tk.Tk()
	app = MainWindow(master=root)
	app.mainloop()
	print("done?")


#reminder = building ui inside frame1