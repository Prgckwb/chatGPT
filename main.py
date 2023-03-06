import os
from rich import print
from chatgpt import ChatGPT, ChatGPTRole, ChatGPTInput

# Put your OpenAI API token here.
TOKEN = os.environ["OPENAI_TOKEN"]


def main():
    chatgpt = ChatGPT(token=TOKEN)

    message = [
        chatgpt.create_message(content="You are a helpful assistant.", role=ChatGPTRole.system),
        chatgpt.create_message(content="Who won the world series in 2020?", role=ChatGPTRole.user),
    ]
    inputs = ChatGPTInput(message)

    # Get reply from ChatGPT
    reply = chatgpt.chat(inputs)
    print(reply)

    # View history of conversations with ChatGPT
    print(chatgpt.message_history)


if __name__ == '__main__':
    main()
