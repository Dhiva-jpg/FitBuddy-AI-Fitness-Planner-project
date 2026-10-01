# FitBuddy – Presentation Notes

## 60-second introduction
FitBuddy is an AI-powered fitness plan generator built using Python, Streamlit, and Google's Gemini API. It collects user preferences such as fitness goal, experience, available equipment, schedule, and dietary preference. Gemini generates a general workout and meal-idea plan, which users can review and download. A local SQLite database demonstrates storing plans and progress.

## Demo flow
1. Open the homepage.
2. Fill in a sample profile using non-sensitive demo data.
3. Select a goal, equipment, days, and dietary preference.
4. Accept the educational-use disclaimer.
5. Generate the plan and explain the Gemini API integration.
6. Download the Markdown plan.
7. Record a sample progress entry and show the chart.
8. Explain limitations and future improvements.

## Explain the technology
- Streamlit renders the web interface.
- Python validates input and constructs the prompt.
- Gemini generates natural-language plan suggestions.
- SQLite stores prototype data.
- Pandas prepares progress records for visualization.

## Be transparent about limitations
- Generative AI can make mistakes or produce inconsistent suggestions.
- The prototype is not clinically validated and is not a medical service.
- Safety instructions in prompts are not a substitute for robust screening.
- Authentication and multi-user access controls must be added before public production use.
- Hosted SQLite storage may not persist reliably; use a managed database for production.
