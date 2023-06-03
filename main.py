from recognize.rec import *
from response.init import *
import os
import asyncio

import tkinter
import customtkinter

listening = False

def deform_txt(message:str):
    mes_l = message.split(" ")
    flag = 0
    for i in range(len(mes_l)):
        if flag == 0:
            if "\n" in mes_l[i]:
                cash = mes_l[i].split("\n")
                mes_l[i] = cash[0]
                mes_l.insert(i+1, "\n")
                mes_l.insert(i+2, cash[1])
                flag += 2
        else:
            flag -= 1
    ress = []
    g = 0
    for i in mes_l:
        if i == "\n":
            if ress == []:
                pass
            else:
                g += 1
        else:
            try:
                if len(ress[g]) <= 25 and len(ress[g]) + len(i):
                    ress[g] = ress[g] + " " + i
                else:
                    g += 1
                    ress.append(i)
            except IndexError:
                ress.append(i)
    rtn = ""
    for i in ress:
        rtn += i + "\n"
    return rtn

but_tk = tkinter.Tk()
txt_tk = tkinter.Tk()
tk_list = [txt_tk,but_tk]
for i in tk_list:
    i.geometry("400x500")
    i.title("Grigorius")
    i.iconbitmap(os.path.abspath(__file__ + '/..') + '/icon.ico')
    i["bg"] = "gray22"

customtkinter.set_appearance_mode("System")

# async def button_function():
#     # thread1 = threading.Thread(target=change_button)
#     # print('222')
#     # thread1.start()
#     # print('333')
#     # thread1.join()
#     # print('312121')
#     await change_button()
#     # print(111)
#     # button.configure(text='🔊')
#     # # старт записи речи с последующим выводом распознанной речи 
#     voice_input = record_and_recognize_audio()
#     # print(voice_input)
#     txt_qu.configure(text=deform_txt(voice_input))

#     for tolk in list_tolking:
#         for req in tolk.request:
#             if req in voice_input:
#                 tolk.response(voice_input)
#                 break
#     # button.configure(text='🎤')
#     # tts_engine.runAndWait()

# async def change_button():
#     global button
#     print('11')
#     await button.configure(text='🔊')
#     print('332')
button = customtkinter.CTkButton(master=but_tk, width=300, height=400, corner_radius=15, command=button_function, fg_color="Light Grey", text_color="Black", text="🎤")
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

start_txt = '''Здравствуйте!
В этом отдельном окне будет отображаться ваш текст, что был услышан Григорием, а так же его ответы для лучшей эфективности взаимодействия.
(Мини подсказка) Чтобы начать работу - нажмите на кнопку и пока микрофон синий - можете говорить. Так же ви можете писать под этим выводом для простого контакта, чтоб не проговаривать текст и/или если бот не может вас понять.'''

txt_qu = customtkinter.CTkLabel(master=txt_tk, width=300, height=400, corner_radius=2, fg_color="Light Grey", text_color="Blue", text=deform_txt(start_txt))
txt_qu.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# def close_window():
#     txt_tk.destroy()
# but_tk.protocol("WM_DELETE_WINDOW", close_window)


but_tk.mainloop()


#Good dumplings are very very tasty

while True:
    # старт записи речи с последующим выводом распознанной речи 
    voice_input = record_and_recognize_audio()
    print(voice_input)
    if voice_input == 'стоп':
        break
    else:
        for tolk in list_tolking:
            for req in tolk.request:
                if req in voice_input:
                    tolk.response(voice_input)
                    break

    tts_engine.runAndWait()
