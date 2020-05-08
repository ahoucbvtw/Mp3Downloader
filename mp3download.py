import youtube_dl
from tkinter import *
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import filedialog

class Main(object):

	def __init__(self):

		self.window = Tk()
		self.window.title("YoutubeMusicDownloader") #視窗名稱
		self.window.config(background = "#f0f0f0")#更該視窗背景顏色
		self.window.geometry("390x360+800+250") #視窗解析度 (x*y+視窗欲固定的畫面位置X+視窗欲固定的畫面位置Y)
		self.window.resizable(0,0) #不可以更改大⼩
		Font = tkfont.Font(family = "新細明體", size = 10, weight = "bold")
		Font_path = tkfont.Font(family = "新細明體", size = 12)

		# def my_hook(d):
		# 	if d['status'] == 'finished':
		# 		messagebox.showinfo(title = "Notice", message = "歌曲已全部下載完成！！")
		# 		downloadlist.delete(0,END)

		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',}]}
			# }],'progress_hooks': [my_hook],}

		def addURL():
			try:
				url = inputurl.get()
				url.index("https://www.youtube.com/watch?v=")
			except:
				messagebox.showerror(title = "Error", message = "請輸入正確Youtube網址！！")
				inputurl.delete(0, END)
			else:
				downloadlist.insert(END,inputurl.get())
				inputurl.delete(0, END)

		def mp3download():
			print(downloadlist.get(0,END))
			for i in downloadlist.get(0,END):
				with youtube_dl.YoutubeDL(ydl_opts) as ydl:
					ydl.download([i])
				downloadlist.delete(0,END)

		frame = Frame(self.window)
		frame.grid(row = 0, padx = 10, pady = 10)

		inputurltitle = Label(frame, font = Font, text = "請輸入Youtube網址：")
		inputurltitle.grid(row = 0, padx = 5, pady = 5)

		addlist = Button(frame, text = "添加++", font = Font, bg = "skyblue", width = 8, height = 1, command = addURL)
		addlist.grid(row = 0, column = 1, padx = 5, pady = 5)

		inputurl = Entry(frame, font = Font_path, width = 45)
		inputurl.grid(row = 1, columnspan = 3, padx = 5, pady = 5)

		frame1title = Label(self.window, font = Font, text = "下載清單列表：")
		frame1title.grid(row = 1, column = 0, padx = 5, pady = 5)

		frame1 = Frame(self.window)
		frame1.grid(row = 2, column = 0, padx = 10, pady = 10)

		slb = Scrollbar(frame1) #垂直滾動條元件 
		slb.pack(side = RIGHT, fill = Y) #設定垂直滾動條顯示的位置 
		downloadlist = Listbox(frame1, height = 10, width = 42, font = Font_path, exportselection = False, borderwidth = 3, selectmode = "single",bg= "#b5e1f3", yscrollcommand = slb.set)
		downloadlist.pack(side = LEFT, fill = BOTH)
		slb.config(command = downloadlist.yview) #設定Scrollbar元件的command選項為該元件的yview()方法

		start = Button(self.window, text = "Download", font = Font, bg = "skyblue", width = 8, height = 1, command = mp3download)
		start.grid(row = 3, column = 0, padx = 5, pady = 5)


		self.window.mainloop()

if __name__ == '__main__':
	Main()
