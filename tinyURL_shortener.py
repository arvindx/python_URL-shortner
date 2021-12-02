import pyshorteners

url = input("Enter your URL: ")
s = pyshorteners.Shortener().tinyurl.short(url)
print("Your new URL is: ", s)