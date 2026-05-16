# DeVloped By ZOBAYAR | CODEX  
import json

def convert_accounts(input_file, output_file):
    # Step 1: JSON Reading files
    with open(input_file, "r", encoding="utf-8") as f:
        accounts_list = json.load(f)

    # Step 2: Creating a new dict
    accounts_dict = {}
    for account in accounts_list:
        uid = str(account.get("uid"))  # Convert uid to string
        password = account.get("password")
        if uid and password:
            accounts_dict[uid] = password

    # Step 3: Writing a new JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(accounts_dict, f, indent=2, ensure_ascii=False)

    print(f"✅ Converted JSON saved to '{output_file}'")


# Example usage
input_file = "accounts-bd-activated.json"   # Your list of dict JSON
output_file = "accs.json"  # Will be saved as a key-value dict

convert_accounts(input_file, output_file)