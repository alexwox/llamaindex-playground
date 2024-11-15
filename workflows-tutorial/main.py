import os
import asyncio
from dotenv import load_dotenv
from llama_index.core.llms import ChatMessage
from llama_index.core.tools import ToolSelection, ToolOutput
from llama_index.core.workflow import Event

from typing import Any, List

from llama_index.core.llms.function_calling import FunctionCallingLLM
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.tools.types import BaseTool
from llama_index.core.workflow import Workflow, StartEvent, StopEvent, step

class InputEvent(Event):
    input: list[ChatMessage]


class ToolCallEvent(Event):
    tool_calls: list[ToolSelection]


class FunctionOutputEvent(Event):
    output: ToolOutput


async def main():
    # Load environment variables from ../.env
    load_dotenv(dotenv_path='../.env')

    # Access the OPENAI_API_KEY
    openai_api_key = os.getenv('OPENAI_API_KEY')
    borsdata_api_key = os.getenv('BORSDATA_API_KEY')

    if openai_api_key is None:
        raise ValueError("OPENAI_API_KEY not found in the environment variables")
    if borsdata_api_key is None:
        raise ValueError("BORSDATA_API_KEY not found in the environment variables")
    
    



if __name__ == "__main__":
    asyncio.run(main())