from typing import Any
from typing import List


class NerModelTestDouble:
    '''Test double for spaCy NLP model.'''

    def __init__(self, model: Any) -> None:
        self.model = model

    def returns_doc_entities(self, entities: List[Any]):
        self.entities = entities

    def __call__(self, sent: Any) -> Any:
        return DocTestDouble(sent, self.entities)


class DocTestDouble:
    '''Test double for spaCy Doc.'''

    def __init__(self, sent, entities):
        self.entities = [SpanTestDouble(ent["text"], ent["label_"]) for ent in entities]


class SpanTestDouble:
    '''Test double for spaCy Span'''

    def __init__(self, text, label) -> None:
        self.text = text
        self.label = label