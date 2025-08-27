"""
Mathematical utility nodes for ComfyUI.

Provides basic arithmetic operations that accept any input type and return int, float, and string outputs.
"""


def _convert_to_number(value):
    """Convert input to a numeric value, handling any input type."""
    if isinstance(value, (int, float)):
        return value
    elif isinstance(value, str):
        try:
            if '.' not in value and 'e' not in value.lower():
                return int(value)
            else:
                return float(value)
        except ValueError:
            return 0.0
    else:
        try:
            return float(value)
        except (ValueError, TypeError):
            return 0.0


class UtilAdd:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("*",),
                "b": ("*",),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT", "STRING")
    RETURN_NAMES = ("int_result", "float_result", "string_result")
    FUNCTION = "add"
    CATEGORY = "Utilitools/Math"

    def add(self, a, b):
        num_a = _convert_to_number(a)
        num_b = _convert_to_number(b)
        result = num_a + num_b
        return (int(result), float(result), str(result))


class UtilSubtract:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("*",),
                "b": ("*",),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT", "STRING")
    RETURN_NAMES = ("int_result", "float_result", "string_result")
    FUNCTION = "subtract"
    CATEGORY = "Utilitools/Math"

    def subtract(self, a, b):
        num_a = _convert_to_number(a)
        num_b = _convert_to_number(b)
        result = num_a - num_b
        return (int(result), float(result), str(result))


class UtilMultiply:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("*",),
                "b": ("*",),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT", "STRING")
    RETURN_NAMES = ("int_result", "float_result", "string_result")
    FUNCTION = "multiply"
    CATEGORY = "Utilitools/Math"

    def multiply(self, a, b):
        num_a = _convert_to_number(a)
        num_b = _convert_to_number(b)
        result = num_a * num_b
        return (int(result), float(result), str(result))


class UtilDivide:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("*",),
                "b": ("*",),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT", "STRING")
    RETURN_NAMES = ("int_result", "float_result", "string_result")
    FUNCTION = "divide"
    CATEGORY = "Utilitools/Math"

    def divide(self, a, b):
        num_a = _convert_to_number(a)
        num_b = _convert_to_number(b)
        if num_b == 0:
            return (0, 0.0, "0")
        result = num_a / num_b
        return (int(result), float(result), str(result))


class UtilCalculator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "expression": ("STRING", {"default": "2 + 2"}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT", "STRING")
    RETURN_NAMES = ("int_result", "float_result", "string_result")
    FUNCTION = "calculate"
    CATEGORY = "Utilitools/Math"

    def calculate(self, expression):
        try:
            import re
            allowed_chars = re.compile(r'^[0-9+\-*/().\s]+$')
            if not allowed_chars.match(expression):
                return (0, 0.0, "0")
            result = eval(expression)
            return (int(result), float(result), str(result))
        except:
            return (0, 0.0, "0")


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