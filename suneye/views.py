from django.shortcuts import render

def home(request):
	import json 
	import requests

	if request.method =="POST":
		zipcode = request.POST['zipcode']
		
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=9E799292-96B7-4034-9BEC-E688E5DE93F0")

		try:	
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error...."

		if api[0]['Category']['Name'] == "Good": 
	  		category_description = "Enjoy your outdoor activities."
	  		category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate": 
	  		category_description = "Good to go"	
	  		category_color = "moderate"
		elif api[0]['Category']['Name'] == "USG": 
	  		category_description = "Stay safe"
	  		category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy": 
	  		category_description = "Use Masks"
	  		category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy": 
	  		category_description = "Use K95 Masks"
	  		category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous": 
	  		category_description = "Stay Home"
	  		category_color = "hazardous"
			
				

		return render(request, 'home.html', {'api': api,
			'category_description': category_description,
			'category_color': category_color
			})


	else:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=9E799292-96B7-4034-9BEC-E688E5DE93F0")

		try:	
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error...."

		if api[0]['Category']['Name'] == "Good": 
	  		category_description = "Enjoy your outdoor activities."
	  		category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate": 
	  		category_description = "Good to go"	
	  		category_color = "moderate"
		elif api[0]['Category']['Name'] == "USG": 
	  		category_description = "Stay safe"
	  		category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy": 
	  		category_description = "Use Masks"
	  		category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy": 
	  		category_description = "Use K95 Masks"
	  		category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous": 
	  		category_description = "Stay Home"
	  		category_color = "hazardous"
			
				

		return render(request, 'home.html', {'api': api,
			'category_description': category_description,
			'category_color': category_color
			})

def about(request):
	return render(request, 'about.html', {})
	
