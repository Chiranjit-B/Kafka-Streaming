import uuid
from datetime import datetime
# from airflow import DAG
# from airflow.operators.python import PythonOperator

# Airflow setup (commented out for now since not using DAG)
# default_args = {
#     'owner': 'chiranjitB',
#     'start_date': datetime(2025, 4, 15, 13, 00)
# }

# with DAG('user_automation',
#          default_args=default_args,
#          schedule_interval='@daily',
#          catchup=False) as dag:
    
#     streaming_task = PythonOperator(
#         task_id='stream_data_from_api',
#         python_callable= stream_data
#     )

def get_data():
    import requests
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    return res['results'][0]

def format_data(res):
    data = {}
    location = res['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{location['street']['number']} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']
    return data

def stream_data():
    import json
    from kafka import KafkaProducer
    
    
    
    res = get_data()
    res = format_data(res)
    print(json.dumps(res, indent=3))




stream_data()
