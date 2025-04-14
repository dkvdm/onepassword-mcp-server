# server.py
import os
from mcp.server.fastmcp import FastMCP
from onepassword.client import Client

# Create an MCP server
mcp = FastMCP("1Password")

@mcp.tool()
async def get_1password_credentials(item_name: str) -> dict:
    """Get 1Password credentials for a given site."""
    # Initialize the 1Password client
    client = await Client.authenticate(auth=os.getenv("OP_SERVICE_ACCOUNT_TOKEN"), integration_name="1Password MCP Integration", integration_version="v1.0.0")
    
    email = await client.secrets.resolve(f"op://AI/{item_name}/username")
    password = await client.secrets.resolve(f"op://AI/{item_name}/password")

    return {"email": email, "password": password}

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
