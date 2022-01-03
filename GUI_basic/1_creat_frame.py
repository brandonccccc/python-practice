from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로 지정
#root.geometry("640x480+100+300") # 가로*세로 + x좌표+y좌표

root.resizable(False, False) # x(너비), y(높이) 크기 변경 불가

root.mainloop()