import hashlib, os
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from main import db, User

app = Tk()

#variablen
userName = StringVar()
userPw = StringVar()

#Button Funktion
def magic():
	#Inputdaten werden gewonnen
	name = f'{userName.get()}'
	pw   = f'{userPw.get()}'

	#Fals Datenbanl noch nicht vorhanden ist wird diese erstellt
	if 'user.sqlite3' not in os.listdir():
		db.create_all()

	#Inputdaten werden gespeichert
	user = User(name, hashlib.sha256(bytes(pw, 'utf-8')).hexdigest())
	db.session.add(user)
	db.session.commit()

	tkinter.messagebox.showinfo('Info', f'User Daten wurden erfolgreich gespeichert\nName: {name} Passwort: {pw}')


#UserName erstellen
Label(app, text = 'User Name').pack()
ttk.Entry(app, textvariable=userName).pack()

Label(app, text = 'User Passwort').pack()
ttk.Entry(app, textvariable=userPw, show='*').pack()

Button(app, text = 'Bestätigen', command=magic).pack()



app.mainloop()