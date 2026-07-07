class MemoryService:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.messages = []
        return cls._instance

    def add_message(self, role: str, content: str):
        self.messages.append({
            "role": role,
            "content": content
        })

    def get_messages(self):
        return self.messages

    def clear(self):
        self.messages.clear()