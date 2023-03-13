import logging

import openai
import tiktoken

from .input import ChatGPTMessage, ChatGPTInput, ChatGPTRole
from .output import ChatGPTOutput
from .util import get_logger


class ChatGPT:
    def __init__(self,
                 token: str,
                 model_name: str = "gpt-3.5-turbo",
                 show_log: bool = False,
                 system_prompt: str = None,
                 ):
        # OpenAI-API token registration
        openai.api_key = token

        self.model = model_name
        self.encoder = tiktoken.encoding_for_model(self.model)

        self.message_history: list[ChatGPTMessage] = []
        self.output_history: list[ChatGPTOutput] = []

        if system_prompt is not None:
            self.set_system_prompt(system_prompt)
        else:
            self.system_prompt = ""

        self.show_log = show_log
        self.logger = get_logger(logging.INFO)

    def set_system_prompt(self, prompt: str):
        self.system_prompt = prompt

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

    def save_history(self, message: ChatGPTMessage, output: ChatGPTOutput):
        self.message_history.append(message)
        self.output_history.append(output)

    def request_by_inputs(
            self,
            inputs: ChatGPTInput,
            continue_chat: bool = True,
            save_history: bool = True
    ) -> ChatGPTOutput:
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

        if self.show_log:
            self.logger.info(f"Input Messages: {inputs.messages}")
            self.logger.info(f"Waiting ChatGPT response...")

        response = openai.ChatCompletion.create(
            model=self.model,
            **(inputs.to_json_inputs())
        )

        response = ChatGPTOutput.from_json(response)
        message = response.choices[0].message

        if self.show_log:
            self.logger.info(f"Responded ChatGPT.")
            self.logger.info(f"Output Messages: {message}")

        if save_history:
            self.output_history.append(response)
            self.message_history += current_message
            self.message_history.append(message)

        return response

    def chat_by_inputs(
            self,
            inputs: ChatGPTInput,
            continue_chat: bool = True,
            save_history: bool = True
    ) -> str:
        """

        Args:
            continue_chat:
            inputs:
            save_history:

        Returns:

        """

        response = self.request_by_inputs(
            inputs=inputs, save_history=save_history, continue_chat=continue_chat
        )
        choice = response.choices[0]
        message = choice.message
        content = message.content

        return content

    def forget_history(self):
        self.message_history = []
        self.output_history = []

    def request(
            self,
            text: str | list,
            continue_chat: bool = True,
            save_history: bool = True
    ) -> ChatGPTOutput:
        if isinstance(text, str):
            text = [text]

        messages = [ChatGPTMessage(self.system_prompt, ChatGPTRole.system)]
        for t in text:
            messages.append(ChatGPTMessage(t, ChatGPTRole.user))
        inputs = ChatGPTInput(messages)

        response = self.request_by_inputs(
            inputs, continue_chat=continue_chat, save_history=save_history
        )
        return response

    def chat(
            self,
            text: str | list[str],
            continue_chat: bool = True,
            save_history: bool = True
    ) -> str:
        if isinstance(text, str):
            text = [text]

        messages = [ChatGPTMessage(self.system_prompt, ChatGPTRole.system)]
        for t in text:
            messages.append(ChatGPTMessage(t, ChatGPTRole.user))

        inputs = ChatGPTInput(messages)
        content = self.chat_by_inputs(
            inputs, continue_chat=continue_chat, save_history=save_history
        )
        return content


if __name__ == '__main__':
    pass
