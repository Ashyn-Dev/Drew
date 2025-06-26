"""
Crew Configuration - Main crew setup and orchestration
"""

import os
from crewai import Agent, Crew, Process, LLM
from crewai_tools import FileReadTool

# Import agents
from agents.product_analyzer_agent import create_product_analyzer_agent
from agents.product_updater_agent import create_product_updater_agent

# Import tasks
from tasks.analysis_task import create_analysis_task
from tasks.update_task import create_update_task


class ProductConfigurationCrew:
    """
    CrewAI setup for automated product configuration validation and updates.
    
    This crew uses two agents working sequentially:
    1. Product Analyzer - Extracts product info and gets current config
    2. Product Updater - Applies configuration updates
    """

    def __init__(self, openai_api_key: str):
        """
        Initialize the crew with API key and LLM configuration
        
        Args:
            openai_api_key: OpenAI API key for GPT model access
        """
        
        # Set up environment
        os.environ["OPENAI_API_KEY"] = openai_api_key
        
        # Configure LLM
        self.llm = LLM(model="gpt-4o-mini", temperature=0.1)
        
        # Create agents
        self.product_analyzer = create_product_analyzer_agent()
        self.product_updater = create_product_updater_agent()
        
        # Create tasks
        self.analysis_task = create_analysis_task(self.product_analyzer)
        self.update_task = create_update_task(self.product_updater, self.analysis_task)

    def create_crew(self) -> Crew:
        """
        Creates and returns the configured CrewAI crew
        
        Returns:
            Configured Crew instance ready for execution
        """
        
        return Crew(
            agents=[
                self.product_analyzer,
                self.product_updater,
            ],
            tasks=[
                self.analysis_task,
                self.update_task,
            ],
            process=Process.sequential,
            verbose=True,
            memory=True,
            max_execution_time=300,
            llm=self.llm,
        )

    def run(self, user_prompt: str):
        """
        Execute the crew with a user prompt
        
        Args:
            user_prompt: Natural language request for product configuration update
            
        Returns:
            Crew execution result
        """
        
        inputs = {"prompt": user_prompt}
        return self.create_crew().kickoff(inputs=inputs)


# Example usage
if __name__ == "__main__":
    # Initialize crew
    api_key = "your-openai-api-key-here"
    crew = ProductConfigurationCrew(api_key)
    
    # Run with sample input
    result = crew.run("Update the product TRE TreMoon Shop with section XYZ and subsection to MOO")
    print(result)