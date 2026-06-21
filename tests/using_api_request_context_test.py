import json


def test_get_api(api_request_context):
    """Showcase Playwright APIRequestContext for a GET request."""
    response = api_request_context.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        headers={"Accept": "application/json"}
    )

    assert response.status == 200
    response_data = response.json()
    print(response_data)
    assert response_data["id"] == 1
    assert "title" in response_data
    print("Test completed successfully")


def test_post_api(api_request_context):
    """Showcase Playwright APIRequestContext for a POST request."""
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

    response = api_request_context.post(
        "https://restful-booker.herokuapp.com/booking",
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        data=json.dumps(payload)
    )

    assert response.status == 200
    response_data = response.json()
    print(response_data)
    print("Test completed successfully")
