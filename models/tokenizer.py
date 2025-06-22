class WorkflowTokenizer:
    def __init__(self):
        self.vocab = {"[PAD]":0, "[UNK]":1, "[CLS]":2}
        
    def train(self, texts):
        # Build vocabulary from texts
        tokens = set()
        for text in texts:
            tokens.update(text.lower().split())
        self.vocab.update({t:i for i,t in enumerate(tokens, start=3)})
    
    def encode(self, text):
        return [self.vocab.get(t, 1) for t in text.lower().split()]  # 1=UNK