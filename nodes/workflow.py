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


class UtilDateTimestamp:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "pre_text": ("STRING", {"default": ""}),
                "include_year": ("BOOLEAN", {"default": True}),
                "include_month": ("BOOLEAN", {"default": True}),
                "include_day": ("BOOLEAN", {"default": True}),
                "include_hour": ("BOOLEAN", {"default": False}),
                "include_minute": ("BOOLEAN", {"default": False}),
                "include_second": ("BOOLEAN", {"default": False}),
                "post_text": ("STRING", {"default": ""}),
                "separator": ("STRING", {"default": "-"}),
                "time_separator": ("STRING", {"default": "-"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("datetime_string",)
    FUNCTION = "generate"
    CATEGORY = "Utilitools/Workflow"

    def generate(self, pre_text="", include_year=True, include_month=True, include_day=True, 
                 include_hour=False, include_minute=False, include_second=False,
                 post_text="", separator="-", time_separator="-"):
        from datetime import datetime
        
        now = datetime.now()
        
        # Build date parts
        date_parts = []
        if include_year:
            date_parts.append(f"{now.year:04d}")
        if include_month:
            date_parts.append(f"{now.month:02d}")
        if include_day:
            date_parts.append(f"{now.day:02d}")
        
        # Build time parts
        time_parts = []
        if include_hour:
            time_parts.append(f"{now.hour:02d}")
        if include_minute:
            time_parts.append(f"{now.minute:02d}")
        if include_second:
            time_parts.append(f"{now.second:02d}")
        
        # Combine parts
        result_parts = []
        if date_parts:
            result_parts.append(separator.join(date_parts))
        if time_parts:
            result_parts.append(time_separator.join(time_parts))
        
        if not result_parts:
            datetime_part = "timestamp"  # Fallback if nothing selected
        else:
            datetime_part = separator.join(result_parts) if len(result_parts) > 1 else result_parts[0]
        
        # Combine pre_text + datetime + post_text
        final_result = f"{pre_text}{datetime_part}{post_text}"
        return (final_result,)


NODE_CLASS_MAPPINGS = {
    "UtilPassthrough": UtilPassthrough,
    "UtilCounter": UtilCounter,
    "UtilDateTimestamp": UtilDateTimestamp,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UtilPassthrough": "Passthrough",
    "UtilCounter": "Counter",
    "UtilDateTimestamp": "Date Timestamp",
}