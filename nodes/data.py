class UtilListCreate:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "item_0": ("*",),
                "item_1": ("*",),
                "item_2": ("*",),
                "item_3": ("*",),
                "item_4": ("*",),
                "item_5": ("*",),
                "item_6": ("*",),
                "item_7": ("*",),
            }
        }

    RETURN_TYPES = ("LIST",)
    RETURN_NAMES = ("list",)
    FUNCTION = "create_list"
    CATEGORY = "Utilitools/Data"

    def create_list(self, **kwargs):
        items = []
        for i in range(8):
            key = f"item_{i}"
            if key in kwargs and kwargs[key] is not None:
                items.append(kwargs[key])
        return (items,)


class UtilListIndex:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list": ("LIST",),
                "index": ("INT", {"default": 0, "min": 0, "max": 999, "step": 1}),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("item",)
    FUNCTION = "get_item"
    CATEGORY = "Utilitools/Data"

    def get_item(self, list, index):
        if index < len(list):
            return (list[index],)
        return (None,)


class UtilBatchController:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": ("*",),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64, "step": 1}),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("output",)
    FUNCTION = "control_batch"
    CATEGORY = "Utilitools/Data"

    def control_batch(self, input, batch_size):
        if hasattr(input, 'shape') and len(input.shape) > 0:
            if input.shape[0] != batch_size:
                if input.shape[0] > batch_size:
                    return (input[:batch_size],)
                else:
                    import torch
                    repeats = batch_size // input.shape[0] + (1 if batch_size % input.shape[0] > 0 else 0)
                    repeated = input.repeat(repeats, *([1] * (len(input.shape) - 1)))
                    return (repeated[:batch_size],)
        return (input,)


NODE_CLASS_MAPPINGS = {
    "UtilListCreate": UtilListCreate,
    "UtilListIndex": UtilListIndex,
    "UtilBatchController": UtilBatchController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UtilListCreate": "Create List",
    "UtilListIndex": "List Index",
    "UtilBatchController": "Batch Controller",
}