import os

from rich import print

from chatgpt import ChatGPT

# Put your OpenAI API token here.
TOKEN = os.environ["OPENAI_TOKEN"]


def main():
    chatgpt = ChatGPT(token=TOKEN)

    # Get reply from ChatGPT
    reply = chatgpt.chat("What is the highest mountain in the world?")
    print(reply)


if __name__ == '__main__':
    main()
