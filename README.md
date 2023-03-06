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
```

This code produces the following output:
```text
The Los Angeles Dodgers won the World Series in 2020.
[
    ChatGPTMessage(content='You are a helpful assistant.', role='system'),
    ChatGPTMessage(content='Who won the world series in 2020?', role='user'),
    ChatGPTMessage(content='The Los Angeles Dodgers won the World Series in 2020.', role='assistant')
]
```

