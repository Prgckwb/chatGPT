from chatgpt.input import ChatGPTRole, ChatGPTMessage


def create_batch_messages(contents: list[str], role: str = ChatGPTRole.user) -> list[ChatGPTMessage]:
    """Create a batch of chat history to be used for ChatGPT.

    Args:
        contents: Chat content, sentence.
        role: Argument to determine who is speaking, selected from `ChatGPTRole`.

    Returns:

    """
    messages = [ChatGPTMessage(content, role) for content in contents]
    return messages
