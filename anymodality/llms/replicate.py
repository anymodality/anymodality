import replicate
from typing import Any, Iterator, Union, List
from anymodality.llms.base import BaseLLM


class ReplicateLLM(BaseLLM):
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
