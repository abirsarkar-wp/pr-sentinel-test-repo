def connect_database():
    database_url = "postgresql://localhost:5432/prsentinel"
    return database_url


def get_user(user_id):
    return {"id": user_id}
