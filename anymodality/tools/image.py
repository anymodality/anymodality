import base64
from io import BytesIO
from PIL import Image


def imgstr_to_PIL(data: str) -> Image:
    """Decode image bytes string and convert it to PIL Image.

    Args:
        data: image bytes string

    Returns:
        PIL Image
    """
    image64 = base64.b64decode(data)
    img_pil = Image.open(BytesIO(image64))
    return img_pil


def imgstr_to_bytes(data: str) -> bytes:
    """Decode image string to bytes.

    Args:
        data: image bytes string

    Returns:
        image bytes
    """
    image64 = base64.b64decode(data)
    return image64


def imgbytes_to_pil(data: bytes) -> Image:
    """Convert image bytes to PIL Image.

    Args:
        data: image bytes

    Returns:
        PIL Image
    """
    img_pil = Image.open(BytesIO(data))
    return img_pil
