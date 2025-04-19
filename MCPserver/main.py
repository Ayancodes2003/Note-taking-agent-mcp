# server.py
from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("AI sticky notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

@mcp.tool()
def add_note(message: str) -> str:
    """Add a note to the notes file.
    
    Args:
        message (str): The message to add to the notes file.

    Returns:
        str: A message indicating that the note was added.
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Note added."

@mcp.tool()
def read_notes() -> str:
    """Read the notes from the notes file.

    Returns:
        str: The notes from the notes file.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        contents = f.read().strip()
    return contents or "No notes found."

@mcp.resource("notes://latest")
def latest_note() -> str:
    """Get the latest note from the notes file.

    Returns:
        str: The latest note from the notes file.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet."

@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Generate a prompt asking the AI to summarise all current notes.
    Returns:
        str: A prompt string that includes all notes and asks for a summary. 
            If no notes exists, a message will be shown indicating that.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        contents = f.read().strip()
    if not content:
        return "there are no notes yet."
    return f"Here are the notes:\n{contents}"
