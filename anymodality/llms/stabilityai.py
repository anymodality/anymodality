import os
import requests
from typing import List

from anymodality.llms.base import BaseLLM


class StabilityAILLM(BaseLLM):
    def __init__(self) -> None:
        super().__init__()
        if os.environ.get("STABILITY_API_KEY") is None:
            raise Exception(
                "Please set your 'STABILITY_API_KEY' as an environment variable."
            )

    def complete():
        pass

    def visual_question_answer(
        self,
        model: str,
        input: dict,
        stream: bool = False,
    ):
        pass

    def text_to_image(
        self,
        model: str,
        input: dict = None,
        stream: bool = False,
    ) -> List[str]:
        if stream:
            print("Stream is not supporting for StabilityAI text-to-image Task.")
        if model is None:
            model = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
        api_key = os.getenv("STABILITY_API_KEY")
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }

        response = requests.post(
            model,
            headers=headers,
            json=input,
        )

        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))

        # list of image bytes
        data = response.json()
        data_list = data["artifacts"]
        imgbytes_list = [data["base64"] for data in data_list]
        return imgbytes_list

    def image_to_image(
        self,
        model: str,
        input: dict = None,
        stream: bool = False,
    ) -> List[str]:
        if stream:
            print("Stream is not supporting for StabilityAI image-to-image Task.")
        if model is None:
            model = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image"
        api_key = os.getenv("STABILITY_API_KEY")
        headers = {"Accept": "application/json", "Authorization": f"Bearer {api_key}"}

        if "init_image" in input:
            files = {}
            files["init_image"] = input.pop("init_image")
        else:
            raise Exception("'init_image' is required in input.")

        response = requests.post(
            model,
            headers=headers,
            files=files,
            data=input,
        )

        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))

        # list of image bytes
        data = response.json()
        data_list = data["artifacts"]
        imgbytes_list = [data["base64"] for data in data_list]
        return imgbytes_list
