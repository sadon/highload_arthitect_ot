import csv
import random
import json
import requests

interests = [" "]
rdays = lambda: random.randint(0,365)
ryear = lambda: random.randint(1920,2015)
from datetime import date, timedelta
headers = {
    'Content-Type': 'application/json',
    'accept': 'application/json'
}

with open('people.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)

    to_process = False
    for row in reader:
        print(row, reader.line_num)
        if to_process == False:
            if (row[0] == "Зубков Глеб") and (row[2] == "Кемерово"):
                to_process = True
                continue
            else:

                continue
        surname, name = row[0].split(" ")
        city = row[2]
        birthday = date.fromisoformat(f"{ryear()}-01-01") + timedelta(days=rdays())
        interests = "empty"
        if random.randint(0,1):
            male_sign = "true"
        else:
            male_sign= "false"
        email = f"some-{rdays()}-email{rdays()}-{birthday.isoformat()}@example.com"

        fields = f"""
              "email": "{email}",
              "password": "test-password",
              "first_name": "{name}",
              "second_name": "{surname}",
              "birthday": "{birthday.isoformat()}",
              "male_sign": {male_sign},
              "biography": "races, languages, python",
              "city": "{city}"
        """
        json_obj = json.loads("{"+fields+"}")

        try:

            response = requests.post(
                'http://127.0.0.1:8000/user/register',
                params={},
                headers=headers,
                data=json.dumps(json_obj).encode("utf-8"),
                timeout = 3
            )
            from time import sleep

            sleep(1)

            if response.status_code != 200:
                print(response.text)

        except requests.Timeout:
            # back off and retry
            #pass

            print("skipped")