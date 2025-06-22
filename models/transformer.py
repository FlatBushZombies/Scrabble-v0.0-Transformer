import torch
import torch.nn as nn

class WorkflowTransformer(nn.Module):
    def __init__(self, vocab_size=10000, d_model=256):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.transformer = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model, nhead=4),
            num_layers=3
        )
        self.decoder = nn.Linear(d_model, vocab_size)  # Simplified output

    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer(x)
        return self.decoder(x.mean(dim=1))  # Pooling