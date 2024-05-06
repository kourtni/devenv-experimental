
from typing import Dict


class NamedEntityClient:
    def __init__(self, model: any) -> None:
        self.model = model

    @staticmethod
    def map_label(label: str) -> str:
        label_map = {
            "GPE": "Location",
            "LANGUAGE": "Language",
            "LOC": "Location",
            "NORP": "Group",
            "PERSON": "Person",
        }

        return label_map.get(label)

    def get_entities(self, sentence: str) -> Dict:
        doc = self.model(sentence)
        entities = [{"entity": ent.text, "label": self.map_label(ent.label)} for ent in doc.entities]
        return {"entities": entities, "html": ""}