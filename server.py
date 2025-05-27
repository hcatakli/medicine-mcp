from mcp.server.fastmcp import FastMCP
from app import getMedicine

# Initialize MCP server
mcp = FastMCP("medicine-mcp")

@mcp.tool()
def get_medicine_info(medicine_name: str) -> str:
    """
    Get information for a medicine.
    """
    # Get definitions from the app
    medicine_info = getMedicine(medicine_name)
    if not medicine_info:
        return "No information found."

    return medicine_info

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=3000)
