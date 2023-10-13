from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union

# from pydantic import BaseModel, Extra, Field, validator


class LLMType(Enum):
    UNKNOWN = 0
    REPLICATE = 1
    HUGGINGFACE = 2
    SAGEMAKER = 3

    @classmethod
    def get_type(cls, llm_name: str):
        llm_type = None
        llm_name = llm_name.lower()
        llm_name = "".join(letter for letter in llm_name if letter.isalnum())
        if "replicate" in llm_name:
            llm_type = LLMType.REPLICATE
        elif "huggingface" in llm_name:
            llm_type = LLMType.HUGGINGFACE
        elif "sagemaker" in llm_name:
            llm_type = LLMType.SAGEMAKER
        else:
            raise Exception("Unknown llm: " + llm_name)
            # llm_type = LLMType.UNKNOWN
        return llm_type


class BaseLLM(ABC):
    # API for https://api.openai.com/v1/chat/completion
    @abstractmethod
    def complete(self):
        pass

    @abstractmethod
    def visual_question_answer(self):
        pass
