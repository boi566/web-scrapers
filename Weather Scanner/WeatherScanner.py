import requests as r
inp = input("Enter a city: ")
inpcaps = inp.title()
getinp = r.get(f"https://wttr.in/{inp}?format=3")
if getinp.status_code == 200:
    print(f"Current weather for {inpcaps}:")
    print(getinp.text)
elif getinp.status_code == 500:
    print(f"Error 500 , enter a vaild city name.")
else:
    print(f"Error: {getinp.status_code}")