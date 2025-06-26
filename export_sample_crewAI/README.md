# CrewAI Product Configuration Sample

This directory contains the successful implementation components from the automated product configuration validation and update crew.

## Structure

```
export_sample_crewAI/
├── agents/                 # Agent definitions
│   ├── product_analyzer_agent.py
│   └── product_updater_agent.py
├── tasks/                  # Task definitions
│   ├── analysis_task.py
│   └── update_task.py
├── tools/                  # Custom CrewAI tools
│   ├── config_updater_tool.py
│   └── get_product_config_tool.py
├── configs/                # Configuration files
│   ├── crew_configuration.py
│   └── sample_products.txt
└── README.md
```

## Components

### Agents

1. **Product Analyzer Agent** (`agents/product_analyzer_agent.py`)
   - Extracts product names from natural language input
   - Retrieves current product configuration
   - Uses deterministic LLM settings for consistency

2. **Product Updater Agent** (`agents/product_updater_agent.py`)
   - Parses user update requirements
   - Executes configuration updates via API
   - Ensures all required parameters are provided

### Tasks

1. **Analysis Task** (`tasks/analysis_task.py`)
   - Mandatory tool sequence for data extraction
   - Returns structured JSON with current config and requested updates
   - Follows strict parsing rules for update requirements

2. **Update Task** (`tasks/update_task.py`)
   - Executes product configuration updates
   - Uses context from analysis task
   - Handles partial updates while preserving unchanged fields

### Tools

1. **ProductConfigUpdaterTool** (`tools/config_updater_tool.py`)
   - HTTP POST requests to `/api/products/name/{encoded_name}`
   - URL encoding for product names with spaces
   - Optional parameters for flexible updates

2. **Get Product Configuration** (`tools/get_product_config_tool.py`)
   - Retrieves current product configuration
   - HTTP GET requests to search API
   - Error handling for API failures

### Configuration

1. **Crew Configuration** (`configs/crew_configuration.py`)
   - Main crew orchestration class
   - Sequential process with memory enabled
   - Example usage and initialization

2. **Sample Products** (`configs/sample_products.txt`)
   - Sample product list for testing
   - Used by FileReadTool in analysis task

## Success Output

The crew successfully:
1. ✅ Extracted "TRE TreMoon Shop" from user input
2. ✅ Retrieved current config: section="ABC", subsection="TRE", coverage="AKH"
3. ✅ Parsed update requirements: section="XYZ", subsection="MOO"
4. ✅ Updated product configuration via API call
5. ✅ Returned structured result with all changes

## Key Features

- **URL Encoding**: Handles product names with spaces using `urllib.parse.quote`
- **Deterministic Processing**: Temperature=0.0, seed=42 for consistent results
- **Flexible Updates**: Optional parameters allow partial configuration updates
- **Error Handling**: Robust error handling for API failures
- **Sequential Processing**: Tasks executed in logical order with context sharing

## API Endpoint Format

```bash
POST http://localhost:3000/api/products/name/{encoded_product_name}
Content-Type: application/json

{
  "section": "XYZ",
  "subsection": "MOO",
  "coverage": "AKH"
}
```

## Usage

```python
from configs.crew_configuration import ProductConfigurationCrew

# Initialize crew
crew = ProductConfigurationCrew("your-openai-api-key")

# Run with natural language input
result = crew.run("Update the product TRE TreMoon Shop with section XYZ and subsection to MOO")
```