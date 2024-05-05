
class NamedEntityClient:
    def __init__(self, model: any) -> None:
        self.model = model

    def get_entities(self, sentence: str):
        doc = self.model(sentence)
        return {}