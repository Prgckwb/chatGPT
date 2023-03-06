import dataclasses

import openai
import tiktoken


class ChatGPTRole:
    system = "system"
    user = "user"
    assistant = "assistant"


@dataclasses.dataclass
class ChatGPTMessage:
    content: str
    role: str

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
        """Create a chat history to be used for ChatGPT.

        Args:
            content: Chat content, sentence.
            role: Argument to determine who is speaking, selected from `ChatGPTRole`.

        Returns:

        """

        message = ChatGPTMessage(content=content, role=role)
        return message

    def count_token(self, sentence: str) -> int:
        """Calculate the number of tokens used in the ChatGPT

        Args:
            sentence: Sentence for which you want to calculate tokens.

        Returns:
            int: Number of tokens.

        """

        encoding = tiktoken.encoding_for_model(self.model)
        tokens = encoding.encode(sentence)
        num_tokens = len(tokens)
        return num_tokens

    def request(self,
                inputs: ChatGPTInput,
                save_history: bool = True) -> ChatGPTOutput:
        """Get data when querying ChatGPT's API.

        Args:
            inputs:
            save_history:

        Returns:

        """

        response = openai.ChatCompletion.create(
            model=self.model,
            **(inputs.to_json_inputs())
        )
        response = ChatGPTOutput.from_json(response)
        message = response.choices[0].message

        if save_history:
            self.output_history.append(response)
            self.message_history += inputs.messages
            self.message_history.append(message)

        return response

    def chat(self,
             inputs: ChatGPTInput,
             save_history: bool = True) -> str:
        """

        Args:
            inputs:
            save_history:

        Returns:

        """

        response = self.request(
            inputs=inputs, save_history=save_history
        )
        choice = response.choices[0]
        message = choice.message
        content = message.content

        return content

    def forget_history(self):
        self.message_history = []
        self.output_history = []


if __name__ == '__main__':
    pass
