"""
Product Analyzer Agent v2 - Extracts product information and retrieves current configuration with extension support
"""

from crewai import Agent, LLM
from crewai_tools import FileReadTool
from tools.get_product_config_tool import get_product_configuration

def create_product_analyzer_agent():
    """
    Creates the Product Analyzer Agent v2
    
    This agent extracts product names from user input and retrieves
    current product configuration data using specialized tools.
    
    v2 Enhancement: Enhanced parsing for extension codes and improved
    configuration handling for code1, code2, code3 updates.
    """
    
    # Initialize LLM with deterministic settings
    llm = LLM(model="gpt-4o-mini", temperature=0.1)
    
    # Initialize file reading tool
    file_read_tool = FileReadTool(file_path="./products.txt")
    
    return Agent(
        role="Product Analyzer",
        goal="Extract product name from user input and retrieve current product configuration including extension codes",
        backstory="You are a product analysis expert who extracts product names from user requests and retrieves their current configuration data, including extension codes like code1, code2, and code3.",
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