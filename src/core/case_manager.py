from pathlib import Path
import json
from datetime import datetime

def create_case():
    """Create a new forensic case folder."""

    case_name =  input("Enter the case name: ").strip()

    if not case_name:
        print("Case name cannot be empty. Please try again.")
        return

    #replace spaces with underscores
    safe_name = case_name.replace(" ", "_")

    #Create a folder path
    case_path = Path("cases") / safe_name

    #check if it already exists
    if case_path.exists():
        print("\n[!] A case with that name already exits. Please choose a different name.")
        return

    #create a folder
    case_path.mkdir(parents=True, exist_ok=True)

    (case_path / "evidence").mkdir()
    (case_path / "reports").mkdir()
    (case_path / "logs").mkdir()
    (case_path / "notes").mkdir()

    case_information = {
        "case_name": case_name,
        "status": "Open",
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(case_path / "case.json", "w") as file:
        json.dump(case_information, file, indent=4)

    print("\nCase created successfully!")
    print(f"Location: {case_path}")