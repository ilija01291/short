import pyshorteners

link = input("please insert the url:  ")

shortener=pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)