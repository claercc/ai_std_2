from openai import OpenAI
from app.core.config import OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME
from typing import Generator, Any
from app.memory.store import conversation_messages, add_message
# from app.services.memory import conversation_messages, add_message

# 从llm.client导入client
from app.llm.client import client
# client = OpenAI(
#     api_key=OPENAI_API_KEY,
#     base_url=OPENAI_BASE_URL
# )

# v3.0 流式輸出
def chat_stream(session_id: str, message: str) -> Generator[str, Any, Any]:
    messages = conversation_messages[session_id]
    # messages.append({"role": "user", "content": message})
    add_message(session_id, {"role": "user", "content": message})
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        stream=True
    )
    answer = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            answer += chunk.choices[0].delta.content
            yield chunk.choices[0].delta.content
    add_message(session_id, {"role": "assistant", "content": answer})
    print(conversation_messages[session_id])

# v1.0 普通輸出
# def chat(message: str) -> str:
#     response = client.chat.completions.create(
#         model=MODEL_NAME,
#         messages=[
#             {"role": "user", "content": message}
#         ]
#     )
#     return response.choices[0].message.content

# v2.0 流式輸出
# def chat_stream(message: str) -> Generator[str, Any, Any]:
#     response = client.chat.completions.create(
#         model=MODEL_NAME,
#         messages=[
#             {"role": "user", "content": message}
#         ],
#         stream=True
#     )
#     for chunk in response:
#         if chunk.choices[0].delta.content:
#             yield chunk.choices[0].delta.content