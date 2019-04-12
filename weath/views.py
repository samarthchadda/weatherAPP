# import requests
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import City
# from .forms import CityForm




# def index(request):
	
# 	#url for the api
# 	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=51681fd29f82ee55eb7e16c51386c137'
# 	# my api key =  # 51681fd29f82ee55eb7e16c51386c137

# 	city = 'Jaipur'


# 	#FOR SUBMIT BUTTON
# 	if request.method == 'POST':

# 		# print(request.POST)
# 		form = CityForm(request.POST)
#         form.save()
		
			



# 	# form = CityForm()
# 	form = CityForm()



# 	cities = City.objects.all()


# 	weather_data = []

# 	for city in cities:

# 		r=requests.get(url.format(city)).json() #.json()  will convert the result of the request into JSON object 
# 		# print(r.text)   #remove .json() from above to run it


# 		city_weather = {

# 			'city': city.name,
# 			'temperature': r['main']['temp'] ,
# 			'description': r['weather'][0]['description'],
# 			'icon': r['weather'][0]['icon'],

# 		}

# 		weather_data.append(city_weather)



# 	# print(city_weather)
# 	print(weather_data)

# 	context = { 'weather_data' : weather_data, 'form' : form }



# 	return render(request,'weath/weather.html',context)
# 	# return HttpResponse("Hello world")






import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=51681fd29f82ee55eb7e16c51386c137'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()


    # city = "Jaipur"

    form = CityForm()

    cities = City.objects.all()
    print(cities)

    weather_data = []

    for city in cities:


	    r = requests.get(url.format(city)).json()

	    city_weather = {

	    	'city': city.name,
	    	'temperature': r['main']['temp'] ,
			'description': r['weather'][0]['description'],
			'icon': r['weather'][0]['icon'],

	    }

	    weather_data.append(city_weather)
        # print(r.text)
    # print(r['main']['temp'])

    # for city in cities:
    	# r1 = requests.get(url.format(city)).json()
        # print(r.text)
    	# print(r['main']['temp'])

  #   	city_weather = {

		# 	'city': city.name,
		# 	'temperature': r['main']['temp'] ,
		# 	'description': r['weather'][0]['description'],
		# 	'icon': r['weather'][0]['icon'],

		# }

    	

    	# weather_data.append(city_weather)



    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weath/weather.html', context)
    # return render(request, 'weath/weather.html')
    
