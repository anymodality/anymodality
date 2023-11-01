# AnyModality

AnyModality is an open-source library to simplify MultiModal LLM inference and deployment.

## Features

- Supporting MultiModal LLM API providers: [Replicate](https://replicate.com/), [Sagemaker](https://aws.amazon.com/sagemaker/)...
- Supporting MultiModal LLM models:  [LLaVA-1.5](https://github.com/haotian-liu/LLaVA), [MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4), [InstructBLIP](https://github.com/salesforce/LAVIS)...

## Contents

- [Install](#install)
- [Documentation](#documentation)
- [Usage](#usage)
  - [Call MultiModal LLM Endpoint](#call-multimodal-llm-endpoint)
  - [Start WebUI for Visual Question Answering](#start-webui-for-visual-question-answering)
- [Supporting Models](#supporting-models)

## Install

```bash
pip install anymodality
```

## Documentation

Full documentation can be found here [here](https://docs.anymodality.ai/).

Please check it out for the most up-to-date tutorials, how-to guides, references, and other resources!

## Usage 

### Call MultiModal LLM Endpoint

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

| Models                                                | Replicate                                                    | SageMaker                                                    | Huggingface  |
| ----------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------ |
| [LLaVA-1.5](https://github.com/haotian-liu/LLaVA)     | [llava-13b](https://replicate.com/yorickvp/llava-13b)        | self-hosting, [deployment](https://huggingface.co/anymodality/llava-v1.5-7b) | self-hosting |
| [MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4) | [minigpt-4](https://replicate.com/daanelson/minigpt-4)       | self-hosting                                                 | self-hosting |
| [InstructBLIP](https://github.com/salesforce/LAVIS)   | [instructblip-vicuna13b](https://replicate.com/joehoover/instructblip-vicuna13b) | self-hosting                                                 | self-hosting |
| [mPLUG-Owl](https://github.com/X-PLUG/mPLUG-Owl)      | [mplug-owl)](https://replicate.com/joehoover/mplug-owl)      | self-hosting                                                 | self-hosting |



