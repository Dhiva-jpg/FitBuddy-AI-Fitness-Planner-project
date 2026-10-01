# FitBuddy – AI Fitness Plan Generator

A beginner-friendly Python + Streamlit prototype that uses Google's Gemini API to generate general fitness education plans based on user preferences. It includes a form, AI plan generation, Markdown download, and a local SQLite progress tracker.

> **Safety:** This is an educational prototype, not medical advice. It should not be used to prescribe exercise or nutrition for people with medical conditions, pregnancy, recent surgery, transplant, injury, or medically restricted diets. Consult a qualified clinician.

## Features
- Fitness profile and goal form
- Gemini-powered workout and meal-idea generation
- Basic prompt-level safety instructions
- Downloadable Markdown plan
- SQLite storage for profiles, plans, and progress
- Simple progress chart

## Requirements
- Python 3.11+
- VS Code (recommended)
- Gemini API key from [Google AI Studio](https://aistudio.google.com/)

## Setup (Windows PowerShell)

1. Extract the ZIP and open the `FitBuddy_AI_Fitness_Project` folder in VS Code.
2. Open Terminal in VS Code.
3. Create a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. Install packages:

   ```powershell
   pip install -r requirements.txt
   ```

5. Copy `.env.example` to `.env` and add your Gemini API key. Keep `.env private; do not upload it to GitHub.
6. Run the app:

   ```powershell
   streamlit run app.py
   ```

7. Open the local address printed in the terminal (usually `http://localhost:8501`).

## Suggested development roadmap

1. Confirm the MVP runs locally.
2. Improve prompts and use Gemini structured JSON output for predictable rendering.
3. Separate UI, AI, safety, and database code into modules.
4. Add robust application-level safety screening and manual review.
5. Implement user authentication and user-specific data access before multi-user use.
6. Improve progress charts and plan history.
7. Add automated tests for input validation, database functions, API failures, and safety cases.
8. Deploy with managed persistent storage. SQLite on ephemeral hosting may lose data on restart/redeploy.
9. Prepare a project report, screenshots, and demo.

## Important notes
- Model availability and quotas vary. If `gemini-flash-latest` is unavailable for your API project, set `GEMINI_MODEL` in `.env` to a supported model shown in Google AI Studio.
- The current safety prompt and keyword checks are not comprehensive medical screening. Do not present the application as clinically validated.
- The progress tracker is a prototype and does not provide secure user accounts.
