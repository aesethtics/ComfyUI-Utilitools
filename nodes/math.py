"""
Mathematical utility nodes for ComfyUI.

Provides basic arithmetic operations with optional float and int inputs.
"""


class UtilAdd:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "float_a": ("FLOAT", {"default": 0.0}),
                "float_b": ("FLOAT", {"default": 0.0}),
                "int_a": ("INT", {"default": 0}),
                "int_b": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int_result", "float_result")
    FUNCTION = "add"
    CATEGORY = "Utilitools/Math"

    def add(self, float_a=0.0, float_b=0.0, int_a=0, int_b=0):
        result = float_a + float_b + int_a + int_b
        return (int(result), float(result))


class UtilSubtract:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "float_a": ("FLOAT", {"default": 0.0}),
                "float_b": ("FLOAT", {"default": 0.0}),
                "int_a": ("INT", {"default": 0}),
                "int_b": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int_result", "float_result")
    FUNCTION = "subtract"
    CATEGORY = "Utilitools/Math"

    def subtract(self, float_a=0.0, float_b=0.0, int_a=0, int_b=0):
        result = (float_a + int_a) - (float_b + int_b)
        return (int(result), float(result))


class UtilMultiply:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "float_a": ("FLOAT", {"default": 1.0}),
                "float_b": ("FLOAT", {"default": 1.0}),
                "int_a": ("INT", {"default": 1}),
                "int_b": ("INT", {"default": 1}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int_result", "float_result")
    FUNCTION = "multiply"
    CATEGORY = "Utilitools/Math"

    def multiply(self, float_a=1.0, float_b=1.0, int_a=1, int_b=1):
        result = float_a * float_b * int_a * int_b
        return (int(result), float(result))


class UtilDivide:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "float_a": ("FLOAT", {"default": 1.0}),
                "float_b": ("FLOAT", {"default": 1.0}),
                "int_a": ("INT", {"default": 1}),
                "int_b": ("INT", {"default": 1}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int_result", "float_result")
    FUNCTION = "divide"
    CATEGORY = "Utilitools/Math"

    def divide(self, float_a=1.0, float_b=1.0, int_a=1, int_b=1):
        dividend = float_a * int_a
        divisor = float_b * int_b
        if divisor == 0:
            return (0, 0.0)
        result = dividend / divisor
        return (int(result), float(result))


class UtilCalculator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "expression": ("STRING", {"default": "2 + 2"}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int_result", "float_result")
    FUNCTION = "calculate"
    CATEGORY = "Utilitools/Math"

    def calculate(self, expression):
        try:
            import re
            allowed_chars = re.compile(r'^[0-9+\-*/().\s]+$')
            if not allowed_chars.match(expression):
                return (0, 0.0)
            result = eval(expression)
            return (int(result), float(result))
        except:
            return (0, 0.0)


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