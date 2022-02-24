import requests


ROSREESTR_URL = "https://rosreestr.gov.ru/api/online/fir_object/"

def get_old_price(number):
    new_number = number.replace(':00', ":").replace(":0", "")
    print(new_number)
    url = ROSREESTR_URL + new_number
    r = requests.get(url)
    print(r)
    if r.status_code == 200:
        rosreestr_data = r.json()
        print(rosreestr_data)
        try:
            old_price = rosreestr_data["parcelData"]["cadCost"]
        except:
            old_price = "Unknown"
        return old_price
    return "Unknown"