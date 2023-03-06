# chatGPT
Wrapper for openai package written in python, specialized for ChatGPT

## Installation

```
pip install -r requirements.txt
```

## Usage
The basic usage is as follows:

```python
import os

from rich import print

from chatgpt import ChatGPT, ChatGPTRole

# Put your OpenAI API token here.
TOKEN = os.environ["OPENAI_TOKEN"]


def main():
    chatgpt = ChatGPT(token=TOKEN)

    messages = [
        chatgpt.create_message(content="You are a helpful assistant.", role=ChatGPTRole.system),
        chatgpt.create_message(content="Who won the world series in 2020?", role=ChatGPTRole.user),
    ]
    reply = chatgpt.chat(messages)
    print(reply)

if __name__ == '__main__':
    main()
```
