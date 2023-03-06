import dataclasses

from .input import ChatGPTMessage


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
