from langchain.llms.fake import FakeListLLM
from core.agent import build_agent

llm = FakeListLLM(responses=["TESTT."])
agent = build_agent(llm)

if __name__ == "__main__":
    bullets = (
        "- led 3 successful product launches\n"
        "- missed 2 sprint deadlines\n"
        "- excellent communication with stakeholders\n"
        "- needs improvement in documentation\n"
        "- mentored 4 junior developers"
    )

    print(agent.run(f"Generate a review for Ezer |senior|{bullets}"))
    print(agent.run("Analyze the tone of this review: 'Ezer struggles significantly and fails to meet basic expectations.'"))

    print(agent.run(f"Suggest a rating for this employee based on:\n{bullets}"))
