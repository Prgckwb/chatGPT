import openai
import tiktoken

from .input import ChatGPTMessage, ChatGPTRole, ChatGPTInput
from .output import ChatGPTOutput




class ChatGPT:
    def __init__(self, token: str, model_name: str = "gpt-3.5-turbo"):
        # OpenAI-API token registration
        openai.api_key = token

        self.model = model_name
        self.encoder = tiktoken.encoding_for_model(self.model)

        self.message_history: list[ChatGPTMessage] = []
        self.output_history: list[ChatGPTOutput] = []

    def count_token(self, sentence: str) -> int:
        """Calculate the number of tokens used in the ChatGPT

        Args:
            sentence: Sentence for which you want to calculate tokens.

        Returns:
            int: Number of tokens.

        """

        tokens = self.encoder.encode(sentence)
        num_tokens = len(tokens)
        return num_tokens

    def check_tokenized_text(self, sentence: str):
        tokens = self.encoder.encode(sentence)
        text = ""
        for i in tokens:
            c = self.encoder.decode([i])
            if len(c) == 1 and ord(c) == 65533:
                text += f"{i}|"
            else:
                text += f"{c}|"
        return text

    def request(self,
                inputs: ChatGPTInput,
                continue_chat: bool = True,
                save_history: bool = True) -> ChatGPTOutput:
        """Get data when querying ChatGPT's API.

        Args:
            continue_chat:
            inputs:
            save_history:

        Returns:

        """
        if isinstance(inputs.messages, ChatGPTMessage):
            inputs.messages = [inputs.messages]
        current_message = inputs.messages

        if continue_chat:
            inputs.messages = self.message_history + current_message

        response = openai.ChatCompletion.create(
            model=self.model,
            **(inputs.to_json_inputs())
        )
        response = ChatGPTOutput.from_json(response)
        message = response.choices[0].message

        if save_history:
            self.output_history.append(response)
            self.message_history += current_message
            self.message_history.append(message)

        return response

    def chat(self,
             inputs: ChatGPTInput,
             continue_chat: bool = True,
             save_history: bool = True) -> str:
        """

        Args:
            continue_chat:
            inputs:
            save_history:

        Returns:

        """

        response = self.request(
            inputs=inputs, save_history=save_history, continue_chat=continue_chat
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
