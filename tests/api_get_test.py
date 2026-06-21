import json


def test_get_request(playwright):
    request = playwright.request.new_context() # using this request variable we can now send request and get a response
    response = request.get("https://restful-booker.herokuapp.com/booking",
                           headers={"Accept": "application/json"}) # sending a get request to the specified URL
    
    assert response.status == 200 # asserting that the response status code is 200 (OK)
    json_data = response.json() # parsing the response body as JSON
    print(json_data) # printing the JSON data received from the response
    assert isinstance(json_data, list)
    assert json_data[0]["bookingid"] == 1 # asserting the first item's bookingid field is equal to 1

    request.dispose() # disposing of the request context to free up resources
    print("Test completed successfully")
    
def test_get_booking_request(playwright):
    request = playwright.request.new_context() # using this request variable we can now send request and get a response
    booking_payload = {
        "firstname": "Sally",
        "lastname": "Brown",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-02"},
        "additionalneeds": "Breakfast"
    }

    create_response = request.post(
        "https://restful-booker.herokuapp.com/booking",
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        data=json.dumps(booking_payload)
    )
    assert create_response.status == 200
    created_booking = create_response.json()
    booking_id = created_booking.get("bookingid")
    assert isinstance(booking_id, int)

    search_response = request.get(
        f"https://restful-booker.herokuapp.com/booking?firstname={booking_payload['firstname']}&lastname={booking_payload['lastname']}",
        headers={"Accept": "application/json"}
    )
    assert search_response.status == 200
    search_data = search_response.json()
    print(search_data)
    assert isinstance(search_data, list)
    assert any(item.get("bookingid") == booking_id for item in search_data), \
        f"Expected created booking {booking_id} to appear in search results"

    detail_response = request.get(
        f"https://restful-booker.herokuapp.com/booking/{booking_id}",
        headers={"Accept": "application/json"}
    )
    assert detail_response.status == 200
    booking_detail = detail_response.json()
    print(booking_detail)
    assert booking_detail["firstname"] == booking_payload["firstname"]
    assert booking_detail["lastname"] == booking_payload["lastname"]

    request.dispose() 
    print("Test completed successfully")