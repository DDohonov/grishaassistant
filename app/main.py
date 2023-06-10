import tkinter
import customtkinter
import requests

API_URL_START = 'http://127.0.0.1:5001/start/'
API_URL_STOP = 'http://127.0.0.1:5001/stop/'
STATUS = False

but_tk = tkinter.Tk()
tk_list = [but_tk]
for i in tk_list:
    i.geometry("400x500")
    i.title("Grigorius")
    i.iconbitmap(r'grishaassistant-master\custom\icon.ico')
    i["bg"] = "gray22"

customtkinter.set_appearance_mode("System")

def button_function():
    global STATUS
    if STATUS:
        button.configure(text='🎤')
        STATUS = False
        requests.get(API_URL_STOP)
    else:
        button.configure(text='🔊')
        STATUS = True
        requests.get(API_URL_START)
    # print(voice_input)
    # txt_qu.configure(text=deform_txt(voice_input))

button = customtkinter.CTkButton(master=but_tk, width=300, height=400, corner_radius=15, command=button_function, fg_color="Light Grey", text_color="Black", text="🎤")
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)



but_tk.mainloop()