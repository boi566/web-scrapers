import requests as r
we = r.get("https://official-joke-api.appspot.com/random_joke")
if we.status_code == 200:
    we2 = we.json()
    print(f"{we2['setup']}\n{we2['punchline']}")
else:
    print(f"error code: {we.status_code}")