# AnyModality

AnyModality is an open-source library to simplify MultiModal LLM inference and deployment.

## Features

- Supporting MultiModal LLM API providers: [OpenAI](https://platform.openai.com/docs/api-reference/), [StabilityAI](https://stability.ai/), [Replicate](https://replicate.com/), [Sagemaker](https://aws.amazon.com/sagemaker/)...
- Supporting MultiModal LLM models:  [LLaVA-1.5](https://github.com/haotian-liu/LLaVA), [MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4), [InstructBLIP](https://github.com/salesforce/LAVIS)...
- Supporting tasks: `text-to-image`, `visual-question-answering`...

## Contents

- [Install](#install)
- [Documentation](#documentation)
- [Usage](#usage)
  - [Call MultiModal LLM Endpoint](#call-multimodal-llm-endpoint)
    - [Visuall Question Answering](#visual-question-answering)
    - [Text to Image](#text-to-image)
  - [Start WebUI for Visual Question Answering](#start-webui-for-visual-question-answering)
- [Supporting Models](#supporting-models)
  - [Visuall Question Answering](#visual-question-answering-1)
  - [Text to Image](#text-to-image-1)

## Install

```bash
pip install anymodality
```

## Documentation

Full documentation can be found here [here](https://docs.anymodality.ai/).

Please check it out for the most up-to-date tutorials, how-to guides, references, and other resources!

## Usage 

### Call MultiModal LLM Endpoint

#### Visual Question Answering

For Replicate [MiniGPT-4](https://replicate.com/daanelson/minigpt-4) endpoint:

```python
from anymodality import Task
task = Task("visual_question_answering")
response = task(
    llm="replicate",
    model="daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423",
    input={
        "image": open("static/parking.jpg", "rb"),
        "prompt": "It is Wednesday at 4 pm. Can I park at the spot right now? Tell me in 1 line.",
    },
    stream=False,
)
print(response)
```

For self-hosting SageMaker [LLaVA-1.5](https://github.com/haotian-liu/LLaVA) endpoint:

```python
from anymodality import Task
task = Task("visual_question_answering")
response = task(
    llm="sagemaker",
    model="huggingface-pytorch-inference-2023-10-29-02-29-37-677",
    input={
        "image": "https://raw.githubusercontent.com/haotian-liu/LLaVA/main/images/llava_logo.png",
        "question": "Describe the image and color details.",
    },
    stream=False,
)
print(response)
```

#### Text to Image

Example code can be found at [examples/text_to_image.py](./examples/text_to_image.py).

**StablityAI** 

```python
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
```

**OpenAI**

```python
task = Task("text_to_image")
response = task(
    llm="openai",
    model="https://api.openai.com/v1/images/generations",
    input={
        "prompt": "A cute baby sea otter",
        "n": 2,
        "size": "1024x1024",
    },
)
# response: list of image urls
```



### Start WebUI for Visual Question Answering

```
python -m anymodality.tools.webui
```

You can also parse llm provider and llm model (endpoint) to the webui:

```
python -m anymodality.tools.webui --llm replicate --model daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423
```

![screenshot](docs/assets/screenshot.png)

## Supporting Models

### Visual Question Answering

| Models                                                | Inference                                                    | Deployment                                                   |
| ----------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [LLaVA-1.5](https://github.com/haotian-liu/LLaVA)     | [Replicate](https://replicate.com/yorickvp/llava-13b), SageMaker | [SageMaker](https://huggingface.co/anymodality/llava-v1.5-7b) |
| [MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4) | [Replicate](https://replicate.com/daanelson/minigpt-4)       | NA                                                           |
| [InstructBLIP](https://github.com/salesforce/LAVIS)   | [Replicate](https://replicate.com/joehoover/instructblip-vicuna13b) | NA                                                           |
| [mPLUG-Owl](https://github.com/X-PLUG/mPLUG-Owl)      | [Replicate](https://replicate.com/joehoover/mplug-owl)      | NA                                                           |

### Text to Image

| Models                                                       | Inference                                                    | Deployment                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [DALL·E 2](https://openai.com/dall-e-2)                      | [OpenAI](https://openai.com/blog/dall-e-api-now-available-in-public-beta) | NA                                                           |
| [DALL·E 3](https://openai.com/blog/dall-e-3-is-now-available-in-chatgpt-plus-and-enterprise) | NA                                                           | NA                                                           |
| [Stable Diffusion XL](https://arxiv.org/abs/2307.01952)      | [StabilityAI](https://platform.stability.ai/sandbox/text-to-image), [Replicate](https://replicate.com/stability-ai/sdxl) | [Huggingface](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) |

