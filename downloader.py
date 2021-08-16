import os
import subprocess
from tkinter import *
from pytube import YouTube

window = Tk()
window.geometry('500x300')
window.resizable(0,0)
window.title("YouTube Downloader")

Label(window, text = 'YouTube Video Downloader', font = 'arial 20 bold').pack()

link = StringVar()
Label(window, text = 'Paste link here: ', font = 'arial 15').place(x = 32, y = 60)
link_enter = Entry(window, width = 70, textvariable = link).place(x = 32, y = 90)

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

path = get_download_path();

def OpenPath():
	subprocess.Popen('explorer '+path)

def DownloadVideo():
	url = YouTube(str(link.get()))
	video = url.streams.get_highest_resolution()
	video.download(path)
	Label(window, text = 'Finished Downloading!', font = 'arial 15 bold').place(x = 140, y = 210)
	Button(window, text = 'Open file location', font = 'arial 15', bg = 'pale violet red', padx = 2, command = OpenPath).place(x = 160, y = 240)
def DownloadAudio():
	url = YouTube(str(link.get()))
	video = url.streams.filter(only_audio = True).first()
	out_file = video.download(path)
	base, ext = os.path.splitext(out_file)
	new_file = base + '.mp3'
	os.replace(out_file, new_file)
	Label(window, text = 'Finished Downloading!', font = 'arial 15 bold').place(x = 140, y = 210)
	Button(window, text = 'Open file location', font = 'arial 15', bg = 'pale violet red', padx = 2, command = OpenPath).place(x = 160, y = 240)
	
Button(window, text = 'DOWNLOAD VIDEO', font = 'arial 15', bg = 'pale violet red', padx = 2, command = DownloadVideo).place(x = 32, y = 150)
Button(window, text = 'DOWNLOAD AUDIO', font = 'arial 15', bg = 'pale violet red', padx = 2, command = DownloadAudio).place(x = 253, y = 150)

window.mainloop()

# just like that :D