import unittest
import requests

class ApiTests(unittest.TestCase):
    URL="http://127.0.0.1:5000/remove_employee"
    VALID_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjUwOTU3OSwianRpIjoiZDM1NDcyYjEtMTdiNy00Nzc5LWEyMjAtY2E4ODY1ODZhYmNhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDY1MDk1NzksImNzcmYiOiI0MjgyOTNmZi00MGE2LTQ5ZDYtYTNlOC1hMDg5ODljNmU0ZjUiLCJleHAiOjE3MDY1MTA0Nzl9.gpATfBKBYRjreH8wwOOMQcXOgteUrg9n1T-4O9XBKnE"
    INVALID_TOKEN = "invalid_token"

    # Positive test case to delete an employee
    def test_delete_existing_item(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        response=requests.delete(self.URL+'/6',headers=headers)
        self.assertEqual(response.status_code,200)
        
        print("Positive test 1 completed- DELETE Request")
        print("The response code is 200 OK")
        print("-----------------------------------------")



    # Negative test case to delete an employee
    def test_delete_with_improper_token(self):
        headers = {
            "Authorization": f"Bearer {self.INVALID_TOKEN}"
        }
        response=requests.delete(self.URL+'/10',headers=headers)
        self.assertEqual(response.status_code,422)
        
        print("Negative test 1 completed- DELETE Request")
        print("The response code is 422")
        print("-----------------------------------------")    

    
    # Negative test case for non-existent data
    def test_delete_non_existent_item(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        response=requests.delete(self.URL+'/99999',headers=headers)
        self.assertEqual(response.status_code,404)
        
        print("Negative test 2 completed- DELETE Request")
        print("The response code is 404")
        print("-----------------------------------------")


        # Negative test case for invalid request methods
    def test_invalid_method(self):
        headers = {
            "Authorization": f"Bearer {self.INVALID_TOKEN}"
        }
        response = requests.put(self.URL,headers=headers)
        self.assertEqual(response.status_code, 404)
        print("Negative Test 2 completed - DELETE Request")
        print("The response code is 404 ")
        print("The requested method is invalid")
        print("--------------------------------------") 

if __name__ == '__main__':
    tester=ApiTests()
    # tester.test_delete_existing_item()


    tester.test_delete_with_improper_token()
    tester.test_delete_non_existent_item()
    tester.test_invalid_method()