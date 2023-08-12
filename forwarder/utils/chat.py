from typing import List, List, Union, TypedDict, Optional, Set

from forwarder import CONFIG


class ChatConfig(TypedDict):
    chat_id: int
    thread_id: Optional[int]


def parse_topic(chat_id: Union[str, int]) -> ChatConfig:
    if isinstance(chat_id, str):
        raw = chat_id.split("#")
        if len(raw) == 2:
            return {"chat_id": int(raw[0]), "thread_id": int(raw[1])}
        return {"chat_id": int(raw[0]), "thread_id": None}

    return {"chat_id": chat_id, "thread_id": None}


def get_source() -> List[ChatConfig]:
    src: List[ChatConfig] = []

    for chat in CONFIG:
        src.extend([parse_topic(item) for item in chat["source"]])
    return src

def get_destenation(source: int) -> List[ChatConfig]:
    dest: List[ChatConfig] = []

    for chat in CONFIG:
        for src in chat["source"]:
            parsed = parse_topic(src)
            if parsed["chat_id"] == source:
                dest.extend([parse_topic(item) for item in chat["destination"]])

    return dest
