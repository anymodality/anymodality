import os
import requests
from typing import List

from anymodality.llms.base import BaseLLM


class OpenAILLM(BaseLLM):
    def __init__(self) -> None:
        super().__init__()
        if os.environ.get("OPENAI_API_KEY") is None:
            raise Exception(
                "Please set your 'OPENAI_API_KEY' as an environment variable."
            )

    def text_generation():
        pass

    # @staticmethod
    def vision(
        self,
        model: str = "gpt-4-vision-preview",
        input: dict = None,
        stream: bool = False,
    ):
        if stream:
            raise Exception("Stream is not supporting for OpenAI gpt-4-vision-preview.")
        url = "https://api.openai.com/v1/chat/completions"
        api_key = os.getenv("OPENAI_API_KEY")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        # process duplicate "model" argument
        if "model" not in input:
            input["model"] = model
        response = requests.post(
            url,
            headers=headers,
            json=input,
        )
        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))

        data = response.json()
        return data["choices"][0]["message"]["content"]

    def text_to_image(
        self,
        model: str = "dall-e-3",
        input: dict = None,
        stream: bool = False,
    ):
        if stream:
            raise Exception("Stream is not supporting for OpenAI text-to-image Task.")

        url = "https://api.openai.com/v1/images/generations"
        api_key = os.getenv("OPENAI_API_KEY")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        # process duplicate "model" argument
        if "model" not in input:
            input["model"] = model
        print(input)
        response = requests.post(
            url,
            headers=headers,
            json=input,
        )
        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))

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

    def image_to_image(
        self,
        model: str,
        input: dict = None,
        stream: bool = False,
    ) -> List[str]:
        pass
        # if stream:
        #     print("Stream is not supporting for OpenAI image-to-image Task.")
