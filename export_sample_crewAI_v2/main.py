#!/usr/bin/env python
"""
Main Entry Point v2 - Enhanced with direct tool testing and extension support
"""

import sys
from configs.crew_configuration import ProductConfigurationCrew
from tools.config_updater_tool import update_product_config


def run():
    """
    Run the crew with sample input.
    """
    # Replace with your actual OpenAI API key
    api_key = "your-openai-api-key-here"
    crew = ProductConfigurationCrew(api_key)
    
    inputs = {
        "prompt": "Update the product EDU EduTech Solutions code1 to E999 and code2 to NEW2",
    }
    result = crew.create_crew().kickoff(inputs=inputs)
    print(result)


def train():
    """
    Train the crew for a given number of iterations.
    """
    if len(sys.argv) < 4:
        print("Usage: python main.py train <n_iterations> <filename>")
        sys.exit(1)
        
    # Replace with your actual OpenAI API key
    api_key = "your-openai-api-key-here"
    crew = ProductConfigurationCrew(api_key)
    
    inputs = {
        "prompt": "Update the product EDU EduTech Solutions code1 to E999 and code2 to NEW2",
    }
    try:
        crew.create_crew().train(
            n_iterations=int(sys.argv[2]), 
            filename=sys.argv[3], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    if len(sys.argv) < 3:
        print("Usage: python main.py replay <task_id>")
        sys.exit(1)
        
    # Replace with your actual OpenAI API key
    api_key = "your-openai-api-key-here"
    crew = ProductConfigurationCrew(api_key)
    
    try:
        crew.create_crew().replay(task_id=sys.argv[2])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    if len(sys.argv) < 4:
        print("Usage: python main.py test <n_iterations> <model_name>")
        sys.exit(1)
        
    # Replace with your actual OpenAI API key
    api_key = "your-openai-api-key-here"
    crew = ProductConfigurationCrew(api_key)
    
    inputs = {
        "prompt": "Update the product EDU EduTech Solutions code1 to E999 and code2 to NEW2",
    }
    try:
        crew.create_crew().test(
            n_iterations=int(sys.argv[2]), 
            openai_model_name=sys.argv[3], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def test_updater():
    """
    Test the updater tool directly with sample inputs.
    NEW in v2: Direct tool testing functionality
    """
    print("Testing ProductConfigUpdaterTool v2...")

    # Test case 1: Product with spaces - section/subsection update
    print("\nTest 1: TRE TreMoon Shop - Section/Subsection Update")
    result1 = update_product_config._run(
        product_name="TRE TreMoon Shop", 
        section="XYZ", 
        subsection="MOO",
        coverage="SVT"
    )
    print(f"Result: {result1}")

    # Test case 2: Extension code update
    print("\nTest 2: EDU EduTech Solutions - Extension Code Update")
    result2 = update_product_config._run(
        product_name="EDU EduTech Solutions", 
        section="CURRENT_SEC",
        subsection="CURRENT_SUB", 
        coverage="CURRENT_COV",
        extension={"code1": "E999", "code2": "NEW2"}
    )
    print(f"Result: {result2}")
    
    # Test case 3: Single extension code update
    print("\nTest 3: Simple Product - Single Extension Code")
    result3 = update_product_config._run(
        product_name="GAM GameZone Pro",
        section="GAMING",
        subsection="PRO",
        coverage="FULL",
        extension={"code1": "G001"}
    )
    print(f"Result: {result3}")

    # Test case 4: Multiple extension codes
    print("\nTest 4: Multiple Extension Codes")
    result4 = update_product_config._run(
        product_name="MED MediCare Plus",
        section="MEDICAL",
        subsection="CARE",
        coverage="PREMIUM",
        extension={"code1": "M001", "code2": "M002", "code3": "M003"}
    )
    print(f"Result: {result4}")


def demo():
    """
    Run demonstration of both basic and extension updates
    NEW in v2: Complete demonstration functionality
    """
    print("ProductConfigurationCrew v2 Demo")
    print("=" * 50)
    
    # Replace with your actual OpenAI API key
    api_key = "your-openai-api-key-here"
    crew = ProductConfigurationCrew(api_key)
    
    print("\n1. Testing Section/Subsection Update:")
    result1 = crew.run("Update the product TRE TreMoon Shop with section XYZ and subsection to MOO")
    print(f"Result: {result1}")
    
    print("\n2. Testing Extension Code Update:")
    result2 = crew.run("Update the product EDU EduTech Solutions code1 to E999 and code2 to NEW2")
    print(f"Result: {result2}")
    
    print("\n3. Testing Mixed Update:")
    result3 = crew.run("Update the product GAM GameZone Pro section to GAMES and code1 to G999")
    print(f"Result: {result3}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [<args>]")
        print("Commands:")
        print("  run           - Run the crew with sample input")
        print("  train         - Train the crew")
        print("  test          - Test the crew")
        print("  replay        - Replay from task ID")
        print("  test_updater  - Test the updater tool directly")
        print("  demo          - Run full demonstration")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    elif command == "test_updater":
        test_updater()
    elif command == "demo":
        demo()
    else:
        print(f"Unknown command: {command}")
        print("Available commands: run, train, test, replay, test_updater, demo")
        sys.exit(1)