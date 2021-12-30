from pytube import YouTube
from tkinter import *
from PIL import Image,ImageTk
import requests
import os

def download_vid(root, e, d_link, yt):
	location = e.get()
	if location == "":
		raise Exception("Location Error")
	elif not os.path.exists(location):
		raise Exception("Location Doesn't Exists")
	else:
		dd = d_link[0].itag
		ys = yt.streams.get_by_itag(dd)
		ys.download(location)
		suc_mes = Label(root, text="Success")
		suc_mes.grid(row=5,column=0,padx=20)




def get_url(e,root,ub):
	root.geometry("800x600")
	text = e.get()
	print(repr(text))
	e.destroy()
	ub.destroy()
	vid_data = get_data(repr(text))
	im = Image.open(requests.get(vid_data[3], stream=True).raw)
	img = im.resize((720,350), Image.ANTIALIAS)
	test = ImageTk.PhotoImage(img)
	im_label = Label(image=test)
	im_label.image = test
	im_label.grid(row=0,column=0,pady=20,padx=20)
	vid_title = Label(root, text=vid_data[0], font=("Arial", 20))
	vid_title.grid(row=1, column=0,pady=20,padx=20)
	len_min = int(vid_data[2])//60
	len_sec = int(vid_data[2]) - int(len_min*60)
	len_text = "Video-Length -> %d:%d" %(len_min,len_sec)
	vid_length = Label(root, text=len_text, font=("Arial", 15))
	vid_length.grid(row=2,column=0,padx=20)
	d_link = vid_data[4]
	loc_entry = Entry(root,width=30)
	loc_entry.grid(row=3,column=0,padx=20)
	download_but = Button(root, text="Download", command=lambda: download_vid(root,loc_entry,d_link,vid_data[5]))
	download_but.grid(row=4,column=0,padx=20)



def get_data(text):
	try:
		yt = YouTube(text)
		vid_data = [yt.title, yt.views, yt.length, yt.thumbnail_url, yt.streams.filter(progressive=True), yt]
		return vid_data
	except:
		print("Error!!!")



root_frame = Tk()
root_frame.iconbitmap("ter.ico")
root_frame.title("Youtube Video Downloader")


url_entry = Entry(root_frame, width=30)
url_entry.grid(row=0,column=0,pady=20,padx=20)
url_but = Button(root_frame,text="Search",command=lambda: get_url(url_entry,root_frame,url_but))
url_but.grid(row=0,column=1,pady=20,padx=10)


root_frame.mainloop()
