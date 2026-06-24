import os
from datetime import datetime

# Output file
OUTPUT_FILE = "all_participants.txt"

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
    print("         EVENT REGISTRATION SYSTEM")
    print("=" * 60)


def display_events():
    print("\n  Available Events:")
    print("  " + "-" * 38)
    for key, event in EVENTS.items():
        print(f"    [{key}] {event}")
    print("  " + "-" * 38)


def input_name():
    val = input("  Full Name       : ").strip()
    while not val:
        print("  [!] Name cannot be empty.")
        val = input("  Full Name       : ").strip()
    return val


def input_age():
    val = input("  Age             : ").strip()
    while not val.isdigit() or not (1 <= int(val) <= 120):
        print("  [!] Enter a valid age (1-120).")
        val = input("  Age             : ").strip()
    return int(val)


def input_email():
    val = input("  Email Address   : ").strip()
    while "@" not in val or "." not in val:
        print("  [!] Enter a valid email address.")
        val = input("  Email Address   : ").strip()
    return val


def input_phone():
    val = input("  Phone Number    : ").strip()
    while not val.replace("+", "").replace("-", "").replace(" ", "").isdigit() or len(val) < 7:
        print("  [!] Enter a valid phone number.")
        val = input("  Phone Number    : ").strip()
    return val


def input_city():
    val = input("  City            : ").strip()
    while not val:
        print("  [!] City cannot be empty.")
        val = input("  City            : ").strip()
    return val


def input_event():
    display_events()
    choice = input("\n  Select Event [1-5]: ").strip()
    while choice not in EVENTS:
        print("  [!] Invalid choice. Enter a number between 1 and 5.")
        choice = input("  Select Event [1-5]: ").strip()
    return EVENTS[choice]


def collect_details():
    """Collect all participant details from scratch."""
    print("\n  Enter Participant Details:")
    print("  " + "-" * 38)
    participant = {
        "name":  input_name(),
        "age":   input_age(),
        "email": input_email(),
        "phone": input_phone(),
        "city":  input_city(),
        "event": input_event(),
    }
    return participant


def preview_form(participant):
    """Display a preview of the filled form."""
    print("\n" + "=" * 60)
    print("  REGISTRATION PREVIEW")
    print("=" * 60)
    print(f"  [1] Full Name    : {participant['name']}")
    print(f"  [2] Age          : {participant['age']}")
    print(f"  [3] Email        : {participant['email']}")
    print(f"  [4] Phone        : {participant['phone']}")
    print(f"  [5] City         : {participant['city']}")
    print(f"  [6] Event        : {participant['event']}")
    print("=" * 60)


def edit_form(participant):
    """Let the user edit any field before saving."""
    while True:
        preview_form(participant)
        print("\n  Which field do you want to edit?")
        print("  [1] Full Name  [2] Age  [3] Email")
        print("  [4] Phone      [5] City [6] Event")
        print("  [0] Done editing")
        print()

        choice = input("  Enter field number (or 0 when done): ").strip()

        if choice == "0":
            break
        elif choice == "1":
            print()
            participant["name"] = input_name()
        elif choice == "2":
            print()
            participant["age"] = input_age()
        elif choice == "3":
            print()
            participant["email"] = input_email()
        elif choice == "4":
            print()
            participant["phone"] = input_phone()
        elif choice == "5":
            print()
            participant["city"] = input_city()
        elif choice == "6":
            participant["event"] = input_event()
        else:
            print("  [!] Invalid choice. Enter a number from 0 to 6.")

    return participant


def generate_participant_id(event_name):
    prefix = "".join([w[0] for w in event_name.split()]).upper()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{prefix}-{timestamp}"


def count_participants():
    """Count existing registrations in the master file."""
    if not os.path.exists(OUTPUT_FILE):
        return 0
    count = 0
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("Email:"):
                count += 1
    return count


