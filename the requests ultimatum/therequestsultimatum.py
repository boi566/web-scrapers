import requests as r
print("1 = life advice , 2 = cat fact , 3 = a url generartor for a random image of a dog")
try:
    pick = int(input("enter 1 , 2 or 3: "))
    while True:
        if pick == 1:
            advice = r.get('https://api.adviceslip.com/advice')
            if advice.status_code == 200:
                advicejsonparsed = advice.json()
                nesteddictbenefits = advicejsonparsed['slip']
                print("Life advice of the day:" , nesteddictbenefits['advice'])
                break
            else:
                print("error code:" , advice.status_code)
                break
        elif pick == 2:
            kitty = r.get('https://catfact.ninja/fact')
            if kitty.status_code == 200:
                kittyparse = kitty.json()
                print("Cat fact:" , kittyparse['fact'])
                break
            else:
                print("error code:" , kitty.status_code)
                break
        elif pick == 3:
            dawg = r.get('https://dog.ceo/api/breeds/image/random')
            if dawg.status_code == 200:
                whatthedawgdoin = dawg.json()
                print("Image to dog pic:" , whatthedawgdoin['message'])
                break
            else:
                print("error code:" , dawg.status_code)
                break
        else:
            print("not in index")
            break
except ValueError:
    print("invalid option")