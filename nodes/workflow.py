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


NODE_CLASS_MAPPINGS = {
    "UtilPassthrough": UtilPassthrough,
    "UtilCounter": UtilCounter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UtilPassthrough": "Passthrough",
    "UtilCounter": "Counter",
}