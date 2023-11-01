import argparse
import gradio as gr
import os
import time
from anymodality import Task


# Chatbot demo with multimodal input (text, image).
def create_demo(llm, model, stream):
    def bot(history, image_path):
        # set response as none
        # for newest conversation (user_input, response)
        history[-1][1] = ""
        prompt = get_prompt(history)
        # print(prompt)

        task = Task("visual_question_answering")
        output = task(
            llm=llm,
            model=model,
            input={
                "image": open(image_path, "rb"),
                "prompt": prompt,
            },
            stream=stream,
        )
        if stream:
            response = ""
            for item in output:
                response += item
        else:
            response = output

        for character in response:
            history[-1][1] += character
            time.sleep(0.05)
            yield history

    def add_text(history, text):
        history = history + [(text, None)]
        return history, gr.Textbox(value="", interactive=False)

    def get_prompt(chat_history, system_prompt: str = ""):
        texts = [f"{system_prompt}"]

        for user_input, response in chat_history:
            texts.append(f"{user_input.strip()}{response.strip()}")
        # texts.append(f"{message.strip()} [/INST]")
        return "".join(texts)

    DESCRIPTION = """
    # AnyModality Webui
    """
    DESCRIPTION += "Provider: " + llm + "<br />"
    DESCRIPTION += "Model: " + model
    with gr.Blocks() as demo:
        gr.Markdown(DESCRIPTION)

        with gr.Row():
            chatbot = gr.Chatbot(
                [],
                elem_id="chatbot",
                bubble_full_width=False,
                avatar_images=(
                    None,
                    (os.path.join(os.path.dirname(__file__), "./static/avatar.png")),
                ),
            )
            imagebox = gr.Image(type="filepath")
        with gr.Row():
            with gr.Column(scale=20):
                textbox = gr.Textbox(
                    scale=4,
                    show_label=False,
                    placeholder="Enter text and press enter, or upload an image",
                    container=False,
                )
            with gr.Column(scale=1, min_width=50):
                send_btn = gr.Button(value="Send", variant="primary")

        gr.Examples(
            examples=[
                [
                    "static/parking.jpg",
                    "It is Wednesday at 4 pm. Can I park at the spot right now? Tell me in 1 line.",
                ],
                ["static/2b827.png", "Tell me the text in image."],
            ],
            inputs=[imagebox, textbox],
        )
        txt_msg = textbox.submit(
            add_text, [chatbot, textbox], [chatbot, textbox], queue=False
        ).then(bot, [chatbot, imagebox], chatbot)

        # txt_msg.then(lambda: gr.Textbox(interactive=True), None, [textbox], queue=False)
        send_btn.click(
            add_text, [chatbot, textbox], [chatbot, textbox], queue=False
        ).then(bot, [chatbot, imagebox], chatbot)
        return demo


def webui():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=7860)
    parser.add_argument(
        "--share",
        action="store_true",
        help="Whether to generate a public, shareable link",
    )
    parser.add_argument("--llm", type=str, default="replicate")
    parser.add_argument(
        "--model",
        type=str,
        default="daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423",
    )
    parser.add_argument("--stream", type=bool, default=False)

    args = parser.parse_args()

    demo = create_demo(args.llm, args.model, args.stream)
    demo.queue()
    demo.launch(
        server_name=args.host,
        server_port=args.port,
        share=args.share,
        max_threads=200,
    )


if __name__ == "__main__":
    webui()
