import tkinter as tk
from tkinter import Tk
from tkinter import Button
from tkinter import OptionMenu
from tkinter import StringVar
from tkinter import mainloop

COUNTRIES = [
	"Auto",
	"United States",
	"China",
	"Russia"
]

master = Tk()
country = StringVar(master)
country.set(COUNTRIES[0])

countrySelect = OptionMenu(master, country, *COUNTRIES)
countrySelect.pack()

def connect():
	print("selected " + country.get())

connectButton = Button(master, text="Connect", command=connect)
connectButton.pack()

mainloop()
