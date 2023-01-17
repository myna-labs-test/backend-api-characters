from .base import BaseDialogDriver
from transformers import AutoTokenizer, TFGPT2LMHeadModel


class SberDriver(BaseDialogDriver):
    model: TFGPT2LMHeadModel = None
    tokenizer: AutoTokenizer = None

    @classmethod
    def with_default_settings(cls):
        if not cls.tokenizer:
            cls.tokenizer = AutoTokenizer.from_pretrained(cls.model_id)
        if not cls.model:
            cls.model = TFGPT2LMHeadModel.from_pretrained(cls.model_id, from_pt=True)
        return cls(model_id=cls.model_id)

    @classmethod
    async def generate_text(cls, input_text: str) -> str:
        tokens = cls.tokenizer.encode(input_text, return_tensors="tf")
        result = cls.model.generate(
            tokens,
            do_sample=True,
            max_length=100,
            top_k=5,
            temperature=1.2
        )
        decoded = cls.tokenizer.decode(result[0], skip_special_tokens=True)
        return decoded