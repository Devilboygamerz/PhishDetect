import os
import json

CONFIG_DIR = "config"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

DEFAULT_CONFIG = {
    "api_key": "",
    "theme": "yellow",
    "version": "1.0.0",
    "save_reports": True,
    "show_vendor_analysis": True
}


def create_config():
    os.makedirs(CONFIG_DIR, exist_ok=True)

    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)


def load_config():
    create_config()

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)


def get_api_key():
    config = load_config()

    if config["api_key"] == "":
        print("\nNo VirusTotal API key found.\n")
        key = input("Enter your VirusTotal API Key: ").strip()

        config["api_key"] = key
        save_config(config)

        print("\n✓ API Key saved successfully.\n")

    return config["api_key"]


def change_api_key():
    config = load_config()

    key = input("Enter new API Key: ").strip()

    config["api_key"] = key
    save_config(config)

    print("\n✓ API Key updated.\n")


def delete_api_key():
    config = load_config()

    config["api_key"] = ""
    save_config(config)

    print("\n✓ API Key removed.\n")
