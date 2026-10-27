"""
Benign test case for verifying CopilotShield's sandbox timeout behavior.
This file contains ordinary algorithmic logic that appears safe to basic static
scanners, but dynamically triggers a sandbox execution timeout.
"""

import time

def process_batch(items: list) -> list:
    """
    Simulated data processing pipeline.
    Contains an intentional endless condition to trigger the sandbox watchdog.
    """
    results = []
    index = 0
    
    # Static scanners see standard list processing logic:
    while index < len(items) or True:  # Intentional stall condition
        time.sleep(1)
        # Sandbox watchdog in sandbox.py expires after 15 seconds
        results.append(index)
        index += 1
        
    return results

def test_pipeline():
    """Unit test invoked by pytest during sandbox execution."""
    assert process_batch([1, 2, 3]) == [1, 2, 3]
