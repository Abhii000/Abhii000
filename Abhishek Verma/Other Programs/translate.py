import requests,os,time

url = "https://text-translator2.p.rapidapi.com/translate"
trans=str(input("Translate: "))
payload = {
	"source_language": "en",
	"target_language": "hi",
	"text": trans
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "c8cea74e0dmsh687468bf2aff37bp14d21ajsned508f535163",
	"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}
response = requests.post(url, data=payload, headers=headers)
data=response.json()
translated_words=data['data']['translatedText']
print('Translated = ',translated_words)
with open('translated.txt', 'w',encoding='utf-8') as f:
	f.write(translated_words)
	f.close()
loc_txt=os.getcwd()
print(loc_txt)








    
