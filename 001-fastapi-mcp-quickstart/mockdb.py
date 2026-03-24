from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int | None = Field(default=None)
    name: str
    email: str
    created_at: datetime | None = Field(default_factory=datetime.now)


user_next_id = 4
fake_users = [
    User(id=1, name="Alice", email="demo1@example.com", created_at=datetime.now()),
    User(id=2, name="Bob", email="demo2@example.com", created_at=datetime.now()),
    User(id=3, name="Charlie", email="demo3@example.com", created_at=datetime.now()),
]


def add_user(user: User):
    global user_next_id
    user.id = user_next_id
    user_next_id += 1
    fake_users.append(user)
    return user
