import requests

header={
    'Accept':'*/*',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjUwOTU3OSwianRpIjoiZDM1NDcyYjEtMTdiNy00Nzc5LWEyMjAtY2E4ODY1ODZhYmNhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDY1MDk1NzksImNzcmYiOiI0MjgyOTNmZi00MGE2LTQ5ZDYtYTNlOC1hMDg5ODljNmU0ZjUiLCJleHAiOjE3MDY1MTA0Nzl9.gpATfBKBYRjreH8wwOOMQcXOgteUrg9n1T-4O9XBKnE'
}
response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)

print("Before Update")
list=response.json()
for i in range(len(list)):
    print(list[i])



headerPut={
    'Accept':'*/*',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjUwOTU3OSwianRpIjoiZDM1NDcyYjEtMTdiNy00Nzc5LWEyMjAtY2E4ODY1ODZhYmNhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDY1MDk1NzksImNzcmYiOiI0MjgyOTNmZi00MGE2LTQ5ZDYtYTNlOC1hMDg5ODljNmU0ZjUiLCJleHAiOjE3MDY1MTA0Nzl9.gpATfBKBYRjreH8wwOOMQcXOgteUrg9n1T-4O9XBKnE'
}

putPayload={
        "address": "Kadri",
        "city": "Mangalore",
        "name": "Manoj",
        "salary": "44000"
}

responsePut= requests.put("http://127.0.0.1:5000/update_employee/5",headers=headerPut,json=putPayload)




print("After Update")
response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)
list=response.json()
for i in range(len(list)):
    print(list[i])


assert responsePut.status_code == 200 , f"expected response to have status code 200 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)