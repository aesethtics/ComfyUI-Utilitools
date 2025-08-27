class UtilPassthrough:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": ("*",),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("output",)
    FUNCTION = "passthrough"
    CATEGORY = "Utilitools/Workflow"

    def passthrough(self, input):
        return (input,)


class UtilCounter:
    def __init__(self):
        self.counter = 0

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "increment": ("INT", {"default": 1, "min": -999, "max": 999, "step": 1}),
            },
            "optional": {
                "reset": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("count",)
    FUNCTION = "count"
    CATEGORY = "Utilitools/Workflow"

    def count(self, increment, reset=False):
        if reset:
            self.counter = 0
        self.counter += increment
        return (self.counter,)


class UtilShowWhatever:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "int_input": ("INT", {}),
                "float_input": ("FLOAT", {}),
                "string_input": ("STRING", {}),
                "image_input": ("IMAGE", {}),
                "latent_input": ("LATENT", {}),
                "conditioning_input": ("CONDITIONING", {}),
                "model_input": ("MODEL", {}),
                "vae_input": ("VAE", {}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "show"
    CATEGORY = "Utilitools/Workflow"
    OUTPUT_NODE = True

    def show(self, **kwargs):
        # Find which input was connected
        input_value = None
        input_name = "None"
        
        for key, value in kwargs.items():
            if value is not None:
                input_value = value
                input_name = key.replace("_input", "")
                break
        
        if input_value is None:
            value_str = "No input connected"
        else:
            # Format the value for display
            if hasattr(input_value, 'shape'):
                value_str = f"Tensor{input_value.shape} dtype={input_value.dtype}"
                if input_value.numel() <= 10:  # Show small tensors
                    value_str += f" = {input_value.flatten().tolist()}"
            elif isinstance(input_value, (list, tuple)):
                if len(input_value) <= 10:
                    value_str = f"{type(input_value).__name__} = {input_value}"
                else:
                    value_str = f"{type(input_value).__name__}[{len(input_value)}] = {str(input_value)[:100]}..."
            elif isinstance(input_value, dict):
                if len(input_value) <= 5:
                    value_str = f"Dict = {input_value}"
                else:
                    value_str = f"Dict with {len(input_value)} keys: {list(input_value.keys())[:5]}..."
            elif isinstance(input_value, str):
                if len(input_value) <= 200:
                    value_str = f'"{input_value}"'
                else:
                    value_str = f'"{input_value[:200]}..."'
            else:
                value_str = str(input_value)
        
        # Print to console for debugging
        print(f"Show Whatever ({input_name}): {value_str}")
        
        # Return for UI display in a text field
        return {"ui": {"text": [f"{input_name.upper()}: {value_str}"]}}


NODE_CLASS_MAPPINGS = {
    "UtilPassthrough": UtilPassthrough,
    "UtilCounter": UtilCounter,
    "UtilShowWhatever": UtilShowWhatever,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UtilPassthrough": "Passthrough",
    "UtilCounter": "Counter",
    "UtilShowWhatever": "Show Whatever",
}