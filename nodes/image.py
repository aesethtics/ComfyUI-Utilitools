class UtilImageDimensions:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT")
    RETURN_NAMES = ("width", "height", "batch_size")
    FUNCTION = "get_dimensions"
    CATEGORY = "Utilitools/Image"

    def get_dimensions(self, image):
        if len(image.shape) == 4:  # [batch, height, width, channels]
            batch_size, height, width, channels = image.shape
            return (width, height, batch_size)
        elif len(image.shape) == 3:  # [height, width, channels]
            height, width, channels = image.shape
            return (width, height, 1)
        else:
            return (0, 0, 0)


class UtilAspectRatio:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 512, "min": 1, "max": 8192, "step": 1}),
                "height": ("INT", {"default": 512, "min": 1, "max": 8192, "step": 1}),
            }
        }

    RETURN_TYPES = ("FLOAT", "STRING")
    RETURN_NAMES = ("ratio", "ratio_string")
    FUNCTION = "calculate_ratio"
    CATEGORY = "Utilitools/Image"

    def calculate_ratio(self, width, height):
        import math
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        ratio = width / height
        divisor = gcd(width, height)
        simplified_width = width // divisor
        simplified_height = height // divisor
        
        ratio_string = f"{simplified_width}:{simplified_height}"
        
        return (ratio, ratio_string)


NODE_CLASS_MAPPINGS = {
    "UtilImageDimensions": UtilImageDimensions,
    "UtilAspectRatio": UtilAspectRatio,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UtilImageDimensions": "Image Dimensions",
    "UtilAspectRatio": "Aspect Ratio",
}