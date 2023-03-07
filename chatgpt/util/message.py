from chatgpt.input import ChatGPTRole, ChatGPTMessage


def create_message(content: str, role: ChatGPTRole = ChatGPTRole.user) -> ChatGPTMessage:
    """Create a chat history to be used for ChatGPT.

    Args:
        content: Chat content, sentence.
        role: Argument to determine who is speaking, selected from `ChatGPTRole`.

    Returns:

    """

    message = ChatGPTMessage(content=content, role=role)
    return message


def create_batch_messages(contents: list[str], role: ChatGPTRole = ChatGPTRole.user) -> list[ChatGPTMessage]:
    """Create a batch of chat history to be used for ChatGPT.

    Args:
        contents: Chat content, sentence.
        role: Argument to determine who is speaking, selected from `ChatGPTRole`.

    Returns:

    """
    messages = [create_message(content, role) for content in contents]
    return messages
