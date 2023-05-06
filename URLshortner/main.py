import pyshorteners

obj = pyshorteners.Shortener()
url = input("Enter the url you want to shorten")
short_url= obj.tinyurl.short(url)
print("The shortened url is "+short_url)
