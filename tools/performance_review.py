def performance_review(bullet_points: str, employee_name: str = "The employee", level: str = "mid") -> str:
    try:
        prompt = (
            f"You are an experienced HR professional. Based on the following bullet points "
            f"about a {level}-level employee named {employee_name}, write a structured, "
            f"professional, and balanced performance review. "
            f"Include: Strengths, Areas for Improvement, and an Overall Summary.\n\n"
            f"Bullet points:\n{bullet_points}"
        )
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error generating review: {str(e)}"
