"""
Product Update Task v2 - Executes configuration updates with extension support
"""

from crewai import Task

def create_update_task(product_updater_agent, analysis_task):
    """
    Creates the Product Update Task v2
    
    This task uses the analysis results to execute product configuration
    updates with the ProductConfigUpdaterTool, ensuring all parameters
    are provided to avoid validation errors.
    
    v2 Enhancement: Added support for extension code updates while
    preserving other configuration values.
    """
    
    return Task(
        description="""
            EXECUTION SEQUENCE:
                
                STEP 1: Parse the user request: "{prompt}"
                STEP 2: Get current configuration from previous task
                STEP 3: Use ProductConfigUpdaterTool with ALL parameters:
                
                MANDATORY: Always provide ALL parameters to avoid validation errors:
                - product_name: from previous task (always required)
                - section: new value if user requested change, otherwise current value from analysis
                - subsection: new value if user requested change, otherwise current value from analysis  
                - coverage: new value if user requested change, otherwise current value from analysis
                - extension: new extension dict if user requested extension code changes, otherwise null
                
                USER REQUEST: "{prompt}"
                
                Instructions:
                - If user says "update subsection to MOO", change subsection to "MOO" but keep current section and coverage
                - If user says "update section to XYZ", change section to "XYZ" but keep current subsection and coverage
                - If user says "code1 to E002 and code2 to EDU5", use extension: {{"code1": "E002", "code2": "EDU5"}}
                - ALWAYS provide all 5 parameters (product_name, section, subsection, coverage, extension) to avoid validation errors
                - For extension updates, keep current section/subsection/coverage values and provide the extension dict
                - For other updates, set extension to null if not being changed
                
                Example formats:
                For section/subsection updates:
                {{
                    "product_name": "TRE TreMoon Shop",
                    "section": "XYZ",
                    "subsection": "MOO", 
                    "coverage": "current_coverage_value",
                    "extension": null
                }}
                
                For extension code updates:
                {{
                    "product_name": "EDU EduTech Solutions",
                    "section": "current_section_value",
                    "subsection": "current_subsection_value",
                    "coverage": "current_coverage_value",
                    "extension": {{"code1": "E002", "code2": "EDU5"}}
                }}
           
            """,
        agent=product_updater_agent,
        expected_output="Update execution result with confirmation of all applied changes",
        context=[analysis_task],
    )