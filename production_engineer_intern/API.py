# -*- coding: utf-8 -*-

# MODULE NECESSARY FOR API USAGE
import requests


class Weather_API:
# =============================================================================
#     THIS CLASS DEFINES HOW TO REQUEST INFORMATION FROM THE API. 
#     
#     OPENWEATHERMAP.ORG IS USED AS THE DATABASE.
# =============================================================================
    
    def get_weather(api_key, city):
# =============================================================================
#         THIS METHOD DEFINES HOW THE MODULE RETRIEVES WEATHER INFORMATION ABOUT A GIVEN 
#         CITY FROM OPENWEATHERMAP.ORG
#         
#         THE ARGUMENTS MUST BE PASSED AS STRINGS. 
# =============================================================================
        
        # THE URL FOR THE API, WRITTEN AS AN f-STRING SO THAT THE city AND api_key 
        # VALUES ARE AUTOMATICALLY ADDED TO THE URL
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        
        # CREATES AN OBJECT TO MAKE REQUESTS. INFORMATION IS RETURNED IN .json FORMAT
        response = requests.get(url).json()
        
        # CREATES AN EMPTY LIST TO HOLD WEATHER INFORMATION
        weatherData = []
        
        # APPENDS THE INFORMATION TO THE LIST
        weatherData.append((response['weather'][0]['description']).capitalize())
        weatherData.append(float(response['main']['temp']) - 273.15)
        
        # RETURNS THE LIST
        return weatherData
        

