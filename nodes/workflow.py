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
            "required": {
                "input": ("*",),
            },
            "optional": {
                "label": ("STRING", {"default": "Value"}),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("output",)
    FUNCTION = "show"
    CATEGORY = "Utilitools/Workflow"
    OUTPUT_NODE = True

    def show(self, input, label="Value"):
        value_str = str(input)
        if hasattr(input, 'shape'):
            value_str = f"Tensor{input.shape} dtype={input.dtype}"
        elif isinstance(input, (list, tuple)):
            value_str = f"{type(input).__name__}[{len(input)}] = {str(input)[:100]}..."
        elif isinstance(input, dict):
            value_str = f"Dict with {len(input)} keys: {list(input.keys())[:5]}..."
        
        print(f"🔍 {label}: {value_str}")
        return {"ui": {"text": [f"{label}: {value_str}"]}, "result": (input,)}


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