class UtilTextConcat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_a": ("STRING", {"default": ""}),
                "text_b": ("STRING", {"default": ""}),
            },
            "optional": {
                "separator": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "concat"
    CATEGORY = "Utilitools/Text"

    def concat(self, text_a, text_b, separator=""):
        return (text_a + separator + text_b,)


class UtilStringReplace:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": ""}),
                "find": ("STRING", {"default": ""}),
                "replace": ("STRING", {"default": ""}),
            },
            "optional": {
                "count": ("INT", {"default": -1, "min": -1, "max": 1000, "step": 1}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "replace"
    CATEGORY = "Utilitools/Text"

    def replace(self, text, find, replace, count=-1):
        if count == -1:
            return (text.replace(find, replace),)
        else:
            return (text.replace(find, replace, count),)


NODE_CLASS_MAPPINGS = {
    "UtilTextConcat": UtilTextConcat,
    "UtilStringReplace": UtilStringReplace,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UtilTextConcat": "Text Concatenation",
    "UtilStringReplace": "String Replace",
}