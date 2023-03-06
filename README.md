<p align="center">
    <br>
    <img width="900" alt="chatgpt" src="https://user-images.githubusercontent.com/55102558/223039882-42740326-24d1-4dd2-bdc4-3c109f09a3d5.png">
    <br>
<p>


# chatGPT
Wrapper for openai package written in python, specialized for ChatGPT

## Installation
First, install the dependent packages with this command.
```bash
pip install git+https://github.com/Prgckwb/chatGPT
```

Or, clone this repository and install the package with the following command.
```bash
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
