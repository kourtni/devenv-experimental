from typing import Any, Dict, List


class NerModelTestDouble:
    '''Test double for spaCy NLP model.'''

    def __init__(self, model: Any) -> None:
        self.model = model

    def returns_doc_entities(self, entities: List[Any]):
        self.entities = entities

    def __call__(self, sentence: str) -> Any:
        return DocTestDouble(sentence, self.entities)


class DocTestDouble:
    '''Test double for spaCy Doc.'''

    def __init__(self, sentence: str, entities: Dict):
        self.entities = [
            SpanTestDouble(ent['text'], ent['label_']) for ent in entities
        ]


class SpanTestDouble:
    '''Test double for spaCy Span'''

    def __init__(self, text: str, label: str) -> None:
        self.text = text
        self.label = label
