import requests

def random_quote():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        print(data["data"]["content"])
        print(f"- {data['data']['author']}")
    else:
        raise Exception("Error fetching quote")
        
try:
    random_quote()
except Exception as e:
    print(str(e))

    