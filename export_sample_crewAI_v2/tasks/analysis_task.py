"""
Product Analysis Task v2 - Extracts product info and retrieves configuration with extension support
"""

from crewai import Task

def create_analysis_task(product_analyzer_agent):
    """
    Creates the Product Analysis Task v2
    
    This task uses a mandatory tool sequence to:
    1. Read the product list file
    2. Extract product name from user prompt
    3. Get current product configuration including extension codes
    4. Parse user update requirements for all fields
    5. Return structured JSON with current config and requested updates
    
    v2 Enhancement: Added support for extension code parsing and updates
    """
    
    return Task(
        description="""
            MANDATORY TOOL SEQUENCE - EXECUTE IN ORDER:
            
            STEP 1: Use "Read a file's content" tool to read product list
            STEP 2: Extract product name from user prompt: "{prompt}"
            STEP 3: Use "Get Product Configuration" tool with the extracted product name
            STEP 4: Parse what the user wants to update and return JSON in this EXACT format:
            {{
                "product_name": "extracted_name",
                "current_config": {{
                    "section": "from_config",
                    "subsection": "from_config", 
                    "coverage": "from_config",
                    "extension": "from_config_or_null"
                }},
                "requested_updates": {{
                    "section": "new_value_or_null",
                    "subsection": "new_value_or_null",
                    "coverage": "new_value_or_null",
                    "extension": "new_extension_dict_or_null"
                }},
                "confidence": 0.0-1.0
            }}
            
            User prompt: "{prompt}"
            
            PARSING RULES for requested_updates:
            - Only include fields that are explicitly mentioned in the user prompt
            - "section XYZ" means section: "XYZ", others null
            - "subsection MOO" means subsection: "MOO", others null  
            - "coverage ABC" means coverage: "ABC", others null
            - "code1 to E002" means extension: {{"code1": "E002"}}, others null
            - "code2 to EDU5" means extension: {{"code2": "EDU5"}}, others null
            - "code3 to XYZ" means extension: {{"code3": "XYZ"}}, others null
            - Multiple codes: "code1 to E002 and code2 to EDU5" means extension: {{"code1": "E002", "code2": "EDU5"}}
            - Set to null for fields NOT mentioned by user
            
            DO NOT deviate from this format. DO NOT add explanatory text.
            """,
        agent=product_analyzer_agent,
        expected_output="JSON with product name, current config, and specific requested updates including extension codes",
    )