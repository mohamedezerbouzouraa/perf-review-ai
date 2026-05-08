from langchain.llms.fake import FakeListLLM
from core.agent import build_agent

llm = FakeListLLM(responses=["Njarbou ntastiweh"])
agent = build_agent(llm)
if __name__ == "__main__":
    bullets = (
        "- led 3 successful product launches\n"
        "- missed 2 sprint deadlines\n"
        "- excellent communication with stakeholders\n"
        "- needs improvement in documentation\n"
        "- mentored 4 junior developers")
    print(agent.run(f"Generate a review for Sarah|senior|{bullets}"))
    print(agent.run(
        "Analyze the tone of: 'Sarah struggles significantly "
        "and fails to meet basic expectations.'"))
    print(agent.run(f"Suggest a rating based on:\n{bullets}"))
    print(agent.run(
        "Generate an improvement plan for: "
        "John|junior|poor documentation, misses deadlines"))
    print(agent.run(
        "Give career advice for: "
        "Sara|mid|tech lead|great communicator, team player|lacks system design skills"))
