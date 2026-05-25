import os
import json
from datetime import datetime

# Directory to store output files
OUTPUT_DIR = "event_registrations"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# File to store all participants
ALL_PARTICIPANTS_FILE = os.path.join(OUTPUT_DIR, "all_participants.txt")

# Available events
EVENTS = {
    "1": "Tech Conference 2026",
    "2": "Python Workshop",
    "3": "Data Science Summit",
    "4": "AI & ML Bootcamp",
    "5": "Web Development Hackathon"
}


def display_banner():
    print("=" * 60)
    print("       EVENT REGISTRATION SYSTEM")
    print("=" * 60)


def display_events():
    print("\n📅 Available Events:")
    print("-" * 40)
    for key, event in EVENTS.items():
        print(f"  [{key}] {event}")
    print("-" * 40)


def get_participant_details():
    print("\n📝 Enter Participant Details:")
    print("-" * 40)

    name = input("  Full Name       : ").strip()
    while not name:
        print("  ⚠  Name cannot be empty.")
        name = input("  Full Name       : ").strip()

    age = input("  Age             : ").strip()
    while not age.isdigit() or not (1 <= int(age) <= 120):
        print("  ⚠  Enter a valid age (1–120).")
        age = input("  Age             : ").strip()

    email = input("  Email Address   : ").strip()
    while "@" not in email or "." not in email:
        print("  ⚠  Enter a valid email address.")
        email = input("  Email Address   : ").strip()

    phone = input("  Phone Number    : ").strip()
    while not phone.replace("+", "").replace("-", "").replace(" ", "").isdigit() or len(phone) < 7:
        print("  ⚠  Enter a valid phone number.")
        phone = input("  Phone Number    : ").strip()

    city = input("  City            : ").strip()
    while not city:
        print("  ⚠  City cannot be empty.")
        city = input("  City            : ").strip()

    return {
        "name": name,
        "age": int(age),
        "email": email,
        "phone": phone,
        "city": city
    }


def choose_event():
    display_events()
    choice = input("\n  Select Event [1-5]: ").strip()
    while choice not in EVENTS:
        print("  ⚠  Invalid choice. Please enter a number between 1 and 5.")
        choice = input("  Select Event [1-5]: ").strip()
    return EVENTS[choice]


def generate_participant_id(event_name):
    """Generate a unique participant ID."""
    prefix = "".join([w[0] for w in event_name.split()]).upper()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{prefix}-{timestamp}"


def save_individual_file(participant):
    """Save each participant's details in a separate .txt file."""
    safe_name = participant["name"].replace(" ", "_").replace("/", "-")
    filename = f"{safe_name}_{participant['participant_id']}.txt"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("       REGISTRATION CONFIRMATION\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"  Participant ID  : {participant['participant_id']}\n")
        f.write(f"  Registered On   : {participant['registered_on']}\n\n")
        f.write(f"  Full Name       : {participant['name']}\n")
        f.write(f"  Age             : {participant['age']}\n")
        f.write(f"  Email Address   : {participant['email']}\n")
        f.write(f"  Phone Number    : {participant['phone']}\n")
        f.write(f"  City            : {participant['city']}\n\n")
        f.write(f"  Event Registered: {participant['event']}\n\n")
        f.write("=" * 50 + "\n")
        f.write("  [OK] Registration Successful!\n")
        f.write("=" * 50 + "\n")

    return filepath


def save_to_all_participants(participant):
    """Append participant summary to the single all_participants.txt file."""
    # Check if file is new (write header once)
    write_header = not os.path.exists(ALL_PARTICIPANTS_FILE)

    with open(ALL_PARTICIPANTS_FILE, "a", encoding="utf-8") as f:
        if write_header:
            f.write("=" * 80 + "\n")
            f.write("                    ALL REGISTERED PARTICIPANTS\n")
            f.write("=" * 80 + "\n")
            f.write(f"  {'#':<4} {'Participant ID':<25} {'Name':<22} {'Age':<5} {'Event':<28} {'City'}\n")
            f.write("-" * 80 + "\n")

        # Count existing entries to number this one
        count = count_all_participants()
        f.write(
            f"  {count:<4} {participant['participant_id']:<25} {participant['name']:<22} "
            f"{participant['age']:<5} {participant['event']:<28} {participant['city']}\n"
        )
        f.write(f"       Email: {participant['email']}  |  Phone: {participant['phone']}  |  Registered: {participant['registered_on']}\n")
        f.write("-" * 80 + "\n")


def count_all_participants():
    """Count how many participants are already registered."""
    if not os.path.exists(ALL_PARTICIPANTS_FILE):
        return 1
    count = 0
    with open(ALL_PARTICIPANTS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            # Each participant has an email line as a signature
            if line.strip().startswith("Email:"):
                count += 1
    return count + 1


def register_participant():
    """Full registration flow for one participant."""
    participant = get_participant_details()
    event = choose_event()

    participant["event"] = event
    participant["registered_on"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    participant["participant_id"] = generate_participant_id(event)

    # Save individual file
    individual_file = save_individual_file(participant)

    # Save to combined file
    save_to_all_participants(participant)

    print("\n" + "=" * 60)
    print("  ✅  REGISTRATION SUCCESSFUL!")
    print("=" * 60)
    print(f"  Participant ID  : {participant['participant_id']}")
    print(f"  Name            : {participant['name']}")
    print(f"  Event           : {participant['event']}")
    print(f"  Individual File : {individual_file}")
    print(f"  Master File     : {ALL_PARTICIPANTS_FILE}")
    print("=" * 60)

    return participant


def view_all_participants():
    """Display all registered participants from the master file."""
    if not os.path.exists(ALL_PARTICIPANTS_FILE):
        print("\n  ℹ  No participants registered yet.\n")
        return

    print("\n")
    with open(ALL_PARTICIPANTS_FILE, "r", encoding="utf-8") as f:
        print(f.read())


def main():
    display_banner()

    while True:
        print("\n🔧 MAIN MENU")
        print("-" * 40)
        print("  [1] Register a New Participant")
        print("  [2] View All Registered Participants")
        print("  [3] Exit")
        print("-" * 40)

        choice = input("  Enter your choice [1-3]: ").strip()

        if choice == "1":
            register_participant()

            more = input("\n  Register another participant? (yes/no): ").strip().lower()
            if more not in ("yes", "y"):
                print("\n  Thank you for using the Event Registration System!")
                break

        elif choice == "2":
            view_all_participants()

        elif choice == "3":
            print("\n  👋 Goodbye! See you at the events!\n")
            break

        else:
            print("  ⚠  Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
