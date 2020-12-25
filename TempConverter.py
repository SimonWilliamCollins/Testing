#temp framework
from tkinter import *
from converters import *
#test commit
class App:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		Label(frame, text='deg c').grid(row = 0, column = 0)
		self.c_var = DoubleVar()
		Entry(frame, textvariable=self.c_var).grid(row = 0, column = 1)
		Label(frame, text='deg F').grid(row = 1, column = 0)
		self.result_var = DoubleVar()
		Label(frame, textvariable = self.result_var).grid(row = 1, column = 1)
		button = Button(frame, text='Convert', command=self.convert)
		button.grid(row = 2, columnspan=2)

	def convert(self):
		c = self.c_var.get()
		self.result_var.set(self.t_conv.convert(c))

root = Tk()
root.wm_title('Temp Converter')
app = App(root)
root.mainloop()