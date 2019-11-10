import requests

def main():
	 email = input("Enter email: ")
	 response = requests.get("https://haveibeenpwned.com/api/v3/breach/"+ email + "?includeUnverified=true")
	 #self.header = {'User-Agent' : self.agent, "hibp-api-key": self.key}
	 #requests.get(url, headers=self.header)
	 #print(response.status_code)
	 status = int(response.status_code)
	 if (status == 404):
			print("-"*60+"\n")
			print("The email " + email + " has not been pwned!\n")
			print("-" * 60)
	 elif (status == 200):
			print("-" * 60+"\n")
			print("The email " + email+ " has been pwned! \n")
			print("-" * 60)
			json = str(response.json()).split()
			a = json[json.index("'AddedDate':")]

			d = []

			domain= json.index("'Description':") + 1
			logo = json.index("'LogoPath':")
			cont=0

			while domain < logo:
				 cont = cont + 1
				 a= json[json.index("'Description':") + cont] + " "
				 d.append(a)
				 domain = domain + 1

			d= ''.join(d)



	  ###Imprimir

			print("{\n")
			print(json[json.index("'AddedDate':")] + json[json.index("'AddedDate':")+1])
			print(json[json.index("'BreachDate':")] + json[json.index("'BreachDate':") + 1])
			print(json[json.index("'Description':")] + d)
			print(json[json.index("'Domain':")] + json[json.index("'Domain':") + 1])
			print(json[json.index("'IsRetired':")] + json[json.index("'IsRetired':") + 1])
			print(json[json.index("'IsSensitive':")] + json[json.index("'IsSensitive':") + 1])
			print(json[json.index("'IsVerified':")] + json[json.index("'IsVerified':") + 1])
			print(json[json.index("'LogoPath':")] + json[json.index("'LogoPath':") + 1])
			print("'Name':" + json[json.index("{'Name':") + 1])
			print(json[json.index("'PwnCount':")] + json[json.index("'PwnCount':") + 1])
			print(json[json.index("'Title':")] + json[json.index("'Title':") + 1] + "\n")
			print("}")


if __name__ == '__main__':
	 main()
