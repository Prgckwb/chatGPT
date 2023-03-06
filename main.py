import os

from rich import print

from chatgpt import ChatGPT, ChatGPTRole, ChatGPTInput

# Put your OpenAI API token here.
TOKEN = os.environ["OPENAI_TOKEN"]


def sample():
    chatgpt = ChatGPT(token=TOKEN)

    message = [
        chatgpt.create_message(content="日本語で答えてください", role=ChatGPTRole.system),
        chatgpt.create_message(content="日本の首都について詳しく教えてください", role=ChatGPTRole.user),
    ]
    inputs = ChatGPTInput(message)

    # Get reply from ChatGPT
    reply = chatgpt.chat(inputs)
    print(reply)

    # View history of conversations with ChatGPT
    print(chatgpt.message_history)


def main():
    chatgpt = ChatGPT(token=TOKEN)

    message = [
        chatgpt.create_message(content="日本語で答えてください", role=ChatGPTRole.system),
        chatgpt.create_message(content="日本の首都について詳しく教えてください", role=ChatGPTRole.user),
    ]
    inputs = ChatGPTInput(message)

    # Get reply from ChatGPT
    reply = chatgpt.chat(inputs)

    message = chatgpt.create_message("小さい男の子の口調で教えてください")
    inputs = ChatGPTInput(message)
    reply = chatgpt.chat(inputs, continue_chat=True)
    print(reply)

    print(chatgpt.message_history)




if __name__ == '__main__':
    main()
