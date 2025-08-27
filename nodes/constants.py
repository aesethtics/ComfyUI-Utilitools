class UtilConstantInt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("INT", {"default": 0, "min": -999999, "max": 999999, "step": 1}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_value"
    CATEGORY = "Utilitools/Constants"

    def get_value(self, value):
        return (value,)


class UtilConstantFloat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0, "min": -999999.0, "max": 999999.0, "step": 0.001}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_value"
    CATEGORY = "Utilitools/Constants"

    def get_value(self, value):
        return (value,)


class UtilConstantString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_value"
    CATEGORY = "Utilitools/Constants"

    def get_value(self, value):
        return (value,)


NODE_CLASS_MAPPINGS = {
    "UtilConstantInt": UtilConstantInt,
    "UtilConstantFloat": UtilConstantFloat,
    "UtilConstantString": UtilConstantString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UtilConstantInt": "Constant Int",
    "UtilConstantFloat": "Constant Float",
    "UtilConstantString": "Constant String",
}