### API, HTTP, JSON & Co

#### Status Codes:

- 200 = OK
- 300 = not authenticated
- 400 = Not Found (front-end mistake)
- 500 = BAD BAD BAD server crash (back-end mistake)

/////////////////////////////////////////

Target URL = path + arguments 

- get requests always return a response
- in Python, using requests package, response can be received as a json file
```
response = requests.get(target_url)
response_dict = response.json()
```
- json file received as a plain txt Dictionary
- Dictionaries can be manipulated in Python :)