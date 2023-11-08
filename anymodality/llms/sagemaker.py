import json
from anymodality.llms.base import BaseLLM


class SagemakerLLM(BaseLLM):
    def __init__(self):
        super().__init__()
        import boto3

        # client = boto3.client(
        #     service_name="sagemaker-runtime",
        #     aws_access_key_id=aws_access_key_id,
        #     aws_secret_access_key=aws_secret_access_key,
        #     region_name=aws_region_name,
        # )

        # Create a low-level client representing Amazon SageMaker Runtime
        self.sagemaker_runtime = boto3.client("sagemaker-runtime")

    def text_generation():
        pass

    # @staticmethod
    def vision(
        self,
        model: str,
        input: dict,
        stream: bool = False,
    ):
        # example input
        # input = (
        #     {
        #         "image": open("static/parking.jpg", "rb"),
        #         "prompt": "It is Wednesday at 4 pm. Can I park at the spot right now? Tell me in 1 line.",
        #     },
        # )

        if stream:
            # TODO
            return
            response = self.sagemaker_runtime.invoke_endpoint_with_response_stream(
                EndpointName=model,
                Body=json.dumps(input),
                ContentType="application/json",
                # Some JumpStart foundation models require explicit
                # acceptance of an end-user license agreement (EULA)
                # before deployment.
                # https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html
                CustomAttributes="accept_eula=true",
            )
        else:
            response = self.sagemaker_runtime.invoke_endpoint(
                EndpointName=model,
                ContentType="application/json",
                Body=json.dumps(input),
                # Some JumpStart foundation models require explicit
                # acceptance of an end-user license agreement (EULA)
                # before deployment.
                # https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html
                CustomAttributes="accept_eula=true",
            )
            response = response["Body"].read().decode("utf8")
        return response
