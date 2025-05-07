from datetime import datetime

class CommonFormat:
    @staticmethod
    def convert_to_datetime(text: str, format: str):
        return datetime.strptime(text, format)
