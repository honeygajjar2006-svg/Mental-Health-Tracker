from predictor import predict_risk
from escape_plan import get_escape_plan


print("\n🧠 --- Mental Health Risk Analyzer ---\n")


sleep = float(input("💤 Sleep hours per day: "))
stress = int(input("😰 Stress level (1-10): "))
work = int(input("💼 Work hours per day: "))
social = int(input("👥 Social interaction (0-5): "))
exercise = int(input("🏃 Exercise days per week (0-7): "))

user_input = [sleep, stress, work, social, exercise]


model = None

risk = predict_risk(model, user_input)
plan = get_escape_plan(risk)


print(f"\n🔍 Risk Level: {risk}")
print(f"📋 Escape Plan: {plan}")
print("\n✅ Thank you for using Mental Health Risk Analyzer! Take care of your mind. 🌸\n")
