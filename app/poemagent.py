from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.memory import ConversationBufferMemory
from app.pipeline import get_pipeline
from app.tools import summarize_poem

hf_pipeline = get_pipeline()
llm = HuggingFacePipeline(pipeline=hf_pipeline)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

tools = [
    Tool(
        name="PoemSummarizer",
        func=summarize_poem,
        description="Summarize a poem using natural language."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True,
)

def run_agent(poem_text):
    prompt = f"""
    You are a poetic assistant. Read the poem below and follow this format:

    Thought: I should summarize the poem.
    Action: PoemSummarizer
    Action Input: {poem_text}
    """
    return agent.run(prompt)

run_agent("And all of you are worlds.")