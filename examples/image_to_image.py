import base64
from anymodality import Task


def sample_stabilityai():
    task = Task("image_to_image")
    response = task(
        llm="stabilityai",
        model="https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image",
        input={
            "init_image": open("./static/cat_1024.png", "rb"),
            "image_strength": 0.35,
            "init_image_mode": "IMAGE_STRENGTH",
            "text_prompts[0][text]": "Galactic dog with a cape",
            "text_prompts[0][weight]": 0.5,
            "cfg_scale": 7,
            "samples": 1,
            "steps": 30,
        },
    )

    # response: list of image bytes str
    for i, image in enumerate(response):
        with open(f"./v1_img2img_{i}.png", "wb") as f:
            f.write(base64.b64decode(image))


def sample_stabilityai_pil():
    task = Task("image_to_image")
    response = task(
        llm="stabilityai",
        input={
            "init_image": open("./static/cat_1024.png", "rb"),
            "init_image_mode": "IMAGE_STRENGTH",
            "text_prompts[0][text]": "Galactic dog with a cape",
        },
    )
    # response: list of image bytes str
    from anymodality.tools.image import imgstr_to_PIL

    img_pil = imgstr_to_PIL(response[0])
    img_pil.show()


if __name__ == "__main__":
    print("StabilityAI image-to-image sample")
    sample_stabilityai()
    sample_stabilityai_pil()
