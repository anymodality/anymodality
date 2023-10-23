import pytest
from anymodality import Task


class TestClassVQAReplicate:
    def test_dialog_replicate(self):
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
        # assert response == "Yes, you can park at the spot right now."

    def test_dialog_sagemaker(self):
        task = Task("visual_question_answering")
        response = task(
            llm="sagemaker",
            model="huggingface-pytorch-inference-2023-10-23-06-30-14-719",
            input={
                "image": "https://raw.githubusercontent.com/haotian-liu/LLaVA/main/images/llava_logo.png",
                "question": "Describe the image and color details.",
            },
            stream=False,
        )
        print(response)
