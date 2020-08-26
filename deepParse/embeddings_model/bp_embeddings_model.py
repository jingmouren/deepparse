from bpemb import BPEmb
from numpy.core.multiarray import ndarray

from .embeddings_model import EmbeddingsModel


class BPEmbEmbeddingsModel(EmbeddingsModel):
    """
    BPEmb embeddings model from `BPEmb: Tokenization-free Pre-trained Subword Embeddings in 275 Languages
    <https://www.aclweb.org/anthology/L18-1473/>`_. The arguments are the same as the
    `BPEmb class <https://github.com/bheinzerling/bpemb/blob/master/bpemb/bpemb.py>`_
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.model = BPEmb(**kwargs)

    def __call__(self, word: str) -> ndarray:
        """
        Callable method to get a word vector.

        Args:
            word (str): Word to get vector.

        Return:
            The BP embedding for a word.
        """
        return self.model.embed(word)
