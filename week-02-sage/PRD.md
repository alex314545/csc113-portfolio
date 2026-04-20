Product Requirements Document
Conversational Spending Tracker — MVP
Version: 1.0
Date: April 2026
Status: Draft

1. Project Overview
What It Does
A browser-based conversational assistant that lets users log expenses, set monthly budgets, and get plain-language spending summaries — all through a simple chat interface, with no account creation or backend required.
Who It's For
Primary users: College students and young professionals (ages 18–30) who manage their own finances for the first time and want a lightweight, low-friction way to stay on budget without committing to a full-featured finance app.
Problem It Solves
Most people only discover they've overspent when they check their bank statement at the end of the month — too late to correct course. Existing budgeting tools (spreadsheets, full-featured apps like Mint) create too much friction to use consistently. This app solves the awareness gap: by letting users log expenses in natural language mid-day (e.g., "I just spent $12 on lunch"), the assistant keeps a running picture of their spending and proactively surfaces insights before problems compound.

2. Core MVP Features
Feature 1: Conversational Expense Logging
Description: Users type expenses in plain English (e.g., "coffee $4.50", "paid $60 for groceries", "uber 14 bucks"). The assistant parses the amount, infers a spending category (food, transport, entertainment, etc.), confirms the entry, and stores it locally.
Why It Matters: The biggest barrier to expense tracking is friction. A chat box with zero setup removes every obstacle between having a thought ("I just spent money") and recording it. If logging takes under 5 seconds, users will actually do it.

Success Criteria:

User can log an expense in a single message with no required formatting
Assistant correctly parses amount and suggests category in ≥ 90% of common inputs
Entry is saved to localStorage and persists across page refresh
Confirmation reply appears within 1 second of user message
User can correct a misclassified category by replying (e.g., "that's entertainment, not food")


Feature 2: Budget Goal Setting
Description: Users set a monthly spending target per category or overall (e.g., "my food budget is $200 this month"). The assistant stores these targets and references them when logging new expenses. When a user is approaching or over their limit, the assistant flags it conversationally.
Why It Matters: Tracking without a target is just data collection — it produces no behavior change. A budget goal gives the assistant something to reason about, turning raw logs into actionable signals ("You're 80% through your food budget with 2 weeks left").

Success Criteria:

Users can set, update, or clear a budget in one conversational message
Budget thresholds trigger a warning message at 80% and 100% usage
Budget status is visible on demand ("how's my budget looking?")
Budgets persist in localStorage and reset at the start of each calendar month


Feature 3: Spending Summaries & Insights
Description: On request (or triggered weekly), the assistant generates a natural-language summary of spending: total spent, breakdown by category, remaining budget, and one actionable observation (e.g., "You're spending 3x more on food delivery than dining in — want to set a separate takeout limit?").
Why It Matters: Users need moments of reflection, not just data entry. A weekly plain-English summary is far more likely to drive behavior change than a raw number dump. It also demonstrates the assistant's value and keeps users engaged with the product.

Success Criteria:

User can trigger a summary with prompts like "how am I doing?", "spending summary", or "show me this week"
Summary includes: total spent, top 3 categories, budget remaining, and one insight
Insight is contextually relevant to the user's actual data (not generic advice)
Summary takes ≤ 2 seconds to generate from localStorage data


3. User Experience
First Screen
The user lands on a clean, single-column chat interface. There is no signup, no onboarding wizard, and no empty dashboard. The assistant greets them with a short, friendly message and a prompt to get started:

BudgetBot: Hey! I'm here to help you track your spending. Just tell me what you spent, like "lunch $9" or "set a $300 monthly food budget." What's up?

A subtle row of three suggestion pills below the input nudges new users: "Log an expense", "Set a budget", "See my summary".

Key Interactions

User Input                       Assistant Response
"coffee 4.50"                    "Got it — $4.50 on Coffee (Food & Drink). You've spent $47 on food this month. "
"set rent budget $1200"          "Done! I'll track your Housing budget at $1,200/month."
"how am I doing?"                Summary with totals, category breakdown, and one insight
"undo that last one"             "Removed: $4.50 Coffee. Want me to log something else?"
"this week's food"               Filters log to food category for current week

Interaction Flow
User types → Assistant parses intent (log / budget / query / undo)
           → Executes action on localStorage data
           → Replies in 1 sentence (confirmations) or paragraph (summaries)
           → Optional follow-up suggestion chips appear
Tone
Friendly, concise, and encouraging. The assistant celebrates good habits ("Nice, cooking at home!") and flags overages matter-of-factly without guilt-tripping.

4. Technical Constraints
Single page application
Must work in web browser
No server-side code needed

5. Out of Scope for V1
The following features are explicitly not being built for the MVP. This list exists to prevent scope creep.
Bank/card sync, User accounts & cloud sync, BudgetBot app (iOS/Android)
