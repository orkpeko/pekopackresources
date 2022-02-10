from tkinter import *
import os
import shutil
import json
import requests
import wget
import ctypes, sys
import zipfile

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

# TK Window define
window = Tk()
window.geometry('853x480')
window.title("PekoPack Updater")
window.config(bg=rgb_hack((0,0,0)))

def api_rqm():
    a=requests.get("https://api.orkpeko.xyz/api/v1/updates").json()["update_payload"]["mods"][0]
    return a
def api_rqu():
    a=requests.get("https://api.orkpeko.xyz/api/v1/updates").json()["update_payload"]["updater"][0]
    return a
def api_rqt():
    a=requests.get("https://api.orkpeko.xyz/api/v1/updates").json()["update_payload"]["texture"][0]
    return a


def clickdownloadmods():
    input("Press enter in the console to confirm, as this will delete everything in your mods folder.")
    folder = f"{diren.get()}\\mods"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    print('Sending request to cdn.orkpeko.xyz for the mod pack...')
    r = requests.get('https://cdn.orkpeko.xyz/r/latestm.zip', allow_redirects=True)
    open(f"{diren.get()}\\mods\\modste.zip", 'wb').write(r.content)
    with zipfile.ZipFile(f"{diren.get()}\\mods\\modste.zip", 'r') as zip_ref:
        zip_ref.extractall(f"{diren.get()}\\mods",)
    print("Done.")


def clickdownloadtexture():
    print('Sending request to cdn.orkpeko.xyz for the texture pack..')
    r = requests.get('https://cdn.orkpeko.xyz/r/latestt.zip', allow_redirects=True)
    open(f"{diren.get()}\\resourcepacks\\pekotweaksnew.zip", 'wb').write(r.content)
    print("Done.")

diren = Entry(window, text="Download Modpack", width=70)
diren.place(rely=0., relx=0.5, x=0, y=0, anchor=N)

labeluu = Label(window, text=f"Updater Updates:\n{api_rqu()}.", width=30, fg="#FFFFFF", bg="#000000")
labeluu.place(rely=0.05, relx=0.5, x=0, y=0, anchor=N)

buttonm = Button(window, text="Download Modpack", width=30, command=clickdownloadmods)
buttonm.place(rely=0.7, relx=0.3, x=0, y=0, anchor=N)

labelmu = Label(window, text=f"Updates:\n{api_rqm()}.", width=30, fg="#FFFFFF", bg="#000000")
labelmu.place(rely=0.3, relx=0.3, x=0, y=0, anchor=N)

buttont = Button(window, text="Download Texturepack", width=30, command=clickdownloadtexture)
buttont.place(rely=0.7, relx=0.7, x=0, y=0, anchor=N)

labeltu = Label(window, text=f"Updates:\n{api_rqt()}.", width=30, fg="#FFFFFF", bg="#000000")
labeltu.place(rely=0.3, relx=0.7, x=0, y=0, anchor=N)

diren.delete(0, "end")
diren.insert(0, f"{os.environ['USERPROFILE']}\\AppData\\Roaming\\.minecraft")

txtpro = Label(window, text="github.com/orkpeko")
txtpro.place(rely=1, relx=1, x=0, y=0, anchor=SE)

window.mainloop()
