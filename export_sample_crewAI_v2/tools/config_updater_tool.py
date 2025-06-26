"""
Product Configuration Updater Tool v2 - Updates product configurations via API with extension support
"""

import requests
from urllib.parse import quote
from typing import Optional, Dict, Any
from crewai.tools.base_tool import BaseTool


class ProductConfigUpdaterTool(BaseTool):
    """
    Tool for updating product configurations on a mock server.
    
    This tool sends HTTP POST requests to update product section,
    subsection, coverage, or extension codes. It handles URL encoding for
    product names with spaces and special characters.
    
    v2 Enhancement: Added support for extension code updates
    """
    
    name: str = "ProductConfigUpdaterTool"
    description: str = """Updates a product's configuration on the mock server.
    Use this tool to update product section, subsection, coverage, or extension codes.
    Only provide the parameters you want to update - others can be omitted.
    Extension should be a dict with code1, code2, and/or code3 keys."""

    def _run(
        self,
        product_name: str,
        section: Optional[str] = None,
        subsection: Optional[str] = None,
        coverage: Optional[str] = None,
        extension: Optional[Dict[str, str]] = None,
    ) -> str:
        """
        Updates a product's configuration
        
        Args:
            product_name: The name of the product to update
            section: New section value (optional)
            subsection: New subsection value (optional) 
            coverage: New coverage value (optional)
            extension: Extension codes dict like {"code1": "E999", "code2": "NEW2"} (optional)
            
        Returns:
            Success message with API response or error message
        """

        # URL encode the product name to handle spaces and special characters
        encoded_name = quote(product_name)
        url = f"http://localhost:3000/api/products/name/{encoded_name}"

        # Build payload with only provided values
        payload = {}
        if section is not None:
            payload["section"] = section
        if subsection is not None:
            payload["subsection"] = subsection
        if coverage is not None:
            payload["coverage"] = coverage
        if extension is not None:
            payload["extension"] = extension

        if not payload:
            return f"No updates specified for product {product_name}"

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return f"Successfully updated product {product_name} with {payload}. Response: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while updating product {product_name}: {e}"


# Create tool instance for use in agents
update_product_config = ProductConfigUpdaterTool()