import requests
import json
import time
import os


def fetch_data():
  api_key = "dd689b835b4658ddd5ee4e5a9d2ed8a6"
  lat = 44.389355 # Lattitude and Longitude of Barrie, Ontario
  lon = 79.690331
  api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

  headers = {
      "Authorization": f"Bearer {api_key}",
      "Content-Type": "application/json",
  }

  response = requests.get(api_url, headers=headers)

  if response.status_code == 200:
      return response.json()
  else:
      print(f"Failed to fetch data from the API. Status code: {response.status_code}")
      return None
def append_to_json(data):
  if data:
      output_directory = "final_project"
      os.makedirs(output_directory, exist_ok=True)

      # if the directory called data exist then appending data to the JSON file
      with open(os.path.join(output_directory, "data.json"), "a") as json_file:
          json.dump(data, json_file)
          json_file.write('\n')
          print("Data is successfully appended to the JSON file.")


while True:
  data = fetch_data()
  append_to_json(data)
  time.sleep(5)
