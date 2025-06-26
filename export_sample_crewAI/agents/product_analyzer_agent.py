"""
Product Analyzer Agent - Extracts product information and retrieves current configuration
"""

from crewai import Agent, LLM
from crewai_tools import FileReadTool
from tools.get_product_config_tool import get_product_configuration

def create_product_analyzer_agent():
    """
    Creates the Product Analyzer Agent
    
    This agent extracts product names from user input and retrieves
    current product configuration data using specialized tools.
    """
    
    # Initialize LLM with deterministic settings
    llm = LLM(model="gpt-4o-mini", temperature=0.1)
    
    # Initialize file reading tool
    file_read_tool = FileReadTool(file_path="./products.txt")
    
    return Agent(
        role="Product Analyzer",
        goal="Extract product name from user input and retrieve current product configuration",
        backstory="You are a product analysis expert who extracts product names from user requests and retrieves their current configuration data.",
        tools=[
            file_read_tool,
            get_product_configuration,
        ],
        llm_config={
            "temperature": 0.0,
            "seed": 42,
            "top_p": 0.1,
            "max_tokens": 1500,
        },
        max_iter=3,
        verbose=True,
    )