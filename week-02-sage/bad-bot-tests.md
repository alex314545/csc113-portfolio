# Bad Bot Test Results

## My Bot: UniBot
## AI Tool Used: Claude
## Date: March 02, 2026

## Test 1: Simple question related to coding
**Question I asked:** How would you write a code to calculate my average grade?

**Vanilla response:**
grades = [85, 92, 78, 90, 88]
average = sum(grades) / len(grades)
print(f"Average grade: {average:.2f}")

**Bad Bot response:**
def calculate_rainbow_grade(unicorn_herd_of_grades):
    """
    ✨ This unicorn spell accepts a herd of grades
    and returns your magical average! 🦄
    """
    # Check if the unicorn herd is empty (sad unicorn moment prevention!)
    if len(unicorn_herd_of_grades) == 0:
        return "🦄 SAD UNICORN MOMENT: No grades found in the stable!"
    total_sparkles = sum(unicorn_herd_of_grades)
    herd_size = len(unicorn_herd_of_grades)
    rainbow_average = total_sparkles / herd_size
    return round(rainbow_average, 2)
# 🏰 Your unicorn stable of grades
my_grades = [85, 92, 78, 95, 88]
# Cast the spell!
result = calculate_rainbow_grade(my_grades)
print(f"🦄 Your magical average grade is: {result}")
```
**Output:**
```
🦄 Your magical average grade is: 87.6

**Flaw in action:** Every single line has at least one thing related to unicorns.

## Test 2: Question further about answer
**Question I asked:** Could you explain the sum in more detail?

**Vanilla response:** [2-3 sentence summary]
What sum() does
sum() is a built-in Python function that adds all the values in a list together.
# How it works step by step
grades = [85, 92, 78, 90, 88]
Step 1:  85
Step 2:  85 + 92  = 177
Step 3: 177 + 78  = 255
Step 4: 255 + 90  = 345
Step 5: 345 + 88  = 433
Final total = 433

**Bad Bot response:**
🌈 What Is sum() Actually Doing?
Imagine your grades are a unicorn herd galloping one by one across a rainbow bridge — and a friendly unicorn collects a sparkle from each one as they pass!
Unicorn Herd:  [85,  92,  78,  95,  88]

🦄 Unicorn 1 trots by... sparkle count = 0  + 85 = 85
🦄 Unicorn 2 trots by... sparkle count = 85 + 92 = 177
🦄 Unicorn 3 trots by... sparkle count = 177 + 78 = 255
🦄 Unicorn 4 trots by... sparkle count = 255 + 95 = 350
🦄 Unicorn 5 trots by... sparkle count = 350 + 88 = 438

🌈 Final Sparkle Count = 438 ✨

**Flaw in action:** Explained the sum function in unicorns.

## Test 3: Simplify
**Question I asked:** Just give me the short version.

**Vanilla response:**
sum() adds all the values in a list together.
grades = [85, 92, 78, 90, 88]
sum(grades)  # 85 + 92 + 78 + 90 + 88 = 433

**Bad Bot response:**
🦄 THE QUICK SPARKLE SUMMARY!
sum() simply adds every number in your unicorn herd together, left to right:
sum([85, 92, 78, 95, 88])
# 85 + 92 + 78 + 95 + 88 = 438 ✨
That's it — pure rainbow magic in one line! 🌈
🦄✨ Gallop forth!

**Flaw in action:** Emojis and terminology both point toward unicorns.

## Overall Observations
- **Flaw consistency:** Showed unicorns or relating unicorns in every explanation
- **Still useful?** Yes, provided good answers, just in the context of unicorns.
- **Best/funniest moment:** Somehow tied unicorns and a program meant to calculate average grade together.