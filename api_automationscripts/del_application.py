import requests

header={
    'Accept':'*/*',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjUwNzc4OCwianRpIjoiMzFhNWQ1MGQtNTdjNy00ZDE3LWI2ZjEtZWYxMjY3NGY5NDNjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDY1MDc3ODgsImNzcmYiOiJkNWE4OGY3Yi0yYzE2LTRhMjgtODRlMi01YTBjNGYzZmExZGIiLCJleHAiOjE3MDY1MDg2ODh9.OMxeZ7au_NugPgTpBDRO9PEXow51Hh6MK2Ov0lQUuEc'
}

response = requests.get("http://127.0.0.1:5000/list_employees", headers=header)
assert response.status_code==200 , f"expected response to have status code 200 but got {response.status_code}"

print("Initial GET Request and the Status Code is",response.status_code)
list=response.json()
for i in range(len(list)):
    print(list[i])



headDel={
    'Accept': '*/*',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjUwNzc4OCwianRpIjoiMzFhNWQ1MGQtNTdjNy00ZDE3LWI2ZjEtZWYxMjY3NGY5NDNjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDY1MDc3ODgsImNzcmYiOiJkNWE4OGY3Yi0yYzE2LTRhMjgtODRlMi01YTBjNGYzZmExZGIiLCJleHAiOjE3MDY1MDg2ODh9.OMxeZ7au_NugPgTpBDRO9PEXow51Hh6MK2Ov0lQUuEc'

}

responseDel= requests.delete("http://127.0.0.1:5000/employee/5",headers=headDel)
assert response.status_code==200 , f"expected response to have status code 200 but got {response.status_code}"
print("Deleted Successfull with response code",responseDel.status_code)



print("Data after delete")
response = requests.get("http://127.0.0.1:5000/list_employees", headers=header)
list=response.json()
for i in range(len(list)):
    print(list[i])
