#jokes program
import requests

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
	"X-RapidAPI-Key": "c8cea74e0dmsh687468bf2aff37bp14d21ajsned508f535163",
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

data=response.json()
print(data)


a1=data['body'][0]['setup']
a2=data['body'][0]['punchline']
print('person: ',a1,'\n\n','joke: ',a2)

