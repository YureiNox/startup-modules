import json
import os

class JsonModifier:
    def __init__(self, filepath='tools/json/startup.json'):
        self.filepath = filepath
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def add_key(self, key, value):
        if key in self.data:
            print(f"Key '{key}' already exists with value: {self.data[key]}")
        else:
            self.data[key] = value
            print(f"Added key '{key}' with value: {value}")
        self.save_changes()

    def modify_key(self, key, new_value):
        if key in self.data:
            self.data[key] = new_value
            print(f"Modified key '{key}' with new value: {new_value}")
        else:
            print(f"Key '{key}' not found.")
        self.save_changes()

    def delete_key(self, key):
        if key in self.data:
            del self.data[key]
            print(f"Deleted key '{key}'")
        else:
            print(f"Key '{key}' not found.")
        self.save_changes()

    def save_changes(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=4)
        print("Changes saved.")

    def show_content(self):
        return self.data

def menu():
    json_mod = JsonModifier()
    while True:
        print("\n--- JSON Modifier Menu ---")
        print("1. Add a key")
        print("2. Modify a key")
        print("3. Delete a key")
        print("4. Show JSON content")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            key = input("Enter the key you want to add: ")
            value_type = input("Enter the type of the value (str, list, int, etc.): ")
            if value_type == 'list':
                value = input("Enter the list values separated by commas: ").split(',')
            elif value_type == 'int':
                value = int(input("Enter the integer value: "))
            else:
                value = input("Enter the value: ")
            json_mod.add_key(key, value)

        elif choice == '2':
            key = input("Enter the key you want to modify: ")
            value_type = input("Enter the type of the new value (str, list, int, etc.): ")
            if value_type == 'list':
                new_value = input("Enter the new list values separated by commas: ").split(',')
            elif value_type == 'int':
                new_value = int(input("Enter the new integer value: "))
            else:
                new_value = input("Enter the new value: ")
            json_mod.modify_key(key, new_value)

        elif choice == '3':
            key = input("Enter the key you want to delete: ")
            json_mod.delete_key(key)

        elif choice == '4':
            content = json_mod.show_content()
            print("Current JSON content:", json.dumps(content, indent=4))

        elif choice == '5':
            print("Exiting the menu.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()
