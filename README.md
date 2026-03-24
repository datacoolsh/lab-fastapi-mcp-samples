# lab-fastapi-mcp-samples

FastAPI + fastapi-mcp 示例合集，演示如何将 FastAPI 路由自动暴露为 MCP 工具。

## 如何使用

### 启动mcp server
1. 安装依赖包：`uv sync`
2. `cd ./001-fastapi-mcp-quickstart`
3. 启动服务：`fastapi dev --port 8000`

### 安装mcpserver
1. 在项目的跟路径下创建 `.mcp.json`
2. 在 `./claude/settings.local.json` 文件中添加启用mcpservername的配置
3. 使用命令行检查 mcp是否添加正确：`claude mcp get fastapimcp`
4. 打开claude 对话框
5. 使用mcp：
    - 例如：使用fastapimcp 中有哪些工具可以使用？
    - 使用fastapimcp 获取用户列表
    - 使用fastapimcp 创建新的用户：name: bob,emal:demo@example.com
