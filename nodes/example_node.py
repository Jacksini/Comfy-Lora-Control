"""
Example Custom Node for ComfyUI

This is a template node that demonstrates the basic structure of a ComfyUI custom node.
"""

class ExampleNode:
    """
    A simple example node that processes text input.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        Define the input parameters for this node.
        """
        return {
            "required": {
                "text": ("STRING", {
                    "default": "Hello ComfyUI!",
                    "multiline": True
                }),
                "multiplier": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 10,
                    "step": 1
                }),
            },
            "optional": {
                "prefix": ("STRING", {
                    "default": "",
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_text",)
    FUNCTION = "execute"
    CATEGORY = "Custom Nodes/Example"
    
    def execute(self, text, multiplier, prefix=""):
        """
        Execute the node logic.
        
        Args:
            text: Input text to process
            multiplier: Number of times to repeat the text
            prefix: Optional prefix to add
            
        Returns:
            Tuple containing the processed text
        """
        result = prefix + (text * multiplier)
        return (result,)


class ImageInfoNode:
    """
    A node that extracts information from images.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }
    
    RETURN_TYPES = ("STRING", "INT", "INT")
    RETURN_NAMES = ("info", "width", "height")
    FUNCTION = "get_image_info"
    CATEGORY = "Custom Nodes/Example"
    
    def get_image_info(self, image):
        """
        Get information about the image.
        
        Args:
            image: Input image tensor (B, H, W, C)
            
        Returns:
            Tuple containing info string, width, and height
        """
        # Image tensor shape: [batch, height, width, channels]
        batch, height, width, channels = image.shape
        
        info = f"Image: {width}x{height}, Batch: {batch}, Channels: {channels}"
        
        return (info, width, height)


# Register the nodes
NODE_CLASS_MAPPINGS = {
    "ExampleNode": ExampleNode,
    "ImageInfoNode": ImageInfoNode,
}

# Display names in the UI
NODE_DISPLAY_NAME_MAPPINGS = {
    "ExampleNode": "Example Text Node",
    "ImageInfoNode": "Image Info Node",
}
