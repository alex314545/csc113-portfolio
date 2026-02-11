# AI-Assisted Coding Session — Week 2

## The Task
Build a prompt tracker script in Python.

## My Initial Prompt to Kevin
I need a Python script called prompt-tracker.py that does these things:
Shows a menu with options: Add Prompt, View Prompts, Search Prompts, Quit

When adding a prompt, asks for:
The prompt text
A category (learning / creating / evaluating / other)
A short note about when to use it
Saves prompts to a text file called "my-prompts.txt" so they persist
When viewing, shows all saved prompts organized by category
When searching, lets me type a keyword and shows matching prompts

Keep it simple — I'm a beginner. Use only built-in Python (no pip installs).
Add comments explaining what each part does.

## Kevin's Initial Response
Initial response was pretty long. He did exactly what my prompt asked him to do and gave me this code: 
def main():
    # This is the main loop of our program. 
    # It keeps running until the user chooses 'Quit'.
    while True:
        print("\n--- Prompt Tracker Menu ---")
        print("1. Add Prompt")
        print("2. View Prompts")
        print("3. Search Prompts")
        print("4. Quit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_prompt()
        elif choice == '2':
            view_prompts()
        elif choice == '3':
            search_prompts()
        elif choice == '4':
            print("Goodbye! Happy prompting.")
            break # This breaks the loop and ends the program
        else:
            print("Invalid choice, please try again.")

def add_prompt():
    # We collect the three pieces of information from the user
    text = input("Enter the prompt text: ")
    
    # We'll enforce the categories the student asked for
    print("Categories: learning, creating, evaluating, other")
    category = input("Enter category: ").lower()
    
    note = input("Enter a short note about when to use it: ")

    # We open the file in 'a' (append) mode. 
    # This adds to the end of the file without deleting what's already there.
    # We use '|' (a pipe) to separate our data so it's easy to read back later.
    with open("my-prompts.txt", "a") as file:
        file.write(f"{category}|{text}|{note}\n")
    
    print("Prompt saved successfully!")

def view_prompts():
    try:
        # We open the file in 'r' (read) mode.
        with open("my-prompts.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No prompts saved yet.")
            return

        # The student wanted them organized by category.
        # We'll loop through our known categories and print matching lines.
        categories = ["learning", "creating", "evaluating", "other"]
        
        for cat in categories:
            print(f"\n--- {cat.upper()} ---")
            for line in lines:
                # .strip() removes the invisible newline at the end
                # .split('|') turns our string back into a list
                parts = line.strip().split('|')
                
                # We check if the category (index 0) matches the one we're looking for
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
                # If the keyword exists anywhere in that line...
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

if __name__ == "__main__":
    main()

## Did the Code Work on First Try?
Yes, it worked flawlessly

## The Back-and-forth
The conversation was extremely simple. Everything I asked him for was done perfectly the first time I asked.

### Exchange 1: [Brief description]
**What I asked**: I asked for a python script that could track prompts and adds them to a text file. It will also allow me to search and view all saved prompts.
**What Kevin said**: After introducing himself, he generated the code and added comments explaining why each step was added and offered alternative ways I could do this.
**Result**: Worked

## The Improvement I Requested
**What I asked for**: Add option to delete prompts
**What changed**: enumerate(lines), lines.pop(selection), mode 'w' vs 'a', try/except ValueError
**Did it work?**: Yes

## Code Understanding Check
Answer honestly — this is about learning, not looking smart.

1. Can I explain what every line of `prompt_tracker.py` does?
   Some parts

2. If I had to modify this script without AI help, could I?
   I'd struggle

3. What's one thing in the code I want to understand better?
   The read, modify, write process looks really interesting.

## Reflection

Previously, I never thought AI could assist in coding. I heard many stories of people trying to use AI to code programs and the code would just never work. This experience pleasantly surprised me, as I was expecting to have to make some adjustments to the code. Kevin did really well in following the prompts. He gave me working code, explained what each step in the code does, and even offered alternatives if I didn't want to do it his way. 
I think the right balance between AI writing it and you is you making sure that it's ethical. Be honest when you used AI to assist you because it's a great tool but very easily misused and could be harmful for you in the long run. Don't use AI to write the whole code, but start the code yourself and when you struggle, ask AI for help or why it's showing this error message. I will personally be using it that way in the future. You can also ask for ways to make the code more efficient, or ask why this code is there if it gives you suggestions.
