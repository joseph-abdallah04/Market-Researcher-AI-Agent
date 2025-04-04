# Market Research Tools for AI Agent
# ==================================

# This file provides specialised tools that allow an AI agent to perform comprehensive 
# market research by accessing various online sources of information. 

# These tools enable the AI to:
# - Search the web for current market trends
# - Access academic research papers
# - Find information about competitors
# - Research industry-specific data 
# - Gather general knowledge from Wikipedia
# - And more.

# How it works:
# Each tools wraps and API or functionality that gives the aI access to different infromation
# sources. When the AI agent needs specific information, it can select the appropriate tool
# and use it to gather the data it needs. This modular approach allows for flexibility and
# scalability, as new tools can be added or existing ones modified without affecting 
# the overall system.

import os # Used to access environment variables that store API keys
from typing import List, Optional # Type hints for better code documentation

# Langchain tool imports - these are the building blocks for our reserach capabilities
from langchain.tools import BaseTool, StructuredTool, Tool # Base classes for all tools
from langchain_community.tools import WikipediaQueryRun, ArxivQueryRun, DuckDuckGoSearchRun # Tools for specific knowledge sources
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper # API wrappers for the rools
from langchain_community.tools.tavily_search import TavilySearchResults # Web search capability
from langchain_community.tools.pubmed import PubMedQueryRun # Medical research database



# --- GENERAL KNOWLEDGE TOOLS ---

# Wikipedia tool: Useful for basic facts, industry overviews, and general knowledge
# The AI can use this to understand general concepts and esatblished knowledge
wiki_tool = WikipediaQueryRun(
    description="Useful for general knowledge and quick facts. Use this to get a summary of a topic or concept.",
    search_type="search",
    api_wrapper=WikipediaAPIWrapper(),
)

# The below google search tool can be included in a future version. Requires API key in order to have access to google's search engine
# google_search_tool = GoogleSearchResults(
#     google_api_key=os.getenv("GOOGLE_API_KEY"),
#     google_cse_id=os.getenv("GOOGLE_CSE_ID"),
#     description="Use this to search the web for current trends, news articles, and general information.",
#     search_type="search",
# )

# --- ACAEDMIC & RESEARCH TOOLS ---

# Arxiv tool: Provides access to scientific papers and academic research
# Useful for cutting-edge market trends, technological innovations, and academic insights
arxiv_tool = ArxivQueryRun(api_wrapper=ArxivAPIWrapper())

# PubMed tool: provides access to medical research papers
# Essential if researching healthcare, biotech, pharmaceutical markets, etc.
pubmed_tool = PubMedQueryRun(
    description="Search for medical and health-related research papers, useful for health industry market research.",
)

# --- WEB SEARCH TOOLS ---  

# Tavily Search: A comprehensive web search tool that can find recent information
# This requires an API key set as an environment variable (within the .env file)
tavily_search_tool = TavilySearchResults(
    max_results=5,
    description="Search the internet for market research, industry news and trends, business information, and financial data.",
)

# Duck Duck Go Search: A privacy-focused search engine that can be used to find information
# Provides different results than other search engines, increasing research diversity
search = DuckDuckGoSearchRun()
ddg_search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the internet for market research, industry news and trends, business information, and financial data.",
)

# --- CUSTOM SPECIALIZED TOOLS ---

# Potentially add custom tools that allow the AI to research specific companies, industries, or markets
# These would be custom-built tools that wrap around specific APIs or data sources
# Example: A tool that queries a specific database or API for industry reports