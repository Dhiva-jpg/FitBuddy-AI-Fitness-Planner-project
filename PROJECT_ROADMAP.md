# FitBuddy – Complete Project Roadmap

## Project goal
Build a web application that accepts a user's fitness preferences and uses a Gemini model to generate general workout schedules and meal ideas. The app also demonstrates data persistence and progress visualization.

## Technology
- Python: application logic
- Streamlit: web interface
- Google Gemini API (`google-genai`): generative AI
- SQLite: local prototype database
- Pandas: progress data
- Git/GitHub: version control and portfolio

## Milestones
1. Environment setup: Python, VS Code, virtual environment, API key.
2. Interface: homepage, profile form, goals, equipment, dietary preferences.
3. Gemini integration: prompts, API error handling, output display.
4. Dashboard: readable results, weekly schedule, download.
5. Database: save profile, generated plans, progress.
6. Enhancements: chat assistant, plan history, progress charts.
7. Testing: normal, invalid, allergy, safety, API-failure, download cases.
8. Deployment: GitHub, Streamlit hosting, secrets configuration, persistent database.
9. Documentation: report, screenshots, architecture diagram, demo.

## Suggested 15-day schedule
| Day | Task |
|---|---|
| 1 | Install Python/VS Code and create project |
| 2 | Learn Streamlit basics and build homepage |
| 3 | Build user profile form |
| 4 | Create API key and test a Gemini call |
| 5 | Integrate Gemini |
| 6 | Workout prompt |
| 7 | Meal suggestions and safety rules |
| 8 | Results dashboard |
| 9 | Downloads and error handling |
| 10 | SQLite schema |
| 11 | Save profiles and plans |
| 12 | Progress tracking and charts |
| 13 | Test and fix bugs |
| 14 | Deploy and capture screenshots |
| 15 | Finish documentation and rehearse demo |

## Database design
- `users`: user_id, name, age, height, weight, goal
- `plans`: plan_id, user_id, generated_plan, created_at
- `progress`: progress_id, user_id, weight, workout_completed, recorded_at

## Testing checklist
- Valid profile generates a plan.
- Missing API key displays a helpful error.
- Missing equipment is rejected.
- Allergy information is respected and output is manually reviewed.
- Medical-risk input routes user to a clinician rather than prescribing.
- API/network/model errors do not crash the app.
- Downloaded plan opens correctly.
- Progress entries are saved and displayed.

## Report chapters
1. Introduction
2. Problem statement
3. Objectives
4. Existing system
5. Proposed system
6. System requirements
7. Architecture
8. Implementation
9. Testing
10. Screenshots
11. Limitations and safety
12. Future enhancements
13. Conclusion

## Architecture
User → Streamlit UI → Input validation → Python backend → Safety checks → Gemini API → Results dashboard → Download / SQLite → Progress tracker.

## Future improvements
Structured JSON responses, secure authentication, managed database, per-user access control, rate limiting, audit logging, clinician-reviewed safety rules, responsive UI, and automated tests.
