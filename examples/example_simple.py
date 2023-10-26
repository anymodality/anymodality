from anymodality import Task
import sys

def sample_dialog_replicate_nonstreaming():
    task = Task("visual_question_answering")
    response = task(
        llm="replicate",
        model="daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423",
        input={
            "image": open("static/parking.jpg", "rb"),
            "prompt": "It is Wednesday at 4 pm. Can I park at the spot right now? Tell me in 1 line.",
        }
    )
    print(response)


def sample_dialog_replicate_streaming():
    task = Task("visual_question_answering")
    response = task(
        llm="replicate",
        model="yorickvp/llava-13b:2facb4a474a0462c15041b78b1ad70952ea46b5ec6ad29583c0b29dbd4249591",
        input={
            "image": open("static/parking.jpg", "rb"),
            "prompt": "It is Wednesday at 4 pm. Can I park at the spot right now? Tell me in 1 line.",
        },
        stream=True,
    )
    for res in response:
        sys.stdout.write(res)
    print()


if __name__ == "__main__":
    print("streaming response sample")
    sample_dialog_replicate_streaming()

    print("non streaming response sample")
    sample_dialog_replicate_nonstreaming()
