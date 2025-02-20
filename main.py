from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Fake database
users_db = [
    {"id": 1, "name": "John Doe", "email": "johndoe@example.com", "age": 28},
    {"id": 2, "name": "Jane Smith", "email": "janesmith@example.com", "age": 32},
]

# Pydantic model for request body
class User(BaseModel):
    name: str
    email: str
    age: int

class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None


# ✅ GET all users
@app.get("/users", response_model=List[dict])
async def get_users():
    return users_db


# ✅ GET a single user by ID
@app.get("/users/{user_id}", response_model=dict)
async def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


# ✅ POST - Create a new user
@app.post("/users", response_model=dict)
async def create_user(user: User):
    new_user = {"id": len(users_db) + 1, **user.dict()}
    users_db.append(new_user)
    return new_user


# ✅ PUT - Update an entire user record
@app.put("/users/{user_id}", response_model=dict)
async def update_user(user_id: int, updated_user: User):
    for user in users_db:
        if user["id"] == user_id:
            user.update(updated_user.dict())
            return user
    raise HTTPException(status_code=404, detail="User not found")


# ✅ PATCH - Partially update a user record
@app.patch("/users/{user_id}", response_model=dict)
async def partial_update_user(user_id: int, user_update: UpdateUser):
    for user in users_db:
        if user["id"] == user_id:
            if user_update.name is not None:
                user["name"] = user_update.name
            if user_update.email is not None:
                user["email"] = user_update.email
            if user_update.age is not None:
                user["age"] = user_update.age
            return user
    raise HTTPException(status_code=404, detail="User not found")


# ✅ DELETE - Remove a user
@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            deleted_user = users_db.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User not found")
