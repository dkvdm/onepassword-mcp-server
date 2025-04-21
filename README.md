> **Project Note**: ⚠️ This MCP server is a proof of concept and is intended for educational purposes only. It utilizes the [1Password Python SDK](https://github.com/modelcontextprotocol/python-sdk) to securely retrieve credentials from your 1Password account and provides them via the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) to Agentic AI for use in its operations. ⚠️

## Quick Start

### Installing via Smithery

To install 1Password Credential Retrieval Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@dkvdm/onepassword-mcp-server):

```bash
npx -y @smithery/cli install @dkvdm/onepassword-mcp-server --client claude
```

### Prerequisites

-   Python 3.11 or higher
-   `uv` (fast Python package installer): `pip install uv`
-   Install packages: `uv sync`
- Create a vault within 1Password named `AI`, and add the items you want to use.
- [Create a service account](https://my.1password.com/developer-tools/infrastructure-secrets/serviceaccount/) and give it the appropriate permissions in the vaults where the items you want to use with the SDK are saved.
- Provision your service account token, and configure clients like Claude Desktop to connect to this server. Add the following structure to the client's configuration (e.g., `claude_desktop_config.json`), adjusting the path and environment variables as needed:

```json
// Example for Claude Desktop config
{
  "mcpServers": {
    "1Password": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "--with",
        "onepassword-sdk",
        "mcp",
        "run",
        "/your/dir/here/onepassword-mcp-server/server.py" // Change this path
      ],
      "env": {
        "OP_SERVICE_ACCOUNT_TOKEN": "INSERT_KEY_HERE" // Insert 1Password Service Account Token
      }
    }
  }
}
```
* Launch Claude and try a prompt such as "Get 1Password credentials for ticktick.com" (based on item name)


### Automate Browser with 1Password and Browser-Use MCP

Install [mcp-browser-use](https://github.com/Saik0s/mcp-browser-use) and configure both MCP servers as such:

```json
// Example for Claude Desktop config
{
  "mcpServers": {
    "1Password": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "--with",
        "onepassword-sdk",
        "mcp",
        "run",
        "/your/dir/here/onepassword-mcp-server/server.py"
      ],
      "env": {
        "OP_SERVICE_ACCOUNT_TOKEN": "INSERT_KEY_HERE"
      }
    },
    "browser-use": {
      "command": "uv",
      "args": [
        "--directory",
        "/your/dir/here/mcp-browser-use",
        "run",
        "mcp-server-browser-use"
      ],
      "env": {
        "MCP_USE_OWN_BROWSER": "true",
        "CHROME_CDP": "http://127.0.0.1:9222",
        "ANTHROPIC_API_KEY": "INSERT_KEY_HERE",
        "PYTHONIOENCODING": "utf-8",
        "PYTHONUNBUFFERED": "1",
        "PYTHONUTF8": "1"
      }
    }
  }
}
```
* Launch Claude and try a prompt such as "get 1Password credentials for ticktick.com and log into https://ticktick.com/signin"
