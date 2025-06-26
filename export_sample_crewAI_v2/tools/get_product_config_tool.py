"""
Get Product Configuration Tool v2 - Retrieves product configuration data with enhanced search
"""

import requests
import json
from urllib.parse import quote
from crewai.tools import tool


@tool("Get Product Configuration")
def get_product_configuration(product_name: str) -> str:
    """
    Retrieves the current configuration for a specific product.
    
    This tool queries the mock server API to get the current
    section, subsection, coverage, and extension values for a product.
    
    v2 Enhancement: Improved search logic using first 3 characters
    and better error handling with JSON formatting.
    
    Args:
        product_name: The name of the product to get configuration for
        
    Returns:
        JSON string with product configuration data or error message
    """
    
    try:
        # Extract the first 3 characters for the API query (v2 enhancement)
        search_term = product_name[:3].upper() if len(product_name) >= 3 else product_name.upper()
        url = f"http://localhost:3000/api/search?q={search_term}"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse and format the response (v2 enhancement)
        data = response.json()
        
        if data.get("success", False) and "products" in data:
            products = data["products"]
            formatted_result = {
                "success": True,
                "total_products": len(products),
                "products": products,
            }
            return json.dumps(formatted_result, indent=2)
        else:
            return json.dumps({
                "success": False,
                "error": "No products found or invalid response format",
                "raw_response": data,
            })
        
    except requests.exceptions.RequestException as e:
        return json.dumps({
            "success": False,
            "error": f"API request failed: {str(e)}",
            "endpoint": url if "url" in locals() else "unknown",
        })
    except json.JSONDecodeError as e:
        return json.dumps({
            "success": False,
            "error": f"Invalid JSON response: {str(e)}",
            "raw_response": response.text if "response" in locals() else "unknown",
        })
    except Exception as e:
        return json.dumps({
            "success": False, 
            "error": f"Unexpected error: {str(e)}"
        })