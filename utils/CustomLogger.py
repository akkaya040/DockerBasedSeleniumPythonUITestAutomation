class CustomLogger:
    @staticmethod
    def info(*messages):
        message = " ".join(str(msg) for msg in messages)
        print(f"INFO: {message}")

    @staticmethod
    def error(*messages):
        message = " ".join(str(msg) for msg in messages)
        print(f"ERROR: {message}")

    @staticmethod
    def warning(*messages):
        message = " ".join(str(msg) for msg in messages)
        print(f"WARNING: {message}")

    # Diğer log seviyelerini burada ekleyebilirsiniz
