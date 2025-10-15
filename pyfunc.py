"""
Azure Function Echo Implementation

This module contains the echo function implementation for Azure Functions.
The actual function code is in the EchoFunction directory.
This file serves as a reference and can be used for local testing.
"""

import json


def echo_function(request_data):
    """
    Echo function that returns the input data back to the caller.
    
    Args:
        request_data: Input data to echo back
        
    Returns:
        Dictionary with echoed data
    """
    return {
        "echo": request_data,
        "message": "Data echoed successfully"
    }


if __name__ == "__main__":
    # Example usage
    test_data = {"test": "Hello, Azure Functions!"}
    result = echo_function(test_data)
    print(json.dumps(result, indent=2))
