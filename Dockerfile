# Generated by https://smithery.ai. See: https://smithery.ai/docs/config#dockerfile
# Use official Python image
FROM python:3.12-slim

# Install uv installer and clean cache
RUN pip install --no-cache-dir uv

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock server.py ./

# Install dependencies via uv
RUN uv sync

# Default command to run the MCP server over stdio
CMD ["uv", "run", "--with", "mcp[cli]", "--with", "onepassword-sdk", "mcp", "run", "server.py"]
