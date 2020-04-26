import pytest
from spacy.vocab import Vocab
from spacy.tokens import Doc
from thinc.api import Model
from ..pipeline import Transformer, AnnotationSetter
from .util import DummyTransformer
from ..types import TransformerOutput


@pytest.fixture
def vocab():
    return Vocab()

@pytest.fixture
def docs(vocab):
    return [Doc(vocab, words=["hello", "world"]), Doc(vocab, words=["this", "is", "another"])]


@pytest.fixture
def component(vocab):
    return Transformer(Vocab(), DummyTransformer())

def test_init(component):
    assert isinstance(component.vocab, Vocab)
    assert isinstance(component.model, Model)
    assert isinstance(component.annotation_setter, AnnotationSetter)
    assert component.listeners == []
    assert component.cfg == {}


def test_predict(component, docs):
    trf_data = component.predict(docs)
    assert isinstance(trf_data, TransformerOutput)
