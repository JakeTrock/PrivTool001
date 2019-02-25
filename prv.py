import io
import stem.process
from stem.util import term
import tkinter as tk
from tkinter import Tk
from tkinter import Button
from tkinter import OptionMenu
from tkinter import StringVar
from tkinter import mainloop
SOCKS_PORT = 7000
#https://stackoverflow.com/questions/5486725/how-to-execute-a-command-prompt-command-from-python
#set HTTP_PROXY=http://proxy_userid:proxy_password@proxy_ip:proxy_port
tor_country = '{??}'
natons_engnames = ["AUTO", "ASCENSION ISLAND", "AFGHANISTAN", "ALAND", "ALBANIA", "ALGERIA", "ANDORRA", "ANGOLA", "ANGUILLA", "ANTARCTICA", "ANTIGUAANDBARBUDA", "ARGENTINAREPUBLIC", "ARMENIA", "ARUBA", "AUSTRALIA", "AUSTRIA", "AZERBAIJAN", "BAHAMAS", "BAHRAIN", "BANGLADESH", "BARBADOS", "BELARUS", "BELGIUM", "BELIZE", "BENIN", "BERMUDA", "BHUTAN", "BOLIVIA", "BOSNIAANDHERZEGOVINA", "BOTSWANA", "BOUVETISLAND", "BRAZIL", "BRITISHINDIANOCEANTERR", "BRITISHVIRGINISLANDS", "BRUNEIDARUSSALAM", "BULGARIA", "BURKINAFASO", "BURUNDI", "CAMBODIA", "CAMEROON", "CANADA", "CAPEVERDE", "CAYMANISLANDS", "CENTRALAFRICANREPUBLIC", "CHAD", "CHILE", "PEOPLE'S REPUBLIC OF CHINA", "CHRISTMASISLANDS", "COCOSISLANDS", "COLOMBIA", "COMORAS", "CONGO", "CONGO(DEMOCRATIC REPUBLIC)", "COOKISLANDS", "COSTARICA", "COTEDIVOIRE", "CROATIA", "CUBA", "CYPRUS", "CZECHREPUBLIC", "DENMARK", "DJIBOUTI", "DOMINICA", "DOMINICANREPUBLIC", "EASTTIMOR", "ECUADOR", "EGYPT", "ELSALVADOR", "EQUATORIALGUINEA", "ESTONIA", "ETHIOPIA", "FALKLANDISLANDS", "FAROEISLANDS", "FIJI", "FINLAND", "FRANCE", "FRANCE METROPOLITAN", "FRENCH GUIANA", "FRENCH POLYNESIA", "FRENCH SOUTHERN TERRITORIES", "GABON", "GAMBIA", "GEORGIA", "GERMANY", "GHANA", "GIBRALTER", "GREECE", "GREENLAND", "GRENADA", "GUADELOUPE", "GUAM", "GUATEMALA", "GUINEA", "GUINEA-BISSAU", "GUYANA", "HAITI", "HEARD & MCDONALD ISLAND", "HONDURAS", "HONGKONG", "HUNGARY", "ICELAND", "INDIA", "INDONESIA", "IRAN", "IRAQ", "IRELAND", "ISLE OF MAN", "ISRAEL", "ITALY", "JAMAICA", "JAPAN", "JORDAN", "KAZAKHSTAN", "KENYA", "KIRIBATI", "KOREA, EM. PEOPLES REP OF", "KOREA, EPUBLIC OF", "KUWAIT", "KYRGYZSTAN", "LAO, PEOPLE'S DEM. REPUBLIC", "LATVIA", "LEBANON", "LESOTHO", "LIBERIA", "LIBYA NARABJAMAHIRIYA", "LIECHTENSTEIN", "LITHUANIA", "LUXEMBOURG", "MACAO", "MACEDONIA", "MADAGASCAR", "MALAWI", "MALAYSIA", "MALDIVES", "MALI", "MALTA", "MARSHALL ISLANDS", "MARTINIQUE", "MAURITANIA", "MAURITIUS", "MAYOTTE", "MEXICO", "MICRONESIA", "MOLDAVA REPUBLIC OF", "MONACO", "MONGOLIA", "MONTENEGRO", "MONTSERRAT", "MOROCCO", "MOZAMBIQUE", "MYANMAR", "NAMIBIA", "NAURU", "NEPAL", "NETHERLANDS ANTILLES", "NETHERLANDS, HE", "NEW CALEDONIA", "NEW ZEALAND", "NICARAGUA", "NIGER", "NIGERIA", "NIUE", "NORFOLK ISLAND", "NORTHERN MARIANA ISLANDS", "NORWAY", "OMAN", "PAKISTAN", "PALAU", "PALESTINE", "PANAMA", "PAPUA NEW GUINEA", "PARAGUAY", "PERU", "PHILIPPINES(REPUBLIC OF THE)", "PITCAIRN", "POLAND", "PORTUGAL", "PUERTORICO", "QATAR", "REUNION", "ROMANIA", "RUSSIAN FEDERATION", "RWANDA", "SAMOA", "SANMARINO", "SAOTOME/PRINCIPE", "SAUDIARABIA", "SCOTLAND", "SENEGAL", "SERBIA", "SEYCHELLES", "SIERRA LEONE", "SINGAPORE", "SLOVAKIA", "SLOVENIA", "SOLOMON ISLANDS", "SOMALIA", "SOMOA, ILBERT, LLICE ISLANDS", "SOUTH AFRICA", "SOUTH GEORGIA, OUTH SANDWICH ISLANDS", "RUSSIA", "SPAIN", "SRILANKA", "ST.HELENA", "ST.KITTSANDNEVIS", "ST.LUCIA", "ST.PIERRE AND MIQUELON", "ST.VINCENT & THE GRENADINES", "SUDAN", "SURINAME", "SVALBARD AND JANMAYEN", "SWAZILAND", "SWEDEN", "SWITZERLAND", "SYRIAN ARAB REPUBLIC", "TAIWAN", "TAJIKISTAN", "TANZANIA, NITED REPUBLIC OF", "THAILAND", "TOGO", "TOKELAU", "TONGA", "TRINIDAD AND TOBAGO", "TUNISIA", "TURKEY", "TURKMENISTAN", "TURKS AND CACOS ISLANDS", "TUVALU", "UGANDA", "UKRAINE", "UNITED ARAB EMIRATES", "UNITED KINGDOM(no new registrations)", "UNITED KINGDOM", "UNITED STATES", "UNITED STATES MINOROUTL.IS.", "URUGUAY", "UZBEKISTAN", "VANUATU", "VATICAN CITY STATE", "VENEZUELA", "VIETNAM", "VIRGINISLANDS (USA)", "WALLIS AND FUTUNA ISLANDS", "WESTERN SAHARA", "YEMEN", "ZAMBIA", "ZIMBABWE"]
natons_prognames = ["??", "ac", "af", "ax", "al", "dz", "ad", "ao", "ai", "aq", "ag", "ar", "am", "aw", "au", "at", "az", "bs", "bh", "bd", "bb", "by", "be", "bz", "bj", "bm", "bt", "bo", "ba", "bw", "bv", "br", "io", "vg", "bn", "bg", "bf", "bi", "kh", "cm", "ca", "cv", "ky", "cf", "td", "cl", "cn", "cx", "cc", "co", "km", "cg", "cd", "ck", "cr", "ci", "hr", "cu", "cy", "cz", "dk", "dj", "dm", "do", "tp", "ec", "eg", "sv", "gq", "ee", "et", "fk", "fo", "fj", "fi", "fr", "fx", "gf", "pf", "tf", "ga", "gm", "ge", "de", "gh", "gi", "gr", "gl", "gd", "gp", "gu", "gt", "gn", "gw", "gy", "ht", "hm", "hn", "hk", "hu", "is", "in", "id", "ir", "iq", "ie", "im", "il", "it", "jm", "jp", "jo", "kz", "ke", "ki", "kp", "kr", "kw", "kg", "la", "lv", "lb", "ls", "lr", "ly", "li", "lt", "lu", "mo", "mk", "mg", "mw", "my", "mv", "ml", "mt", "mh", "mq", "mr", "mu", "yt", "mx", "fm", "md", "mc", "mn", "me", "ms", "ma", "mz", "mm", "na", "nr", "np", "an", "nl", "nc", "nz", "ni", "ne", "ng", "nu", "nf", "mp", "no", "om", "pk", "pw", "ps", "pa", "pg", "py", "pe", "ph", "pn", "pl", "pt", "pr", "qa", "re", "ro", "ru", "rw", "ws", "sm", "st", "sa", "uk", "sn", "rs", "sc", "sl", "sg", "sk", "si", "sb", "so", "as", "za", "gs", "su", "es", "lk", "sh", "kn", "lc", "pm", "vc", "sd", "sr", "sj", "sz", "se", "ch", "sy", "tw", "tj", "tz", "th", "tg", "tk", "to", "tt", "tn", "tr", "tm", "tc", "tv", "ug", "ua", "ae", "gb", "uk", "us", "um", "uy", "uz", "vu", "va", "ve", "vn", "vi", "wf", "eh", "ye", "zm", "zw"]

master = Tk()
country = StringVar(master)
country.set(natons_engnames[0])

countrySelect = OptionMenu(master, country, *natons_engnames)
countrySelect.pack()

def connect():
	tor_country = nations_prognames[nations_engnames.index(country.get())]
	def query(url):
  
    output = io.BytesIO()

    def print_bootstrap_lines(line):
        if "Bootstrapped " in line:
            print(term.format(line, term.Color.BLUE))


    print(term.format("Starting Tor:\n", term.Attr.BOLD))

    tor_process = stem.process.launch_tor_with_config(
        config = {
            'SocksPort': str(SOCKS_PORT),
            'ExitNodes': tor_country,
        },
        init_msg_handler = print_bootstrap_lines,
    )
        
def disconnect():
    tor_process.kill()
    
connectButton = Button(master, text="Connect", command=connect)
connectButton.pack()
disconnectButton = Button(master, text="Disconnect", command=disconnect)
disconnectButton.pack()
mainloop()
