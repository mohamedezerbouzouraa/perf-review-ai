def improvement_plan_generator(weak_areas: str, employee_name: str = "The employee", level: str = "mid") -> str:s
    
    try:
        prompt = (
            f"You are an experienced HR coach. Create a structured 90-day Personal Improvement Plan (PIP) "
            f"for {employee_name}, a {level}-level employee.\n\n"
            f"Weak areas identified:\n{weak_areas}\n\n"
            f"Structure the plan as follows:\n"
            f"- Month 1: Awareness & Foundation (what to learn and acknowledge)\n"
            f"- Month 2: Practice & Application (concrete actions to take)\n"
            f"- Month 3: Measurement & Validation (how success will be measured)\n\n"
            f"For each month provide 2-3 specific, measurable, and realistic milestones." )
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error generating improvement plan: {str(e)}"
