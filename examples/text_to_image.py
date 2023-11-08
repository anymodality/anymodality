import base64
from anymodality import Task


def sample_stabilityai():
    task = Task("text_to_image")
    response = task(
        llm="stabilityai",
        input={
            "text_prompts": [{"text": "A lighthouse on a cliff"}],
        },
    )
    # response: list of image bytes str
    for i, image in enumerate(response):
        with open(f"./v1_txt2img_{i}.png", "wb") as f:
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
    # response: list of image bytes str
    from anymodality.tools.image import imgstr_to_PIL

    img_pil = imgstr_to_PIL(response[0])
    img_pil.show()


def sample_openai_url_dalle3():
    task = Task("text_to_image")
    response = task(
        llm="openai",
        input={
            "model": "dall-e-3",
            "prompt": "A cute baby sea otter",
            "size": "1024x1024",
            "n": 2,
        },
    )
    # response: list of image urls
    for i, img_url in enumerate(response):
        print(i)
        print(img_url)


def sample_openai_url_dalle2():
    task = Task("text_to_image")
    response = task(
        llm="openai",
        input={
            "model": "dall-e-2",
            "prompt": "A cute baby sea otter",
            "size": "1024x1024",
        },
    )
    # response: list of image urls
    for i, img_url in enumerate(response):
        print(i)
        print(img_url)


def sample_replicate():
    task = Task("text_to_image")
    response = task(
        llm="replicate",
        model="stability-ai/sdxl:2a865c9a94c9992b6689365b75db2d678d5022505ed3f63a5f53929a31a46947",
        input={
            "prompt": "An astronaut riding a rainbow unicorn",
            "num_outputs": 2,
        },
    )
    # response: list of image urls
    for i, img_url in enumerate(response):
        print(i)
        print(img_url)


def sample_replicate_without_version():
    task = Task("text_to_image")
    response = task(
        llm="replicate",
        model="stability-ai/sdxl",
        input={
            "prompt": "An astronaut riding a rainbow unicorn",
        },
    )
    # response: list of image urls
    for i, img_url in enumerate(response):
        print(i)
        print(img_url)


if __name__ == "__main__":
    print("StabilityAI text-to-image sample")
    sample_stabilityai()
    print("StabilityAI text-to-image and convert to pil sample")
    sample_stabilityai_pil()
    print("OpenAI text-to-image sample")
    sample_openai_url_dalle3()
    sample_openai_url_dalle2()
    print("Replicate text-to-image sample")
    sample_replicate()
    sample_replicate_without_version()
