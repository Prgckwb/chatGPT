import os

from rich import print

from chatgpt import ChatGPT, ChatGPTRole

# Put your OpenAI API token here.
TOKEN = os.environ["OPENAI_TOKEN"]


def main():
    chatgpt = ChatGPT(token=TOKEN)

    messages = [
        chatgpt.create_message(
            role=ChatGPTRole.system,
            content="You are a helpful assistant."
        ),
        chatgpt.create_message(
            role=ChatGPTRole.user,
            content="Who won the world series in 2020?"
        ),
    ]

    reply = chatgpt.chat(messages)
    print(reply)


if __name__ == '__main__':
    main()
