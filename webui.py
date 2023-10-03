import argparse
import gradio as gr
import os
import time
import replicate

# Chatbot demo with multimodal input (text, markdown, LaTeX, code blocks, image, audio, & video). Plus shows support for streaming text.

os.environ["REPLICATE_API_TOKEN"] = "r8_FYo7y8bU58DjKR7sDnJzjG0sGS9bDpu29ntlX"


models = {
    "daanelson/minigpt-4": "daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423",
    "joehoover/mplug-owl": "joehoover/mplug-owl:51a43c9d00dfd92276b2511b509fcb3ad82e221f6a9e5806c54e69803e291d6b",
    "joehoover/instructblip-vicuna13b": "joehoover/instructblip-vicuna13b:c4c54e3c8c97cd50c2d2fec9be3b6065563ccf7d43787fb99f84151b867178fe",
}
model_keys = list(models.keys())


def get_prompt(chat_history, system_prompt: str = ""):
    texts = [f"{system_prompt}"]

    for user_input, response in chat_history:
        texts.append(f"{user_input.strip()}{response.strip()}")
    # texts.append(f"{message.strip()} [/INST]")
    return "".join(texts)


def add_text(history, text):
    history = history + [(text, None)]
    return history, gr.Textbox(value="", interactive=False)


def add_file(history, file):
    history = history + [((file.name,), None)]
    return history


def bot(model_choice, history, image_path):
    print(model_choice)

    model_url = models[model_choice]

    history[-1][1] = ""
    prompt = get_prompt(history)
    print(prompt)

    image = open(image_path, "rb")
    if model_choice == "daanelson/minigpt-4":
        output = replicate.run(
            model_url,
            input={"prompt": prompt, "image": image},
        )
        response = output
    else:
        output = replicate.run(
            model_url,
            input={"prompt": prompt, "img": image},
        )
        response = ""
        for item in output:
            response += item

    for character in response:
        history[-1][1] += character
        time.sleep(0.05)
        yield history


with gr.Blocks() as demo:
    with gr.Row(elem_id="model_selector_row"):
        model_selector = gr.Dropdown(
            choices=model_keys,
            value=model_keys[0] if len(model_keys) > 0 else "",
            interactive=True,
            show_label=False,
            container=False,
        )
    # gr.Dropdown.update(choices=models, visible=True)

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
                f"static/parking.jpg",
                "It is Wednesday at 4 pm. Can I park at the spot right now? Tell me in 1 line.",
            ],
            [f"static/2b827.png", "Tell me the text in image."],
        ],
        inputs=[imagebox, textbox],
    )
    # txt_msg = textbox.submit(
    #     add_text, [chatbot, textbox], [chatbot, textbox], queue=False
    # ).then(bot, chatbot, chatbot)
    txt_msg = textbox.submit(
        add_text, [chatbot, textbox], [chatbot, textbox], queue=False
    ).then(bot, [model_selector, chatbot, imagebox], chatbot)

    # txt_msg.then(lambda: gr.Textbox(interactive=True), None, [textbox], queue=False)
    # file_msg = btn.upload(add_file, [chatbot, btn], [chatbot], queue=False).then(
    #     bot, chatbot, chatbot
    # )
    # send_btn.click(
    #     add_text,
    #     [model_selector, textbox],
    #     [state, chatbot, textbox] + btn_list,
    # )
    send_btn.click(add_text, [chatbot, textbox], [chatbot, textbox], queue=False).then(
        bot, [model_selector, chatbot, imagebox], chatbot
    )

    # file_msg = btn.upload(add_file, [chatbot, btn], [chatbot], queue=False).then(
    #     bot, chatbot, chatbot
    # )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=7860)
    parser.add_argument(
        "--share",
        action="store_true",
        help="Whether to generate a public, shareable link",
    )
    args = parser.parse_args()

    demo.queue()
    demo.launch(
        server_name=args.host,
        server_port=args.port,
        share=args.share,
        max_threads=200,
    )
