import pyshorteners
url = input("Enter the URL:")
print("Short URL is:",pyshorteners.Shortener().tinyurl.short(url))