def save_to_master(participant):
    """Append participant to the master file."""
    write_header = not os.path.exists(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        if write_header:
            f.write("=" * 100 + "\n")
            f.write("                     ALL REGISTERED PARTICIPANTS\n")
            f.write("=" * 100 + "\n")
            f.write(
                f"  {'#':<4} {'Participant ID':<25} {'Name':<22} "
                f"{'Age':<5} {'Event':<28} {'City'}\n"
            )
            f.write("-" * 100 + "\n")

        num = count_participants() + 1
        f.write(
            f"  {num:<4} {participant['participant_id']:<25} {participant['name']:<22} "
            f"{participant['age']:<5} {participant['event']:<28} {participant['city']}\n"
        )
        f.write(
            f"       Email: {participant['email']}  |  "
            f"Phone: {participant['phone']}  |  "
            f"Registered: {participant['registered_on']}\n"
        )
        f.write("-" * 100 + "\n")


def register_participant():
    """Full registration flow with edit option."""
    participant = collect_details()

    while True:
        preview_form(participant)
        print("\n  What would you like to do?")
        print("  [1] Confirm & Save")
        print("  [2] Edit Details")
        print("  [3] Cancel Registration")
        print()

        action = input("  Enter choice [1-3]: ").strip()

        if action == "1":
            participant["registered_on"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            participant["participant_id"] = generate_participant_id(participant["event"])
            save_to_master(participant)

            print("\n" + "=" * 60)
            print("  REGISTRATION SUCCESSFUL!")
            print("=" * 60)
            print(f"  Participant ID  : {participant['participant_id']}")
            print(f"  Name            : {participant['name']}")
            print(f"  Event           : {participant['event']}")
            print(f"  Saved to        : {OUTPUT_FILE}")
            print("=" * 60)
            break

        elif action == "2":
            participant = edit_form(participant)

        elif action == "3":
            print("\n  [!] Registration cancelled.\n")
            break

        else:
            print("  [!] Please enter 1, 2, or 3.")


def view_all_participants():
    """Print the master file to the terminal."""
    if not os.path.exists(OUTPUT_FILE):
        print("\n  No participants registered yet.\n")
        return
    print()
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        print(f.read())


def load_participants():
    """Parse all_participants.txt and return a list of participant dicts."""
    participants = []
    if not os.path.exists(OUTPUT_FILE):
        return participants

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        # Data rows: start with 2 spaces then a digit (the row number)
        stripped = line.rstrip("\n")
        if len(stripped) > 2 and stripped[:2] == "  " and stripped[2:3].isdigit():
            try:
                num   = int(stripped[2:6].strip())
                pid   = stripped[6:31].strip()
                name  = stripped[31:53].strip()
                age   = int(stripped[53:58].strip())
                event = stripped[58:86].strip()
                city  = stripped[86:].strip()

                # Next line: email/phone/registered
                detail = lines[i + 1].strip() if i + 1 < len(lines) else ""
                email, phone, registered_on = "", "", ""
                if detail.startswith("Email:"):
                    detail = detail[len("Email:"):].strip()
                    parts = detail.split("|")
                    email         = parts[0].strip()
                    phone         = parts[1].replace("Phone:", "").strip() if len(parts) > 1 else ""
                    registered_on = parts[2].replace("Registered:", "").strip() if len(parts) > 2 else ""

                participants.append({
                    "num": num,
                    "participant_id": pid,
                    "name": name,
                    "age": age,
                    "email": email,
                    "phone": phone,
                    "city": city,
                    "event": event,
                    "registered_on": registered_on,
                })
            except (ValueError, IndexError):
                pass

    return participants


def rewrite_master(participants):
    """Rewrite the master file from a list of participant dicts."""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("=" * 100 + "\n")
        f.write("                     ALL REGISTERED PARTICIPANTS\n")
        f.write("=" * 100 + "\n")
        f.write(
            f"  {'#':<4} {'Participant ID':<25} {'Name':<22} "
            f"{'Age':<5} {'Event':<28} {'City'}\n"
        )
        f.write("-" * 100 + "\n")
        for i, p in enumerate(participants, 1):
            f.write(
                f"  {i:<4} {p['participant_id']:<25} {p['name']:<22} "
                f"{p['age']:<5} {p['event']:<28} {p['city']}\n"
            )
            f.write(
                f"       Email: {p['email']}  |  "
                f"Phone: {p['phone']}  |  "
                f"Registered: {p['registered_on']}\n"
            )
            f.write("-" * 100 + "\n")


def edit_saved_participant():
    """Select a saved participant by number and edit their details."""
    participants = load_participants()

    if not participants:
        print("\n  No participants registered yet.\n")
        return

    print("\n" + "=" * 60)
    print("  SELECT PARTICIPANT TO EDIT")
    print("=" * 60)
    for p in participants:
        print(f"  [{p['num']}] {p['name']}  |  {p['event']}  |  {p['city']}")
    print("  [0] Back to Main Menu")
    print("=" * 60)

    choice = input("\n  Enter participant number: ").strip()

    if choice == "0":
        return

    if not choice.isdigit() or not any(p["num"] == int(choice) for p in participants):
        print("  [!] Invalid number. Returning to main menu.\n")
        return

    selected = next(p for p in participants if p["num"] == int(choice))
    updated = edit_form(selected)

    for i, p in enumerate(participants):
        if p["num"] == updated["num"]:
            participants[i] = updated
            break

    rewrite_master(participants)

    print("\n" + "=" * 60)
    print("  PARTICIPANT UPDATED SUCCESSFULLY!")
    print("=" * 60)
    print(f"  Name     : {updated['name']}")
    print(f"  Event    : {updated['event']}")
    print(f"  Saved to : {OUTPUT_FILE}")
    print("=" * 60)


def main():
    display_banner()

    while True:
        print("\n  MAIN MENU")
        print("  " + "-" * 38)
        print("  [1] Register a New Participant")
        print("  [2] View All Registered Participants")
        print("  [3] Edit a Registered Participant")
        print("  [4] Exit")
        print("  " + "-" * 38)

        choice = input("  Enter your choice [1-4]: ").strip()

        if choice == "1":
            register_participant()
            more = input("\n  Register another participant? (yes/no): ").strip().lower()
            if more not in ("yes", "y"):
                print("\n  Thank you for using the Event Registration System!\n")
                break

        elif choice == "2":
            view_all_participants()

        elif choice == "3":
            edit_saved_participant()

        elif choice == "4":
            print("\n  Goodbye! See you at the events!\n")
            break

        else:
            print("  [!] Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
