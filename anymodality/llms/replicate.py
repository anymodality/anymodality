import os
import requests
from urllib.parse import urljoin
import posixpath

import replicate
from anymodality.llms.base import BaseLLM


def replicate_get(api_key, url):
    headers = {
        "Authorization": f"Token {api_key}",
    }
    response = requests.get(
        url,
        headers=headers,
    )
    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))
    return response


def get_model_version(api_key, model):
    url_path = posixpath.join(model, "versions")
    url = urljoin("https://api.replicate.com/v1/models/", url_path)
    response = replicate_get(api_key, url)
    version = response.json()["results"][0]["id"]
    return version


class ReplicateLLM(BaseLLM):
    def __init__(self) -> None:
        super().__init__()
        if os.environ.get("REPLICATE_API_TOKEN") is None:
            raise Exception(
                "Please set your 'REPLICATE_API_TOKEN' as an environment variable."
            )
        self.model_dict = {}

    def complete():
        pass

    # @staticmethod
    def visual_question_answer(
        self,
        model: str,
        input: dict,
        stream: bool = False,
    ):
        # if model without version like "daanelson/minigpt-4"
        # complete it with version like
        # "daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423"
        model = self.preprocess_url(model)
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
        if stream:
            print("Stream is not supporting for Replicate text-to-image Task.")
        # if model without version like "daanelson/minigpt-4"
        # complete it with version like
        # "daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423"
        model = self.preprocess_url(model)
        print(model)
        output = replicate.run(
            model,
            input=input,
        )
        # list of image urls
        return output

    def preprocess_url(self, url: str) -> str:
        api_key = os.getenv("REPLICATE_API_TOKEN")
        if ":" in url:
            # user input model:version
            # example: daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423
            version = url.split(":")[1]
            # if version not same as in self.model_dict
            # update version
            self.model_dict[url] = version
            return url
        elif "/" in url:
            # user input only model
            # example: daanelson/minigpt-4
            if url in self.model_dict:
                # get version from self.model_dict
                version = self.model_dict[url]
            else:
                version = get_model_version(api_key, url)
                # get newest version for model from Replicate
                # update version in self.model_dict
                self.model_dict[url] = version
            return url + ":" + version
        else:
            raise Exception(url + " is not setup correctly.")
