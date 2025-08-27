"""
Mathematical utility nodes for ComfyUI.

Provides basic arithmetic operations with both integer and float outputs.
"""


class UtilAdd:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0, "min": -999999.0, "max": 999999.0, "step": 0.001}),
                "b": ("FLOAT", {"default": 0.0, "min": -999999.0, "max": 999999.0, "step": 0.001}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int_result", "float_result")
    FUNCTION = "add"
    CATEGORY = "Utilitools/Math"

    def add(self, a, b):
        result = a + b
        return (int(result), float(result))


class UtilSubtract:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0, "min": -999999.0, "max": 999999.0, "step": 0.001}),
                "b": ("FLOAT", {"default": 0.0, "min": -999999.0, "max": 999999.0, "step": 0.001}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int_result", "float_result")
    FUNCTION = "subtract"
    CATEGORY = "Utilitools/Math"

    def subtract(self, a, b):
        result = a - b
        return (int(result), float(result))


class UtilMultiply:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 1.0, "min": -999999.0, "max": 999999.0, "step": 0.001}),
                "b": ("FLOAT", {"default": 1.0, "min": -999999.0, "max": 999999.0, "step": 0.001}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int_result", "float_result")
    FUNCTION = "multiply"
    CATEGORY = "Utilitools/Math"

    def multiply(self, a, b):
        result = a * b
        return (int(result), float(result))


class UtilDivide:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 1.0, "min": -999999.0, "max": 999999.0, "step": 0.001}),
                "b": ("FLOAT", {"default": 1.0, "min": -999999.0, "max": 999999.0, "step": 0.001}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int_result", "float_result")
    FUNCTION = "divide"
    CATEGORY = "Utilitools/Math"

    def divide(self, a, b):
        if b == 0:
            return (0, 0.0)
        result = a / b
        return (int(result), float(result))


class UtilCalculator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "expression": ("STRING", {"default": "2 + 2"}),
            }
        }

    RETURN_TYPES = ("FLOAT", "INT")
    RETURN_NAMES = ("float_result", "int_result")
    FUNCTION = "calculate"
    CATEGORY = "Utilitools/Math"

    def calculate(self, expression):
        try:
            import re
            allowed_chars = re.compile(r'^[0-9+\-*/().\s]+$')
            if not allowed_chars.match(expression):
                return (0.0, 0)
            result = eval(expression)
            return (float(result), int(result))
        except:
            return (0.0, 0)


NODE_CLASS_MAPPINGS = {
    "UtilAdd": UtilAdd,
    "UtilSubtract": UtilSubtract,
    "UtilMultiply": UtilMultiply,
    "UtilDivide": UtilDivide,
    "UtilCalculator": UtilCalculator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UtilAdd": "Add",
    "UtilSubtract": "Subtract", 
    "UtilMultiply": "Multiply",
    "UtilDivide": "Divide",
    "UtilCalculator": "Calculator",
}