# chatGPT

## Usage

```python
import os

from rich import print

from chatgpt import ChatGPT, ChatGPTRole

# Put your OpenAI API token here.
TOKEN = os.environ["OPENAI_TOKEN"]


def main():
    chatgpt = ChatGPT(token=TOKEN)

    messages = [
        chatgpt.create_message(content="日本語で答えてください", role=ChatGPTRole.system),
        chatgpt.create_message(content="AIとはなんですか?", role=ChatGPTRole.user),
    ]
    reply = chatgpt.chat(messages)
    print(reply)

if __name__ == '__main__':
    main()
```
