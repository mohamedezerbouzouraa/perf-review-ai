def rating_suggester(bullet_points: str) -> str:
    try:
        prompt = (
            f"You are an HR evaluation expert. Based on the following bullet points "
            f"about an employee's performance, suggest a rating from 1 to 5 where:\n"
            f"1 = Poor | 2 = Below Expectations | 3 = Meets Expectations | "
            f"4 = Exceeds Expectations | 5 = Outstanding\n\n"
            f"Bullet points:\n{bullet_points}\n\n"
            f"Provide the rating and a 2-3 sentence justification."
        )
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error suggesting rating: {str(e)}"
