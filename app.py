import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from database import initialize_database, save_user, save_plan, save_progress, get_progress

load_dotenv()
initialize_database()

st.set_page_config(page_title="FitBuddy | AI Fitness Planner", page_icon="💪", layout="wide")

st.markdown("""
<style>
.main { background-color: #f7f9fc; }
.hero {
    background: linear-gradient(120deg, #123c69, #1d976c);
    padding: 30px; border-radius: 18px; color: white; text-align: center;
}
.hero h1 { color: white; font-size: 42px; }
.hero p { color: #e8f5ee; font-size: 18px; }
div.stButton > button {
    background-color: #16865c; color: white; border-radius: 10px;
    border: none; padding: 12px 20px; font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

api_key = st.secrets.get("GEMINI_API_KEY") if "GEMINI_API_KEY" in st.secrets else os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL", "gemini-flash-latest")

st.markdown("""
<div class="hero">
  <h1>💪 FitBuddy</h1>
  <p>Your Personal AI Fitness Companion</p>
  <p>Train smarter. Eat better. Stay consistent.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.subheader("Create Your Personalized Fitness Plan")
st.write("Tell us about your goals and preferences to generate a general educational fitness plan.")

with st.form("fitness_form"):
    st.subheader("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name (optional)")
        age = st.number_input("Age", min_value=18, max_value=100, value=22)
        height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=300.0, value=65.0)
    with col2:
        gender = st.selectbox("Gender (optional)", ["Prefer not to say", "Female", "Male", "Other"])
        experience = st.selectbox("Fitness Experience", ["Beginner", "Intermediate", "Advanced"])
        activity = st.selectbox("Daily Activity", ["Low", "Moderate", "High"])

    st.subheader("Fitness Goals")
    goal = st.selectbox("Choose Your Goal", ["Muscle Gain", "Fat Loss", "General Fitness", "Strength Building", "Flexibility"])
    equipment = st.multiselect("Available Equipment", ["No Equipment", "Dumbbells", "Resistance Bands", "Gym Equipment", "Yoga Mat"], default=["No Equipment"])
    days = st.slider("Workout Days Per Week", min_value=1, max_value=7, value=3)
    session_time = st.selectbox("Workout Duration", ["15 minutes", "30 minutes", "45 minutes", "60 minutes"])

    st.subheader("Nutrition Preferences")
    diet = st.selectbox("Dietary Preference", ["Vegetarian", "Vegetarian with Eggs", "Non-Vegetarian", "Vegan", "No Specific Preference"])
    food_allergies = st.text_input("Food allergies or restrictions (optional)")
    additional_info = st.text_area("Anything else we should consider? (optional)", placeholder="Example: Home workouts, limited equipment...")
    consent = st.checkbox("I understand this is general educational guidance, not medical advice.")
    submitted = st.form_submit_button("✨ Generate My Fitness Plan", use_container_width=True)

if submitted:
    if not consent:
        st.error("Please confirm the disclaimer.")
    elif not equipment:
        st.error("Please select available equipment.")
    elif not api_key:
        st.error("Gemini API key is missing. Add it to your .env file or Streamlit secrets.")
    else:
        profile = f"""
Name: {name or 'Not provided'}
Age: {age}
Height: {height} cm
Weight: {weight} kg
Gender: {gender}
Fitness experience: {experience}
Daily activity: {activity}
Goal: {goal}
Equipment: {', '.join(equipment)}
Workout days per week: {days}
Session duration: {session_time}
Dietary preference: {diet}
Food allergies/restrictions: {food_allergies or 'None specified'}
Additional context: {additional_info or 'None'}
"""
        prompt = f"""
You are FitBuddy, a cautious and supportive general fitness education assistant.
Create a personalized general fitness plan based on this profile:
{profile}

Include:
1. Brief goal summary.
2. Weekly workout schedule with exercises, sets, reps, rest, and simple instructions.
3. Warm-up and cool-down suggestions.
4. General meal ideas matching dietary preference and respecting listed allergies.
5. Recovery and rest-day guidance.
6. Realistic consistency tips.
7. A note that results vary and no outcome is guaranteed.

Do not diagnose conditions, prescribe medications or supplements, claim medical approval,
or present calorie/protein targets as medically safe. Use clear Markdown headings.

SAFETY:
If the user mentions a medical condition, pregnancy, recent surgery, transplant,
significant injury, or medically restricted diet, do not provide a personalized
exercise or nutrition prescription. Instead, explain that they should consult their
treating clinician before following a plan.
End with a brief safety reminder.
"""
        try:
            with st.spinner("FitBuddy is creating your plan..."):
                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(model=model_name, contents=prompt)
                plan = response.text

            if not plan:
                st.error("The AI returned an empty response. Please try again.")
            else:
                st.success("Your fitness plan is ready!")
                st.markdown("---")
                st.header("🎯 Your Personalized Plan")
                st.markdown(plan)
                st.download_button("📥 Download Your Plan", data=plan, file_name="fitbuddy_plan.md", mime="text/markdown")

                user_id = save_user(name or "Guest", int(age), float(height), float(weight), goal)
                save_plan(user_id, plan)
                st.caption("Plan saved to the local SQLite database for this prototype.")
        except Exception as error:
            st.error("Could not generate the plan. Check your API key, model availability, internet connection, and API usage limits.")
            st.caption(f"Technical details: {error}")

st.markdown("---")
st.header("📊 Progress Tracker (Prototype)")
st.info("Progress tracking in this starter is local and session-independent only when you supply a user ID. Add authentication before multi-user deployment.")
progress_user_id = st.number_input("User ID for progress records", min_value=1, step=1, value=1)
progress_weight = st.number_input("Current weight (kg)", min_value=20.0, max_value=300.0, value=65.0, key="progress_weight")
workout_done = st.checkbox("I completed today's workout")
if st.button("Save Progress"):
    save_progress(int(progress_user_id), float(progress_weight), int(workout_done))
    st.success("Progress saved.")
records = get_progress(int(progress_user_id))
if records:
    import pandas as pd
    df = pd.DataFrame(records, columns=["Weight", "Workout Completed", "Date"])
    st.line_chart(df.set_index("Date")["Weight"])
    st.dataframe(df, use_container_width=True)

st.markdown("---")
st.caption("FitBuddy is an educational prototype, not a substitute for professional medical, nutrition, or rehabilitation advice.")
