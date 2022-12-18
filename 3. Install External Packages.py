import requests as REQUEST

"""
    Command to install external packages
        pip install packageName
    Example
        pip install requests
"""
# print(REQUEST.options)
# print(REQUEST.status_codes)

url = 'https://api.quotable.io/random'
response = REQUEST.get(url)
data = response.json()
print(data)
print(data['author'])