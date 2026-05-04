from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

from tools.performance_review import performance_review
from tools.tone_analyzer import tone_analyzer
from tools.rating_suggester import rating_suggester

def build_agent(llm):
    tools = [
        Tool(
            name="PerformanceReview",
            func=performance_review,
            description=(
                "Generates a professional HR performance review from raw bullet points. "
                "Input format: 'name|level|bullet1, bullet2, bullet3' "
                "Example: 'Sarah|senior|led 3 launches, missed 2 deadlines'"
            )
        ),
        Tool(
            name="ToneAnalyzer",
            func=tone_analyzer,
            description=(
                "Analyzes the tone of a performance review draft. "
                "Returns whether it is too harsh, too lenient, or well balanced, "
                "with suggestions to improve fairness and professionalism."
            )
        ),
        Tool(
            name="RatingSuggester",
            func=rating_suggester,
            description=(
                "Suggests a performance rating from 1 to 5 based on bullet points "
                "about an employee's work, with a short justification."
            )
        ),
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent
