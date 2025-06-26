"""
Get Product Configuration Tool - Retrieves product configuration data
"""

import requests
from urllib.parse import quote
from crewai.tools.base_tool import tool


@tool("Get Product Configuration")
def get_product_configuration(product_name: str) -> str:
    """
    Retrieves the current configuration for a specific product.
    
    This tool queries the mock server API to get the current
    section, subsection, and coverage values for a product.
    
    Args:
        product_name: The name of the product to get configuration for
        
    Returns:
        JSON string with product configuration data or error message
    """
    
    try:
        # URL encode the product name to handle spaces and special characters
        encoded_name = quote(product_name)
        url = f"http://localhost:3000/api/search?q={encoded_name}"
        
        response = requests.get(url)
        response.raise_for_status()
        
        return response.text
        
    except requests.exceptions.RequestException as e:
        return f"Error retrieving configuration for {product_name}: {e}"