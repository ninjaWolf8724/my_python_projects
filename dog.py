import requests
url = "https://random.dog/woof"
dog = requests.get(url).text
url2 = "random.dog" + "/" + dog
print("Go to %s to view the cute doggo." %url2)
