from enum import Enum
from typing import Any, Iterator

from anymodality.llms.base import LLMType


class TaskType(Enum):
    UNKNOWN = 0
    TextGeneration = 1
    VisualQuestionAnswering = 2

    @classmethod
    def get_type(cls, task_name: str):
        task_type = None
        task_name = task_name.lower()
        task_name = "".join(letter for letter in task_name if letter.isalnum())
        if "textgeneration" in task_name:
            task_type = TaskType.TextGeneration
        elif "visualquestionanswering" in task_name:
            task_type = TaskType.VisualQuestionAnswering
        else:
            raise Exception("Unknown task: " + task_name)
            # task_type = TaskType.UNKNOWN
        return task_type


class Task:
    def __init__(self, task_name: str = "visual_question_answering"):
        self.task_name = task_name
        self.task_type = TaskType.get_type(task_name)

    def __call__(
        self, llm: str, model: str, input: dict, stream: bool = False, **kwargs: Any
    ) -> Any | Iterator[Any]:
        llm_type = LLMType.get_type(llm)
        if llm_type == LLMType.REPLICATE:
            from anymodality.llms.replicate import ReplicateLLM

            llm_object = ReplicateLLM()
        elif llm_type == LLMType.SAGEMAKER:
            from anymodality.llms.sagemaker import SagemakerLLM

            llm_object = SagemakerLLM()

        input = input if kwargs is None else {**input, **kwargs}

        if self.task_type == TaskType.VisualQuestionAnswering:
            response = llm_object.visual_question_answer(model, input, stream)

        return response
