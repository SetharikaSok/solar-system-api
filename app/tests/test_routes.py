def test_read_all_planets_returns_empty_list(client):
    

    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_read_planet_by_id(client, make_two_planet):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "jupiter",
        "color": "copper",
        "description": "gas giant with no solid surface"
    }

def test_create_planet(client):
    response = client.post("/planets", json={
        "name": "venus",
        "color": "orange",
        "description": "hottest planet in solar system"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "planet venus succesfully created!"
    
# def test_read_planet_by_name(client, make_two_planet):
#     response = client.get("/planets/uranus")
#     response_body = response.get_json()

#     assert response.status_code == 200
#     assert response_body == {
#             "name": "uranus",
#             "color": "baby blue",
#             "description": "mostly ice"
#     }
