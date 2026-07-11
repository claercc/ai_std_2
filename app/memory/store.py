from collections import defaultdict

conversation_messages = defaultdict(list)

# 简单模拟历史记录 ，实际应用中需要更复杂的数据库存储
MAX_HISTORY = 10
def add_message(session_id: str, message: dict):
    conversation_messages[session_id].append(message)
    if len(conversation_messages[session_id]) > MAX_HISTORY:
        # conversation_messages[session_id].pop(0)
        del conversation_messages[session_id][:-MAX_HISTORY]
