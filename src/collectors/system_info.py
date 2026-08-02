import platform
import socket
import getpass
import json
from datetime import datetime
from pathlib import Path


def collect_system_information():
    """Collect system information and save it to a JSON file."""

    system_information = {
        "hostname": socket.gethostname(),
        "current_user": getpass.getuser(),
        "operating_system": platform.system(),
        "release": platform.release(),
        "os_version": platform.version(),
        "architecture": platform.architecture()[0],
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "collection_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Create a folder for system information if it doesn't exist
    output_folder = Path("output")
    output_folder.mkdir(parents=True, exist_ok=True)

    # Save the system information to a JSON file
    output_file = output_folder / f"system_info_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(system_information, file, indent=4)

    print(f"System information collected and saved to {output_file}")