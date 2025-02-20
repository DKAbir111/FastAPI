from fastapi import FastAPI

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