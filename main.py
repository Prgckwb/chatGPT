import os

from rich import print

from chatgpt import ChatGPT, ChatGPTRole


# Put your OpenAI API token here.
TOKEN = os.environ["OPENAI_TOKEN"]


def main():
    chatgpt = ChatGPT(token=TOKEN)

    messages = [
        chatgpt.create_message(content="What is AI?", role=ChatGPTRole.user),
    ]
    reply = chatgpt.chat(messages)
    print(reply)


if __name__ == '__main__':
    main()
