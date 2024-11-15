import asyncio
from playwright.async_api import async_playwright
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from playwright.sync_api import Page, expect
import re
from pydantic import BaseModel
from typing import Any

async def main():
    """Run without any arguments to get the title of the page"""
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        title = await page.title()
        await browser.close()
        return title

# Replace asyncio.run(main()) with:

title_tool = FunctionTool.from_defaults(
    async_fn=main,
    
)

# Initialize the LLM
llm = OpenAI(model="gpt-3.5-turbo")

# Create the ReAct agent with the tool and LLM
agent = ReActAgent.from_tools([title_tool], llm=llm, verbose=True)

agent.chat("What is the title of the page?")