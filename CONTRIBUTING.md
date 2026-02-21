# Contributing to Comfy-Lora-Control

Thank you for considering contributing to Comfy-Lora-Control! This document provides guidelines and steps for contributing.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - ComfyUI version and system information
   - Screenshots if applicable

### Suggesting Features

1. Check if the feature has been suggested before
2. Create a new issue with the "feature request" label
3. Describe the feature and its use case clearly

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes following our coding standards:
   - Follow PEP 8 style guide
   - Use meaningful variable and function names
   - Add docstrings to classes and functions
   - Keep functions focused and concise

4. Test your changes:
   - Load the nodes in ComfyUI
   - Test all functionality
   - Ensure no existing features are broken

5. Commit your changes:
   ```bash
   git commit -m "Add feature: brief description"
   ```

6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Create a Pull Request with:
   - Clear description of changes
   - Reference to related issues
   - Screenshots/examples if applicable

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/Comfy-Lora-Control.git
   cd Comfy-Lora-Control
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install black flake8 isort  # For code formatting
   ```

3. Create a symbolic link to ComfyUI's custom_nodes:
   ```bash
   # Windows
   mklink /D "C:\path\to\ComfyUI\custom_nodes\Comfy-Lora-Control" "C:\path\to\repo"
   
   # Linux/Mac
   ln -s /path/to/repo /path/to/ComfyUI/custom_nodes/Comfy-Lora-Control
   ```

## Code Style

### Python
- Follow PEP 8
- Use type hints where possible
- Maximum line length: 100 characters
- Use `black` for formatting: `black --line-length=100 .`
- Use `isort` for import sorting: `isort --profile black .`

### JavaScript
- Use ES6+ features
- Use meaningful variable names
- Add comments for complex logic

### Documentation
- Update README.md for new features
- Add docstrings to all functions and classes
- Include examples in docstrings

## Node Development Guidelines

When creating new nodes:

1. **Class Structure**:
   ```python
   class YourNode:
       @classmethod
       def INPUT_TYPES(cls):
           return {...}
       
       RETURN_TYPES = (...)
       RETURN_NAMES = (...)
       FUNCTION = "execute"
       CATEGORY = "Custom Nodes/YourCategory"
       
       def execute(self, ...):
           # Your logic here
           return (result,)
   ```

2. **Error Handling**:
   - Add try-except blocks for operations that might fail
   - Provide meaningful error messages
   - Log errors appropriately

3. **Performance**:
   - Optimize for speed when processing large batches
   - Avoid unnecessary operations
   - Cache results when appropriate

4. **Testing**:
   - Test with various input types and sizes
   - Test edge cases
   - Verify integration with other nodes

## Questions?

Feel free to open an issue for any questions about contributing!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
