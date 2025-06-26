"""
Product Configuration Updater Agent v2 - Updates product configurations with extension support
"""

from crewai import Agent, LLM
from tools.config_updater_tool import update_product_config

def create_product_updater_agent():
    """
    Creates the Product Configuration Updater Agent v2
    
    This agent parses user update requirements and executes 
    product configuration updates using the ProductConfigUpdaterTool.
    
    v2 Enhancement: Enhanced to handle extension code updates
    (code1, code2, code3) along with traditional section/subsection/coverage updates.
    """
    
    # Initialize LLM with deterministic settings
    llm = LLM(model="gpt-4o-mini", temperature=0.1)
    
    return Agent(
        role="Product Configuration Updater",
        goal="Parse user update requirements and execute product configuration updates including extension codes",
        backstory="You are a product configuration specialist who understands user update requests for sections, subsections, coverage, and extension codes (code1, code2, code3), and applies configuration changes using the appropriate tools.",
        tools=[update_product_config],
        llm_config={
            "temperature": 0.0,
            "seed": 42,
            "top_p": 0.1,
            "max_tokens": 1500,
        },
        max_iter=3,
        verbose=True,
    )