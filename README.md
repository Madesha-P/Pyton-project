# Event Registration System

Hi this is ,

A simple command-line application written in Python that allows you to register participants for events and automatically saves their details into organized `.txt` files.

---

## Features

- Register participants with full validation on every field
- Choose from 5 pre-defined events
- Auto-generates a unique Participant ID per registration
- Saves each participant's details in their own individual `.txt` file
- Appends every registration to a single master file (`all_participants.txt`)
- View all registered participants directly from the terminal
- Fully compatible with Windows, macOS, and Linux (UTF-8 encoded output)

---

## Requirements

- Python 3.x (no external libraries needed — uses only built-in modules)

To check your Python version:
```
python --version
```

---

## How to Run

1. Download `event_registration.py`
2. Open a terminal (Command Prompt, PowerShell, or any shell)
3. Navigate to the folder where the file is saved:
   ```
   cd path\to\your\folder
   ```
4. Run the script:
   ```
   python event_registration.py
   ```

---

## Menu Options

```
[1] Register a New Participant
[2] View All Registered Participants
[3] Exit
```

### Registering a Participant

When you select option 1, you will be prompted to enter:

| Field        | Validation                          |
|--------------|-------------------------------------|
| Full Name    | Cannot be empty                     |
| Age          | Must be a number between 1 and 120  |
| Email        | Must contain `@` and `.`            |
| Phone Number | Must be numeric, minimum 7 digits   |
| City         | Cannot be empty                     |

After entering details, you select one of the 5 available events:

```
[1] Tech Conference 2026
[2] Python Workshop
[3] Data Science Summit
[4] AI & ML Bootcamp
[5] Web Development Hackathon
```

---

## Output Files

All files are saved inside a folder named `event_registrations/`, which is created automatically in the same directory as the script.

### Individual File (one per participant)

**Filename format:** `FirstName_LastName_<ParticipantID>.txt`

**Example:** `Arjun_Sharma_TC2-20260525103045.txt`

**Contents:**
```
==================================================
       REGISTRATION CONFIRMATION
==================================================

  Participant ID  : TC2-20260525103045
  Registered On   : 2026-05-25 10:30:45

  Full Name       : Arjun Sharma
  Age             : 28
  Email Address   : arjun.sharma@email.com
  Phone Number    : +91-9876543210
  City            : Mysuru

  Event Registered: Tech Conference 2026

==================================================
  [OK] Registration Successful!
==================================================
```

### Master File (all participants in one place)

**Filename:** `all_participants.txt`

All registrations are appended here in a tabular format with a numbered list, making it easy to review everyone at a glance.

```
================================================================================
                    ALL REGISTERED PARTICIPANTS
================================================================================
  #    Participant ID            Name                   Age   Event                        City
--------------------------------------------------------------------------------
  1    TC2-20260525103045        Arjun Sharma           28    Tech Conference 2026         Mysuru
       Email: arjun.sharma@email.com  |  Phone: +91-9876543210  |  Registered: 2026-05-25 10:30:45
--------------------------------------------------------------------------------
```

---

## Folder Structure

After running the program, your folder will look like this:

```
your-folder/
│
├── event_registration.py
│
└── event_registrations/
    ├── all_participants.txt
    ├── Arjun_Sharma_TC2-20260525103045.txt
    ├── Priya_Nair_PW-20260525103112.txt
    └── ...
```

---

## Participant ID Format

Each ID is auto-generated using the initials of the event name and a timestamp:

```
<EVENT_INITIALS>-<YYYYMMDDHHMMSS>

Example:
  Tech Conference 2026      -->  TC2-20260525103045
  Python Workshop           -->  PW-20260525103112
  Data Science Summit       -->  DSS-20260525103200
  AI & ML Bootcamp          -->  A&MB-20260525103245
  Web Development Hackathon -->  WDH-20260525103310
```

---
## License

This project is free to use and modify for personal or educational purposes.
