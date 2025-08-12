import time
from wellness_bot import WellnessBot
import mood_tracker

def print_disclaimer():
    """Prints a disclaimer about the app's purpose."""
    print("=" * 60)
    print("🚨 DISCLAIMER 🚨".center(60))
    print("This AI Wellness Companion is for informational and educational".center(60))
    print("purposes only. It is NOT a substitute for professional".center(60))
    print("medical advice, diagnosis, or treatment.".center(60))
    print("=" * 60)
    print("\n")

def display_menu():
    """Displays the main menu."""
    print("\n--- AI Wellness Companion Menu ---")
    print("1. Track my mood")
    print("2. Get a coping strategy for my current mood")
    print("3. Get a calming exercise")
    print("4. Get a journaling prompt")
    print("5. View my mood history")
    print("6. Exit")
    print("----------------------------------")

def handle_mood_tracking():
    """Handles the mood tracking feature."""
    mood = input("How are you feeling right now? (e.g., happy, anxious, calm): ")
    while True:
        try:
            rating_str = input(f"On a scale of 1-10, how intense is this feeling of {mood}? ")
            rating = int(rating_str)
            if 1 <= rating <= 10:
                mood_tracker.log_mood(mood.strip(), rating)
                break
            else:
                print("❌ Please enter a number between 1 and 10.")
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")

def handle_coping_strategy(bot: WellnessBot):
    """Handles generating a coping strategy."""
    print("\nGetting a coping strategy...")
    last_mood_entry = mood_tracker.get_last_mood()
    if not last_mood_entry:
        print("Your mood log is empty. Please track your mood first (Option 1).")
        return
    
    mood = last_mood_entry['mood']
    print(f"Based on your last logged mood: '{mood}'")
    strategy = bot.generate_coping_strategy(mood)
    print("\n💡 Here is a gentle suggestion for you:\n")
    print(strategy)

def handle_calming_exercise(bot: WellnessBot):
    """Handles generating a calming exercise."""
    print("\n🧘 Generating a calming exercise for you...")
    exercise = bot.generate_calming_exercise()
    print("\nFind a quiet space and follow this guide:\n")
    print(exercise)

def handle_journal_prompt(bot: WellnessBot):
    """Handles generating a journal prompt."""
    print("\n✍️ Generating a journal prompt for you...")
    prompt = bot.generate_journal_prompt()
    print("\nHere is a prompt for your reflection:\n")
    print(prompt)
    journal_entry = input("\nFeel free to write your thoughts here (or just press Enter to return): ")
    if journal_entry.strip():
        print("\nThank you for sharing. Taking time to reflect is a great step.")

def handle_view_history():
    """Displays the user's mood history."""
    print("\n--- Your Mood History ---")
    history = mood_tracker.get_mood_history()
    if not history:
        print("No moods logged yet.")
    else:
        for entry in history:
            print(f"- {entry['timestamp']}: Feeling {entry['mood']} (Intensity: {entry['rating']}/10)")
    print("-------------------------")

def main():
    """Main function to run the application."""
    print_disclaimer()
    try:
        bot = WellnessBot()
    except ValueError as e:
        print(f"❌ Initialization Error: {e}")
        print("Please ensure you have a .env file with your GOOGLE_API_KEY.")
        return

    print("Welcome to your AI Wellness Companion!")

    while True:
        display_menu()
        choice = input("Please choose an option (1-6): ")

        if choice == '1':
            handle_mood_tracking()
        elif choice == '2':
            handle_coping_strategy(bot)
        elif choice == '3':
            handle_calming_exercise(bot)
        elif choice == '4':
            handle_journal_prompt(bot)
        elif choice == '5':
            handle_view_history()
        elif choice == '6':
            print("\nThank you for taking time for your wellness. Goodbye! 👋")
            break
        else:
            print("\n❌ Invalid choice. Please select a number from 1 to 6.")
        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()