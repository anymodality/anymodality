import os
import replicate
from anymodality.llms.base import BaseLLM


class ReplicateLLM(BaseLLM):
    def __init__(self) -> None:
        super().__init__()
        if os.environ.get("REPLICATE_API_TOKEN") is None:
            raise Exception(
                "Please set your 'REPLICATE_API_TOKEN' as an environment variable."
            )

    def complete():
        pass

    # @staticmethod
    def visual_question_answer(
        self,
        model: str,
        input: dict,
        stream: bool = False,
    ):
        output = replicate.run(
            model,
            input=input,
        )
        return output

    def text_to_image(
        self,
        model: str,
        input: dict,
        stream: bool = False,
    ):
        pass
