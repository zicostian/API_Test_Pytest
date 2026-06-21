from playwright.sync_api import sync_playwright
import json

def test_get_api():
    with sync_playwright() as p:
        request = p.request.new_context()  # using this request variable we can now send request and get a response
        response = request.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            headers={"Accept": "application/json"}
        )

        assert response.status == 200  # asserting that the response status code is 200 (OK)
        response_data = response.json()
        print(response_data)  # printing the JSON data received from the response
        assert response_data["id"] == 1
        assert "title" in response_data
        request.dispose()  # disposing of the request context to free up resources
        print("Test completed successfully")


def test_post_api():
    with sync_playwright() as p:
        request = p.request.new_context()  # using this request variable we can now send request and get a response
        payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        response = request.post(
            "https://restful-booker.herokuapp.com/booking",
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            data=json.dumps(payload)
        )

        assert response.status == 200
        response_data = response.json()
        print(response_data)
        request.dispose()