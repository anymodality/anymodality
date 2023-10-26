from typing import Dict, Iterator
import replicate
from anymodality.llms.base import BaseLLM

from enum import Enum


class StreamingSupportType(Enum):
    NON_STREAMING = 0
    CAN_STREAMING = 1
    ONLY_STREAMING = 2

# TODO define a schema for model spec, including expected input/oputput
KNOWN_MODELS = {
    "mini_gpt4": {
        "model_str": "daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423",
        "streaming_mode": StreamingSupportType.NON_STREAMING,
        "input_schema": {},
        "output_schema": {},
    },
    "llava": {
        "model_str": "yorickvp/llava-13b:2facb4a474a0462c15041b78b1ad70952ea46b5ec6ad29583c0b29dbd4249591",
        "streaming_mode": StreamingSupportType.CAN_STREAMING,
        "input_schema": {},
        "output_schema": {},
    }
}

class ReplicateLLM(BaseLLM):
    def complete():
        pass

    def visual_question_answer(
        self,
        model: str,
        input: dict,
        stream: bool = False,
    ) -> Dict[str, str] | Iterator[str]:
        if stream:
            output: Iterator[str] = replicate.run(
                model,
                input=input,
            )
            return output
        else:
            output: Dict[str, str] = replicate.run(
                model,
                input=input,
            )
            return output

