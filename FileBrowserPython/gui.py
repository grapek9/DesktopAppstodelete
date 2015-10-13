import tkinter as tk
def runGui():
	class MainWindow(tk.Frame):
		def __init__(self,master=None):
			tk.Frame.__init__(self,master)
			self.pack()
			self.createWidgets()
			master.minsize(width=666,height=666)
			master.maxsize(width=666,height=666)
			master.title("FileExplorer by grapek9")
		def createWidgets(self):
			self.button = tk.Button(self)
			self.button["text"] = "Hello World\n(click me)"
			self.button["command"] = self.say_something
			self.button.pack(side="top")

			self.QUIT = tk.Button(self,text="QUIT",fg="red",command=root.destroy)
			self.QUIT.pack(side="bottom")

		def say_something(self):
			print("something")

	root= tk.Tk()
	app = MainWindow(master=root)
	app.mainloop()
	print("done?")