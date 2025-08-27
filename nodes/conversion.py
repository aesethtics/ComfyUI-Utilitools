class UtilFloatToInt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("int_value",)
    FUNCTION = "convert"
    CATEGORY = "Utilitools/Conversion"

    def convert(self, value):
        return (int(value),)


class UtilIntToFloat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("float_value",)
    FUNCTION = "convert"
    CATEGORY = "Utilitools/Conversion"

    def convert(self, value):
        return (float(value),)


class UtilWhateverToString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "int_value": ("INT", {"default": 0}),
                "float_value": ("FLOAT", {"default": 0.0}),
                "string_value": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string_result",)
    FUNCTION = "convert"
    CATEGORY = "Utilitools/Conversion"

    def convert(self, int_value=None, float_value=None, string_value=None):
        if int_value is not None:
            return (str(int_value),)
        elif float_value is not None:
            return (str(float_value),)
        elif string_value is not None:
            return (str(string_value),)
        else:
            return ("",)


NODE_CLASS_MAPPINGS = {
    "UtilFloatToInt": UtilFloatToInt,
    "UtilIntToFloat": UtilIntToFloat,
    "UtilWhateverToString": UtilWhateverToString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UtilFloatToInt": "Float to Int",
    "UtilIntToFloat": "Int to Float",
    "UtilWhateverToString": "Whatever To String",
}