import os
import ollama
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from pydantic import BaseModel
import tools

load_dotenv()

class ResearchResponse(BaseModel):
    niche: str
    problemStatement: str
    moneyMakingOpportunities: str
    marketResearch: str
    targetAudience: str
    competitors: str
    pricingStrategy: str
    marketingStrategy: str
    productDevelopment: str
    problemFix: str
    featureList: str

llm = ChatOllama(model="deepseek-r1:32b")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [   
        (
            "system",
            """
            You are a business consultant. Take the user's query as a niche or problem to be solved
            and use the necessary tools to generate a comprehensive business plan. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

# Create the tools for market research. get_market_research_tools() is a function that returns a list of tools
AItools = [
    tools.wiki_tool, 
    tools.arxiv_tool, 
    tools.pubmed_tool, 
    tools.tavily_search_tool, 
    tools.ddg_search_tool
]
# These tools are used to gather information from various sources. When the AI agent needs specific information, it can select the appropriate tool

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=AItools,
)

agent_executor = AgentExecutor(agent=agent, tools=AItools, verbose=True)
query = input("What is your business idea or niche?\n")
raw_response = agent_executor.run(query=query)

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    print("Error parsing response:", e, "\nRaw response:", raw_response)