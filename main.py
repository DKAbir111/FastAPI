from fastapi import FastAPI, HTTPException

app=FastAPI()


users_db=[
        {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "age": 28
        },
        {
            "name": "Jane Smith",
            "email": "janesmith@example.com",
            "age": 32
        },
        {
            "name": "Alice Johnson",
            "email": "alicejohnson@example.com",
            "age": 25
        },
        {
            "name": "Michael Brown",
            "email": "michaelbrown@example.com",
            "age": 40
        }
    ]
@app.get('/')
async def root():
    return {"Server is running on http://127.0.0.1:8000"}


@app.get('/users')
async def get_users():
    return users_db


# single user fetch
@app.get("/users/{user_age}")
async def get_user(user_age: int):
    for user in users_db:
        if user["age"] == user_age:
            return user
        raise HTTPException(status_code=404, detail="User not found")
      