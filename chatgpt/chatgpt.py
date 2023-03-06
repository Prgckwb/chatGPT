import dataclasses

import openai
import tiktoken


class ChatGPTRole:
    system = "system"
    user = "user"
    assistant = "assistant"


@dataclasses.dataclass
class ChatGPTMessage:
    role: str
    content: str

    @classmethod
    def from_json(cls, json_data):
        role = json_data["role"]
        content = json_data["content"]
        return cls(role, content)


@dataclasses.dataclass
class ChatGPTOutputUsage:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

    @classmethod
    def from_json(cls, json_data):
        prompt_tokens = json_data["prompt_tokens"]
        completion_tokens = json_data["completion_tokens"]
        total_tokens = json_data["total_tokens"]
        return cls(prompt_tokens, completion_tokens, total_tokens)


@dataclasses.dataclass
class ChatGPTOutputChoice:
    index: str
    message: ChatGPTMessage
    finish_reason: str

    @classmethod
    def from_json(cls, json_data):
        index = json_data["index"]
        message = ChatGPTMessage.from_json(json_data["message"])
        finish_reason = json_data["finish_reason"]
        return cls(index, message, finish_reason)


@dataclasses.dataclass
class ChatGPTOutput:
    id_: str
    object_: str
    created: int
    choices: list[ChatGPTOutputChoice]
    usage: ChatGPTOutputUsage

    @classmethod
    def from_json(cls, json_data):
        id_ = json_data["id"]
        object_ = json_data["object"]
        created = json_data["created"]
        choices = [ChatGPTOutputChoice.from_json(c) for c in json_data["choices"]]
        usage = ChatGPTOutputUsage.from_json(json_data["usage"])
        return cls(id_, object_, created, choices, usage)


class ChatGPT:
    def __init__(self, token: str, model_name: str = "gpt-3.5-turbo"):
        # OpenAI-API token registration
        openai.api_key = token

        self.model = model_name
        self.message_history: list[ChatGPTMessage] = []
        self.output_history: list[ChatGPTOutput] = []

    @staticmethod
    def create_message(content: str, role: str = ChatGPTRole.user) -> ChatGPTMessage:
        message = ChatGPTMessage(role, content)
        return message

    def count_token(self, sentence: str):
        encoding = tiktoken.encoding_for_model(self.model)
        tokens = encoding.encode(sentence)
        num_tokens = len(tokens)
        return num_tokens

    def request(self, messages: list[ChatGPTMessage], save_history: bool = True) -> ChatGPTOutput:
        messages = [dataclasses.asdict(m) for m in messages]
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages
        )
        response = ChatGPTOutput.from_json(response)

        if save_history:
            self.output_history.append(response)

        return response

    def chat(self, messages: list[ChatGPTMessage], save_history: bool = True) -> str:
        response = self.request(messages)
        choice = response.choices[0]
        message = choice.message
        content = message.content

        if save_history:
            self.message_history += messages
            self.message_history.append(message)
        return content
