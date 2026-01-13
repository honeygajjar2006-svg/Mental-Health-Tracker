def get_escape_plan(risk_level):
    """
    Provide coping strategies based on risk level.
    """
    plans = {
        "Low": "🧘 Relax, meditate, read, or take short walks.",
        "Moderate": "💬 Talk to friends/family, journal, or pick up hobbies.",
        "High": "📞 Seek professional help, therapy, or mental health resources immediately."
    }
    return plans.get(risk_level, "💡 Stay mindful and take care of yourself.")
