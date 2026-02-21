"""
Installation script for Comfy-Lora-Control

This script is automatically called by ComfyUI during the installation process.
Use it to install additional dependencies or perform setup tasks.
"""

import subprocess
import sys
import os


def install_requirements():
    """Install required packages from requirements.txt"""
    requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    
    if os.path.exists(requirements_path):
        try:
            print("[Comfy-Lora-Control] Installing requirements...")
            subprocess.check_call([
                sys.executable, 
                "-m", 
                "pip", 
                "install", 
                "-r", 
                requirements_path
            ])
            print("[Comfy-Lora-Control] Requirements installed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[Comfy-Lora-Control] Error installing requirements: {e}")
            return False
    else:
        print("[Comfy-Lora-Control] No requirements.txt found, skipping...")
        return True


def setup_directories():
    """Create necessary directories if they don't exist"""
    base_dir = os.path.dirname(__file__)
    directories = [
        "userdata",
        "models",
    ]
    
    for directory in directories:
        dir_path = os.path.join(base_dir, directory)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"[Comfy-Lora-Control] Created directory: {directory}")


def main():
    """Main installation function"""
    print("=" * 60)
    print("[Comfy-Lora-Control] Starting installation...")
    print("=" * 60)
    
    # Install requirements
    if not install_requirements():
        print("[Comfy-Lora-Control] Warning: Some requirements failed to install")
    
    # Setup directories
    setup_directories()
    
    print("=" * 60)
    print("[Comfy-Lora-Control] Installation completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
