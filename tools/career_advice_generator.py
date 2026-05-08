def career_advice_generator(employee_info: str) -> str:
    try:
        parts = [p.strip() for p in employee_info.split("|")]
        if len(parts) < 5:
            return "Invalid input. Please use format: 'name|current_level|target_role|strengths|weak areas'"

        name, current_level, target_role, strengths, weak_areas = parts

        prompt = (
            f"You are a senior career coach specializing in tech and corporate growth.\n\n"
            f"Employee Profile:\n"
            f"- Name: {name}\n"
            f"- Current Level: {current_level}\n"
            f"- Target Role: {target_role}\n"
            f"- Strengths: {strengths}\n"
            f"- Areas to Improve: {weak_areas}\n\n"
            f"Provide personalized career advice that includes:\n"
            f"1. How to leverage their strengths to reach {target_role}\n"
            f"2. Specific skills or certifications to pursue\n"
            f"3. A realistic timeline to achieve the target role\n"
            f"4. One motivational insight tailored to their profile")
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error generating career advice: {str(e)}"
