import requests

result = requests.get('localhost:8000')


print(result.status_code)
print(result.content)