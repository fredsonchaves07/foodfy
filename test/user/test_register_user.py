def test_valid_post_request(client):
    assert client.post("/api/v1/user").status_code == 201, "The request is not valid"
