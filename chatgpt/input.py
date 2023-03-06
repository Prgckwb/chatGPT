import dataclasses


class ChatGPTRole:
    system = "system"
    user = "user"
    assistant = "assistant"


@dataclasses.dataclass
class ChatGPTMessage:
    content: str
    role: ChatGPTRole

    @classmethod
    def from_json(cls, json_data):
        role = json_data["role"]
        content = json_data["content"]
        return cls(role=role, content=content)


@dataclasses.dataclass
class ChatGPTInput:
    messages: list[ChatGPTMessage] | ChatGPTMessage
    temperature: float = 1.0
    top_p: float = 1.0
    num_choices_per_input: int = 1
    stream: bool = False
    stop: str | list[str] = None
    max_tokens: int = None
    presence_penalty: float = 0.0
    frequency_penalty: float = 0.0
    logit_bias = None
    user: str = None

    def __post_init__(self):
        # TODO: 条件指定をする
        # assert self.temperature == 1
        if isinstance(self.messages, ChatGPTMessage):
            self.messages = [self.messages]



    def to_json_inputs(self):
        args = dict()

        if isinstance(self.messages, ChatGPTMessage):
            msg = [self.messages]
        elif isinstance(self.messages, list):
            msg = self.messages
        else:
            raise TypeError

        args["messages"] = [dataclasses.asdict(m) for m in msg]
        args["temperature"] = self.temperature
        args["top_p"] = self.top_p
        args["n"] = self.num_choices_per_input
        args["stream"] = self.stream

        if self.stop is not None:
            args["stop"] = self.stop
        if self.max_tokens is not None:
            args["max_tokens"] = self.max_tokens

        args["presence_penalty"] = self.presence_penalty
        args["frequency_penalty"] = self.frequency_penalty

        if self.logit_bias is not None:
            args["logit_bias"] = self.logit_bias
        if self.user is not None:
            args["user"] = self.user

        return args
