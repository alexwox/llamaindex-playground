import os
import asyncio
from dotenv import load_dotenv

from llama_index.tools.tavily_research import TavilyToolSpec
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool




async def main():
    # Load environment variables from ../.env
    load_dotenv(dotenv_path='../.env')

    # Access the OPENAI_API_KEY
    openai_api_key = os.getenv('OPENAI_API_KEY')
    #borsdata_api_key = os.getenv('BORSDATA_API_KEY')
    tavily_api_key = os.getenv('TAVILY_API_KEY')
        
    if openai_api_key is None:
        raise ValueError("OPENAI_API_KEY not found in the environment variables")
    #if borsdata_api_key is None:
    #    raise ValueError("BORSDATA_API_KEY not found in the environment variables")
    if tavily_api_key is None:
        raise ValueError("TAVILY_API_KEY not found in the environment variables")

    llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # Initialize the Tavily tool
    tavily_tool = TavilyToolSpec(
        api_key=tavily_api_key,
    )
    agent = ReActAgent.from_tools(tavily_tool.to_tool_list(), llm=llm, verbose=True)

    agent.chat('What happened in the latest Burning Man festival?')
    



if __name__ == "__main__":
    asyncio.run(main())