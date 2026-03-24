from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from mockdb import fake_users, add_user, User
from schemas import UserCreate

INCLUDE_MCPS = ["get_users", "create_user"]
app = FastAPI()


@app.get("/users", operation_id="get_users")
async def get_users():
    return fake_users


# 注册mcp工具：operation_id="create_user"
@app.post("/users", operation_id="create_user")
async def create_user(user_in: UserCreate):
    new_user = User(name=user_in.name, email=user_in.email)
    return add_user(new_user)


mcp = FastApiMCP(
    app,
    # 注册mcp工具
    include_operations=INCLUDE_MCPS,
)
mcp.mount_http()
