import urllib.request
import urllib.error

url = "https://islahofficial.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"}

try:
    request = urllib.request.Request(url, headers=headers)
    webpage = urllib.request.urlopen(request)

except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code)

except urllib.error.URLError as e:
    print("Connection failed:", e.reason)

else:
    for line in webpage:
        print(line.decode("utf-8"))