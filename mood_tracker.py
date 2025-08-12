import json
from datetime import datetime
import os

MOOD_LOG_FILE = "mood_log.json"

def get_mood_history():
    """
    Retrieves the mood history from the log file.
    Returns a list of mood entries.
    """
    if not os.path.exists(MOOD_LOG_FILE):
        return []
    try:
        with open(MOOD_LOG_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def log_mood(mood: str, rating: int):
    """
    Logs the user's current mood to a JSON file.

    Args:
        mood (str): The mood description (e.g., "Happy", "Anxious").
        rating (int): A rating of the mood intensity (e.g., 1-10).
    """
    history = get_mood_history()
    
    new_entry = {
        "timestamp": datetime.now().isoformat(),
        "mood": mood,
        "rating": rating
    }
    
    history.append(new_entry)
    
    try:
        with open(MOOD_LOG_FILE, "w") as f:
            json.dump(history, f, indent=4)
        print("\n✨ Your mood has been logged successfully.")
    except IOError as e:
        print(f"\n❌ Error: Could not write to mood log file: {e}")

def get_last_mood():
    """Returns the most recently logged mood, or None if no history."""
    history = get_mood_history()
    return history[-1] if history else None