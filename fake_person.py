import fake_useragent
import requests


# test file, here i try to solve the connect problem
# when i get with url without headers, received a forbidden error
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Referer': 'http://porno365.lol/'
}
url = ""
response = requests.get(url, headers=headers)
print(response.text)