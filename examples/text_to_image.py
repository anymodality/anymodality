import base64
from anymodality import Task


def sample_stabilityai():
    task = Task("text_to_image")
    response = task(
        llm="stabilityai",
        model="https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
        input={
            "text_prompts": [{"text": "A lighthouse on a cliff"}],
        },
    )
    # response: list of image bytes
    for i, image in enumerate(response):
        with open(f"./out/v1_txt2img_{i}.png", "wb") as f:
            f.write(base64.b64decode(image))


def sample_stabilityai_pil():
    task = Task("text_to_image")
    response = task(
        llm="stabilityai",
        model="https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
        input={
            "text_prompts": [{"text": "A lighthouse on a cliff"}],
            "samples": 1,
        },
    )
    # response: list of image bytes
    from anymodality.tools.image import imgstr_to_PIL

    img_pil = imgstr_to_PIL(response[0])
    img_pil.show()


if __name__ == "__main__":
    print("StabilityAI text-to-image sample")
    sample_stabilityai()
    print("StabilityAI text-to-image and convert to pil sample")
    sample_stabilityai_pil()
