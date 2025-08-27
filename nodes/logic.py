class UtilIfThenElse:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "condition": ("BOOLEAN", {"default": True}),
                "if_true": ("*",),
                "if_false": ("*",),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("result",)
    FUNCTION = "execute"
    CATEGORY = "Utilitools/Logic"

    def execute(self, condition, if_true, if_false):
        return (if_true if condition else if_false,)


class UtilSwitch:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "index": ("INT", {"default": 0, "min": 0, "max": 7, "step": 1}),
            },
            "optional": {
                "input_0": ("*",),
                "input_1": ("*",),
                "input_2": ("*",),
                "input_3": ("*",),
                "input_4": ("*",),
                "input_5": ("*",),
                "input_6": ("*",),
                "input_7": ("*",),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("selected",)
    FUNCTION = "switch"
    CATEGORY = "Utilitools/Logic"

    def switch(self, index, **kwargs):
        input_key = f"input_{index}"
        if input_key in kwargs and kwargs[input_key] is not None:
            return (kwargs[input_key],)
        return (None,)


class UtilBooleanAND:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("BOOLEAN", {"default": True}),
                "b": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "execute"
    CATEGORY = "Utilitools/Logic"

    def execute(self, a, b):
        return (a and b,)


class UtilBooleanOR:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("BOOLEAN", {"default": False}),
                "b": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "execute"
    CATEGORY = "Utilitools/Logic"

    def execute(self, a, b):
        return (a or b,)


class UtilBooleanNOT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "execute"
    CATEGORY = "Utilitools/Logic"

    def execute(self, value):
        return (not value,)


NODE_CLASS_MAPPINGS = {
    "UtilIfThenElse": UtilIfThenElse,
    "UtilSwitch": UtilSwitch,
    "UtilBooleanAND": UtilBooleanAND,
    "UtilBooleanOR": UtilBooleanOR,
    "UtilBooleanNOT": UtilBooleanNOT,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UtilIfThenElse": "If Then Else",
    "UtilSwitch": "Switch",
    "UtilBooleanAND": "Boolean AND",
    "UtilBooleanOR": "Boolean OR",
    "UtilBooleanNOT": "Boolean NOT",
}