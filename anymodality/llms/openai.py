import os
import requests

from anymodality.llms.base import BaseLLM


class OpenAILLM(BaseLLM):
    def __init__(self) -> None:
        super().__init__()
        if os.environ.get("OPENAI_API_KEY") is None:
            raise Exception(
                "Please set your 'OPENAI_API_KEY' as an environment variable."
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
        pass

    def text_to_image(
        self,
        model: str = "https://api.openai.com/v1/images/generations",
        input: dict = None,
        stream: bool = False,
    ):
        if stream:
            print("Stream is not supporting for OpenAI text-to-image Task.")
        api_key = os.getenv("OPENAI_API_KEY")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        response = requests.post(
            model,
            headers=headers,
            json=input,
        )

        data = response.json()
        data_list = data["data"]
        # response_format:
        # The format in which the generated images are returned.
        # Must be one of url or b64_json.
        if "response_format" in input and input["response_format"] == "b64_json":
            imgbytes_list = [data["b64_json"] for data in data_list]
            return imgbytes_list
        else:
            imgurl_list = [data["url"] for data in data_list]
            return imgurl_list
