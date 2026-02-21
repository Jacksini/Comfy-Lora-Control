"""
PreStartup Script for Comfy-Lora-Control

This script is executed by ComfyUI before the main application starts.
Use it for early initialization, dependency checking, or environment setup.
"""

import os
import sys


def check_dependencies():
    """Check if all required dependencies are available"""
    try:
        # Add your dependency checks here
        # Example:
        # import torch
        # import numpy
        print("[Comfy-Lora-Control] Dependency check passed")
        return True
    except ImportError as e:
        print(f"[Comfy-Lora-Control] Warning: Missing dependency: {e}")
        return False


def setup_environment():
    """Setup environment variables or paths if needed"""
    base_dir = os.path.dirname(__file__)
    
    # Add custom paths or environment variables
    # Example:
    # models_path = os.path.join(base_dir, "models")
    # if os.path.exists(models_path):
    #     os.environ["LORA_MODELS_PATH"] = models_path
    
    print(f"[Comfy-Lora-Control] Environment setup completed")


def main():
    """Main prestartup function"""
    print("=" * 60)
    print("[Comfy-Lora-Control] PreStartup script running...")
    print("=" * 60)
    
    # Check dependencies
    check_dependencies()
    
    # Setup environment
    setup_environment()
    
    print("[Comfy-Lora-Control] PreStartup completed successfully")
    print("=" * 60)


# This is called by ComfyUI before starting
if __name__ == "__main__":
    main()
