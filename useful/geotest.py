import requests
import json
from requests.structures import CaseInsensitiveDict

url = "https://api.geoapify.com/v1/geocode/search?text=38%20Upper%20Montagu%20Street%2C%20Westminster%20W1H%201LJ%2C%20United%20Kingdom&apiKey=7730a01760064316b225303a0192248a"

address = '205 Av. Bento Gonçalves, Porto Alegre, 90650002, Brazil'
address = address.replace(' ', '%20').replace(',', '%2C')

url_test = f"https://api.geoapify.com/v1/geocode/search?text={address}&apiKey=7730a01760064316b225303a0192248a" 

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(url_test, headers=headers)


with open('api_call.json', 'w', encoding='utf-8') as f:
    json.dump(resp.json(), f, ensure_ascii=False, indent=4)







