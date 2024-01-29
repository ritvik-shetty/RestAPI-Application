import requests

header={
    'Accept':'*/*',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjUwOTU3OSwianRpIjoiZDM1NDcyYjEtMTdiNy00Nzc5LWEyMjAtY2E4ODY1ODZhYmNhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDY1MDk1NzksImNzcmYiOiI0MjgyOTNmZi00MGE2LTQ5ZDYtYTNlOC1hMDg5ODljNmU0ZjUiLCJleHAiOjE3MDY1MTA0Nzl9.gpATfBKBYRjreH8wwOOMQcXOgteUrg9n1T-4O9XBKnE'
}
response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)

assert response.status_code==200 , f"expected response to have status code 200 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)

list=response.json()
for i in range(len(list)):
    print(list[i])
