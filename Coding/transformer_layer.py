import numpy as np
import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(
        self,
        emb_dim: int,
        num_heads: int,
        dropout: float,
        bias: bool,
    ):
        super().__init__()


        self.emb_dim = emb_dim
        self.num_heads = num_heads
        self.dropout = dropout
        self.bias = bias

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 
         
        return x

