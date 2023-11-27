#

import requests
from datetime import datetime
import os



nutrition_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"


spreadsheet_endpoint=("your google spreadsheet_endpoint")



exercise_name=input("tell me which exercise yo did: ")

APP_ID= ("Your nutritionix.com APP_ID")
API_KEY=("Your nutritionix.com API_KEY")	
 

# -------------------requests data from nutrition-----------------


user_params = {
  
  "query":exercise_name, # the name of the exercise we want to give to nutritionix.com to get data about it 
 
}


header={
  
  "x-app-id": APP_ID,
  "x-app-key": API_KEY,
  
}

response=requests.post(url=nutrition_endpoint,json=user_params,headers=header)
result = response.json()




# -------------------adding a new row to the spread sheet-----------------



today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# here we convert the todays time into this form yyyymmdd to be suitable with api parameters requerments .


for exercise in result["exercises"]: # here the result is a dictionary we get from nutrition according to a specific exercise we type and anlyzed by it , that dictionary contains a key called exercises , 
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    header={
      "Authorization":  (" yor google sheet Authorization")
    }
# here the key word exercise is a nested dictionary inside another dictionary , so it have keys , so we deal with dictionary as a normal dictionary we call the key as we want , from that key is the name , duration , calories , which have values . here we give parameters to the sheety api , and he will understand automatically were to put the date , the exercise and other ., the parameters shoul be all in a camel case , so if you type : mondayworkout , it should become :  mondayWorkout


# In addition to that :
  
  # Sheety expects your record to be nested in a singular root property named after your sheet. For example if your endpoint is named emails, nest your record in a property called email , so here our end point or the sheet name is called workout(s) , so according to sheety , the parameters should be nested inside a dictionary called by the root of the sheet name , or the singular form of the sheet name which is the workout .

    sheet_response = requests.post(url=spreadsheet_endpoint, json=sheet_inputs, headers=header)

    print(sheet_response.text)

# be very carefull at the first , you have to make a copy of trhe spread sheet bcz the first version we cannot edit it ! 





