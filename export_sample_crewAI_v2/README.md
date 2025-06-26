# CrewAI Product Configuration Sample v2

This directory contains the enhanced implementation components from the automated product configuration validation and update crew, with support for extension code updates.

## What's New in v2

- **Extension Support**: Added support for updating extension codes (code1, code2, code3)
- **Enhanced Tools**: Updated ProductConfigUpdaterTool with extension parameter
- **Improved Parsing**: Better parsing rules for extension code updates
- **Test Functionality**: Added direct tool testing capabilities

## Structure

```
export_sample_crewAI_v2/
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
├── main.py                 # Entry point with test functionality
├── requirements.txt        # Dependencies
└── README.md
```

## Components

### Agents

1. **Product Analyzer Agent** (`agents/product_analyzer_agent.py`)
   - Extracts product names from natural language input
   - Retrieves current product configuration
   - Enhanced parsing for extension codes
   - Uses deterministic LLM settings for consistency

2. **Product Updater Agent** (`agents/product_updater_agent.py`)
   - Parses user update requirements including extension codes
   - Executes configuration updates via API
   - Ensures all required parameters are provided

### Tasks

1. **Analysis Task** (`tasks/analysis_task.py`)
   - Enhanced with extension field support
   - Mandatory tool sequence for data extraction
   - Returns structured JSON with current config and requested updates
   - Supports parsing extension code updates like "code1 to E999"

2. **Update Task** (`tasks/update_task.py`)
   - Enhanced to handle extension code updates
   - Executes product configuration updates
   - Uses context from analysis task
   - Handles partial updates while preserving unchanged fields

### Tools

1. **ProductConfigUpdaterTool** (`tools/config_updater_tool.py`)
   - **NEW**: Extension parameter support for code updates
   - HTTP POST requests to `/api/products/name/{encoded_name}`
   - URL encoding for product names with spaces
   - Optional parameters for flexible updates
   - Extension dict format: `{"code1": "E999", "code2": "NEW2"}`

2. **Get Product Configuration** (`tools/get_product_config_tool.py`)
   - Enhanced search functionality
   - Uses first 3 characters for API queries
   - Improved error handling and JSON formatting
   - HTTP GET requests to search API

### Configuration

1. **Crew Configuration** (`configs/crew_configuration.py`)
   - Main crew orchestration class
   - Sequential process with memory enabled
   - Example usage and initialization

2. **Sample Products** (`configs/sample_products.txt`)
   - Sample product list for testing
   - Used by FileReadTool in analysis task

3. **Main Entry Point** (`main.py`)
   - **NEW**: Direct tool testing functionality
   - Run, train, test, and replay commands
   - Example test cases for extension updates

## Success Output Examples

### Basic Section/Subsection Updates
The crew successfully:
1. ✅ Extracted "TRE TreMoon Shop" from user input
2. ✅ Retrieved current config: section="ABC", subsection="TRE", coverage="AKH"
3. ✅ Parsed update requirements: section="XYZ", subsection="MOO"
4. ✅ Updated product configuration via API call
5. ✅ Returned structured result with all changes

### Extension Code Updates (NEW)
The crew successfully:
1. ✅ Extracted "EDU EduTech Solutions" from user input
2. ✅ Retrieved current config with extension codes
3. ✅ Parsed extension requirements: "code1 to E999 and code2 to NEW2"
4. ✅ Updated extension codes via API call: `{"code1": "E999", "code2": "NEW2"}`
5. ✅ Preserved existing section/subsection/coverage values

## Key Features

- **Extension Code Support**: Handles individual extension code updates (code1, code2, code3)
- **URL Encoding**: Handles product names with spaces using `urllib.parse.quote`
- **Deterministic Processing**: Temperature=0.0, seed=42 for consistent results
- **Flexible Updates**: Optional parameters allow partial configuration updates
- **Enhanced Error Handling**: Robust error handling for API failures
- **Sequential Processing**: Tasks executed in logical order with context sharing
- **Direct Tool Testing**: Test individual tools without full crew execution

## API Endpoint Formats

### Basic Configuration Update
```bash
POST http://localhost:3000/api/products/name/{encoded_product_name}
Content-Type: application/json

{
  "section": "XYZ",
  "subsection": "MOO",
  "coverage": "AKH"
}
```

### Extension Code Update (NEW)
```bash
POST http://localhost:3000/api/products/name/{encoded_product_name}
Content-Type: application/json

{
  "section": "current_section",
  "subsection": "current_subsection",
  "coverage": "current_coverage",
  "extension": {
    "code1": "E999",
    "code2": "NEW2"
  }
}
```

## Usage

### Basic Crew Usage
```python
from configs.crew_configuration import ProductConfigurationCrew

# Initialize crew
crew = ProductConfigurationCrew("your-openai-api-key")

# Run with natural language input for section/subsection updates
result = crew.run("Update the product TRE TreMoon Shop with section XYZ and subsection to MOO")

# Run with extension code updates
result = crew.run("Update the product EDU EduTech Solutions code1 to E999 and code2 to NEW2")
```

### Direct Tool Testing (NEW)
```python
from main import test_updater

# Test the updater tool directly
test_updater()
```

### Command Line Usage (NEW)
```bash
# Run the crew
python main.py run

# Test the updater tool directly
python main.py test_updater

# Train the crew
python main.py train 5 training_data.json

# Test with iterations
python main.py test 3 gpt-4o-mini

# Replay from task
python main.py replay task_id_123
```

## Extension Code Parsing Rules

- `"code1 to E999"` → `extension: {"code1": "E999"}`
- `"code2 to NEW2"` → `extension: {"code2": "NEW2"}`
- `"code1 to E999 and code2 to NEW2"` → `extension: {"code1": "E999", "code2": "NEW2"}`
- Multiple codes supported in single update
- Other fields (section, subsection, coverage) preserved unless explicitly changed

## Migration from v1

1. Extension field now supported in all tools and tasks
2. ProductConfigUpdaterTool accepts `extension` parameter as dict
3. Analysis task parses extension code update requests
4. Update task handles extension updates while preserving other fields
5. Main.py includes testing functionality for direct tool validation