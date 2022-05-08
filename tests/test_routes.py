def test_get_all_books_with_no_records(client):
    response = client.get("/books")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_book_by_id(client):
    response = client.get("/books/1")
    response_body = response.get_json()

    