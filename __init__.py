"""
ComfyUI Custom Nodes Package
"""

from .nodes.example_node import NODE_CLASS_MAPPINGS as EXAMPLE_MAPPINGS
from .nodes.example_node import NODE_DISPLAY_NAME_MAPPINGS as EXAMPLE_DISPLAY_MAPPINGS

# Combine all node mappings
NODE_CLASS_MAPPINGS = {
    **EXAMPLE_MAPPINGS,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **EXAMPLE_DISPLAY_MAPPINGS,
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
