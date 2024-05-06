import unittest
from ner_client import NamedEntityClient
from parameterized import parameterized
from test_doubles import NerModelTestDouble

class TestNerClient(unittest.TestCase):

    # Expected entities dict structure.
    # { entities:   [{...}],
    #   html:       "<span>..."}

    def test_get_entities_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble("eng")
        model.returns_doc_entities([])
        ner = NamedEntityClient(model)
        entities = ner.get_entities("")
        self.assertIsInstance(entities, dict)

    def test_get_entities_returns_dict_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble("eng")
        model.returns_doc_entities([])
        ner = NamedEntityClient(model)
        entities = ner.get_entities("Chicago is a city in Illinois.")
        self.assertIsInstance(entities, dict)

    @parameterized.expand([("person_to_person", "Laurent Fressinet", "PERSON", "Person"),
                           ("norp_to_group", "Russian", "NORP", "Group"),
                           ("loc_to_location", "the ocean", "LOC", "Location"),
                           ("language_to_language", "ASL", "LANGUAGE", "Language"),
                           ("gpe_to_location", "Australia", "GPE", "Location")])
    def test_get_ents_given_spacy_label_is_returned_serializes_to_custom_label(
        self, _, text, label_, label):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": text, "label_":label_}]
        model.returns_doc_entities(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_entities("...")
        expected_result = {"entities": [{"entity": text, "label": label}],
                           "html": ""}
        self.assertListEqual(result["entities"], expected_result["entities"])
    
    def test_get_ents_given_multiple_spacy_entities_serializes_all(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Russian", "label_":"NORP"},
                    {"text": "the ocean", "label_":"LOC"},
                    {"text": "ASL", "label_":"LANGUAGE"}]
        model.returns_doc_entities(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_entities("...")
        expected_result = {"entities": [{"entity": "Russian", "label": "Group"},
                                        {"entity": "the ocean", "label": "Location"},
                                        {"entity": "ASL", "label": "Language"}],
                           "html": ""}
        self.assertListEqual(result["entities"], expected_result["entities"])