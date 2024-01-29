import unittest
import requests

class ApiTests(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/"
    VALID_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjUwOTU3OSwianRpIjoiZDM1NDcyYjEtMTdiNy00Nzc5LWEyMjAtY2E4ODY1ODZhYmNhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDY1MDk1NzksImNzcmYiOiI0MjgyOTNmZi00MGE2LTQ5ZDYtYTNlOC1hMDg5ODljNmU0ZjUiLCJleHAiOjE3MDY1MTA0Nzl9.gpATfBKBYRjreH8wwOOMQcXOgteUrg9n1T-4O9XBKnE"
    INVALID_TOKEN = "invalid_token"

    
    data={
        "name": "Karthik",
        "address": "kundapura-street",
        "city": "udupi",
        "salary": "344344"
    }

    # Positive test case 1: Ensure successful creation of data with valid token
    def test_create_data_successful(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        response = requests.post(self.BASE_URL+"create_employee", json=self.data,headers=headers)
        self.assertEqual(response.status_code,201)
        print("Positive Test 1 completed - POST Request")
        print("The response code is 201 OK")

    # Positive test case 2: Ensure successful creation with special characters
    def test_create_data_with_special_characters(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        data_to_post = {"name": "Special Characters !@#$%^&*()","address": "kundapura-street","city": "udupi","salary": "97765"}
        response = requests.post(self.BASE_URL+"create_employee", json=data_to_post,headers=headers)
        self.assertEqual(response.status_code,201)
        print("Positive Test 2 completed - POST Request")
        print("The response code is 201 OK")

       # Positive test case 4: Ensure proper handling of duplicate data
   
    def test_create_duplicate_data(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }

        data_to_post = {"name": "Karthik",
        "address": "kundapura-street",
        "city": "udupi",
        "salary": "97765"}

        response1 = requests.post(self.BASE_URL+"create_employee", json=data_to_post,headers=headers)
        response2 = requests.post(self.BASE_URL+"create_employee", json=data_to_post,headers=headers)

        self.assertEqual(response1.status_code, 201)
        print("Positive Test 3 completed - POST Request")
        print("1st POST Request")
        print("The response code is 201 OK")
        self.assertEqual(response2.status_code, 201)
        print("2nd POST request with same data(But id will change)")
        print("The response code is 201 OK")



    # Negative test case 1: Ensure successful creation of data with valid token
    def test_post_invalid_token(self):
        headers = {
            "Authorization": f"Bearer {self.INVALID_TOKEN}"
        }
        response = requests.post(self.BASE_URL+"create_employee", json=self.data,headers=headers)
        self.assertEqual(response.status_code,422)
        print("Negative Test 1 completed - POST Request")
        print("The response code is 422")

    # Negative test case 2: Missing attributes 
    def test_field_missing(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        data_to_post = {"name": "Karthik","city": "udupi","salary": "97765"}
        response = requests.post(self.BASE_URL+"create_employee", json=data_to_post,headers=headers)
        self.assertEqual(response.status_code,400)
        print("Negative Test 2 completed - POST Request")
        print("The response code is 400")
        print("Since fields are missing")

    # Negative test case 3: Incorrect attribute name
    def test_attr_name_error(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        data_to_post = {"name": "Karthik","city": "udupi", "address": "kundapura-street", "sal": "99845"}
        response = requests.post(self.BASE_URL+"create_employee", json=data_to_post,headers=headers)
        self.assertEqual(response.status_code,400)
        print("Negative Test 3 completed - POST Request")
        print("The response code is 400")
        print("Since data in field missing")

if __name__ == '__main__':
    tester=ApiTests()
    # tester.test_create_data_successful()
    # tester.test_create_data_with_special_characters()
    # tester.test_create_duplicate_data()

    tester.test_post_invalid_token()
    tester.test_field_missing()
    tester.test_attr_name_error()