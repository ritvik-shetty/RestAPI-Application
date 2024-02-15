import requests

header={
    'Accept':'*/*',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNzk3OTEwNSwianRpIjoiYTRmNzg4NjktNjUxYy00NDI2LWJiYzAtNTA1MGViMzExM2M0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDc5NzkxMDUsImNzcmYiOiJmMWUyMmNkNy04MmQ2LTRkOTctYWEzMi1kNjFhNGIwMjczYTAiLCJleHAiOjE3MDc5ODAwMDV9.BfyWHhsHwABjsyN0EkLhZNEv8IO1PphMQPhHviIu4L4'
}
response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)

assert response.status_code==200 , f"expected response to have status code 200 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)

list=response.json()
for i in range(len(list)):
    print(list[i])
