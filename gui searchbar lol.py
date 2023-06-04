import tkinter as tk
import subprocess
window = tk.Tk()
answer = []
def open_link_in_chrome(link):
    # Specify the Chrome executable path
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    # Construct the command to open the link in Chrome
    command = [chrome_path, link]

    # Execute the command
    subprocess.Popen(command)

def submityt():
    answer.append(entry.get())
    print(answer[0])
    joe = r'https://www.youtube.com/results?search_query=' + answer[0]
    open_link_in_chrome(joe)
    entry.delete(0,tk.END)
    answer.clear()
def submitgoogle():
    answer.append(entry.get())
    print(answer[0])
    joe = r'https://www.google.com/search?q=' + answer[0]
    open_link_in_chrome(joe)
    entry.delete(0,tk.END)
    answer.clear()
def clear():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get())-1, tk.END)
entry = tk.Entry(window,font=('Papyrus',40))
entry.pack(side=tk.LEFT)
submit_buttonyt = tk.Button(window,text='youtubr',font=('Papyrus',10),command=submityt)
submit_buttonyt.pack(side=tk.RIGHT)
submit_buttongg = tk.Button(window,text='google',font=('Papyrus',10),command=submitgoogle)
submit_buttongg.pack(side=tk.RIGHT)
clear_button = tk.Button(window,text='clear',font=('Papyrus',10),command=clear)
clear_button.pack(side=tk.RIGHT)
backspace_button = tk.Button(window,text='backspace',font=('Papyrus',10),command=backspace)
backspace_button.pack(side=tk.RIGHT)
window.mainloop()
