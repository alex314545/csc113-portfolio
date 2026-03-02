# prompt-tracker.py

def main():
    while True:
        print("\n--- Prompt Tracker Menu ---")
        print("1. Add Prompt")
        print("2. View Prompts")
        print("3. Search Prompts")
        print("4. Delete Prompt")  # NEW: Added menu option
        print("5. Quit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_prompt()
        elif choice == '2':
            view_prompts()
        elif choice == '3':
            search_prompts()
        elif choice == '4':
            delete_prompt() # NEW: Call the delete function
        elif choice == '5':
            print("Goodbye! Happy prompting.")
            break 
        else:
            print("Invalid choice, please try again.")

def add_prompt():
    text = input("Enter the prompt text: ")
    print("Categories: learning, creating, evaluating, other")
    category = input("Enter category: ").lower()
    note = input("Enter a short note about when to use it: ")

    with open("my-prompts.txt", "a") as file:
        file.write(f"{category}|{text}|{note}\n")
    
    print("Prompt saved successfully!")

def view_prompts():
    try:
        with open("my-prompts.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No prompts saved yet.")
            return

        categories = ["learning", "creating", "evaluating", "other"]
        for cat in categories:
            print(f"\n--- {cat.upper()} ---")
            for line in lines:
                parts = line.strip().split('|')
                if parts[0] == cat:
                    print(f"Prompt: {parts[1]}")
                    print(f"Note: {parts[2]}")
                    print("-" * 10)
    except FileNotFoundError:
        print("No prompts found. Add one first!")

def search_prompts():
    keyword = input("Enter a keyword to search for: ").lower()
    try:
        with open("my-prompts.txt", "r") as file:
            found = False
            for line in file:
                if keyword in line.lower():
                    parts = line.strip().split('|')
                    print(f"\n[{parts[0].upper()}]")
                    print(f"Prompt: {parts[1]}")
                    print(f"Note: {parts[2]}")
                    found = True
            if not found:
                print("No matching prompts found.")
    except FileNotFoundError:
        print("No prompts found yet.")

# NEW: The delete function
def delete_prompt():
    try:
        # 1. READ: Get all lines from the file
        with open("my-prompts.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("Nothing to delete.")
            return

        # 2. DISPLAY: Show prompts with a number so the user can choose
        print("\n--- Delete a Prompt ---")
        for index, line in enumerate(lines):
            parts = line.strip().split('|')
            # We show index + 1 so users see "1" instead of "0"
            print(f"{index + 1}. [{parts[0]}] {parts[1][:50]}...") 

        # 3. CHOOSE: Ask the user which number to remove
        choice = input("\nEnter the number of the prompt to delete (or 'c' to cancel): ")
        
        if choice.lower() == 'c':
            return

        # Convert input to an integer and adjust for 0-based indexing
        selection = int(choice) - 1

        if 0 <= selection < len(lines):
            # 4. MODIFY: Remove the chosen line from our list
            deleted_item = lines.pop(selection)
            
            # 5. WRITE: Save the list back to the file
            # We use 'w' mode here to overwrite the entire file
            with open("my-prompts.txt", "w") as file:
                file.writelines(lines)
            
            print(f"Successfully deleted: {deleted_item.split('|')[1][:20]}...")
        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("No file found to delete from.")

if __name__ == "__main__":
    main()