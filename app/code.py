import requests

brand_map = {0:"Audi", 1:"Hyundai Creta", 2:"Mahindra Scorpio", 3:"Rolls Royce",
4:"Swift", 5:"Tata Safari", 6:"Toyota Innova"}


def predict_car(model,img): 
    url = "http://172.17.0.2/api/genhog"
    
    
    response = requests.get(url, json={"img_data":img})
    if response.status_code == 200:
        try:
            response_data = response.json()
            data_list = [response_data[key] for key in response_data]
            car = model.predict(data_list)
            result_brand=brand_map.get(car[0])

            return result_brand
        except requests.exceptions.JSONDecodeError as e:
            print("JSON Decode Error:", e)
    else:
        print("API Request Error. Status Code:", response.status_code)
        return None
