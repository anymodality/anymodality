import pytest
from anymodality import Task


class TestClassVQAReplicate:
    def test_dialog1(self):
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
