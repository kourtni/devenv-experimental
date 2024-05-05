import unittest
from ner_client import NamedEntityClient
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