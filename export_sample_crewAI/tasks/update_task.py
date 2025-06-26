"""
Product Update Task - Executes configuration updates
"""

from crewai import Task

def create_update_task(product_updater_agent, analysis_task):
    """
    Creates the Product Update Task
    
    This task uses the analysis results to execute product configuration
    updates with the ProductConfigUpdaterTool, ensuring all parameters
    are provided to avoid validation errors.
    """
    
    return Task(
        description="""
            EXECUTION SEQUENCE:
                
                STEP 1: Parse the user request: "{prompt}"
                STEP 2: Get current configuration from previous task
                STEP 3: Use ProductConfigUpdaterTool with ALL parameters:
                
                MANDATORY: Always provide all 4 parameters to avoid validation errors:
                - product_name: from previous task
                - section: new value if user requested change, otherwise current value from analysis
                - subsection: new value if user requested change, otherwise current value from analysis  
                - coverage: new value if user requested change, otherwise current value from analysis
                
                USER REQUEST: "{prompt}"
                
                Instructions:
                - If user says "update subsection to MOO", change subsection to "MOO" but keep current section and coverage
                - If user says "update section to XYZ", change section to "XYZ" but keep current subsection and coverage
                - Always include all parameters even if they don't change
                
                Example format:
                {{
                    "product_name": "TRE TreMoon Shop",
                    "section": "XYZ",
                    "subsection": "MOO", 
                    "coverage": "current_coverage_value"
                }}
           
            """,
        agent=product_updater_agent,
        expected_output="Update execution result",
        context=[analysis_task],
    )