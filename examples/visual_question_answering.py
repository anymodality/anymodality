from anymodality import Task


def sample_replicate():
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


def sample_replicate_without_version():
    task = Task("visual_question_answering")
    response = task(
        llm="replicate",
        model="daanelson/minigpt-4",
        input={
            "image": open("static/parking.jpg", "rb"),
            "prompt": "It is Wednesday at 4 pm. Can I park at the spot right now? Tell me in 1 line.",
        },
        stream=False,
    )
    print(response)


if __name__ == "__main__":
    print("Replicate visual-question-answering sample")
    sample_replicate()
    sample_replicate_without_version()
