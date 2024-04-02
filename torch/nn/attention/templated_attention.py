from typing import Callable

import torch
from torch._higher_order_ops.templated_attention import sdpa


_score_mod_signature = Callable[
    [torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor], torch.Tensor
]


def templated_attention(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    score_mod: _score_mod_signature,
) -> torch.Tensor:
    """This function implements scaled dot product attention with an arbitrary attention score modification function.

    .. warning::
        `torch.nn.attention.templated_attention` is a prototype feature in PyTorch. It doesn't support training currently.
        Please look forward to a more stable implementation in a future version of PyTorch.
        Read more about feature classification at: https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype

    Args:
        query (Tensor): Query tensor; shape :math:`(B, H, L, E)`.
        key (Tensor): Key tensor; shape :math:`(B, H, S, E)`.
        value (Tensor): Value tensor; shape :math:`(B, H, S, Ev)`.
        score_mod (Callable): Function to modify attention scores; signature :math:`(score, b, h, m, n, *other_buffers) -> score`.
    Returns:
        output (Tensor): Attention output; shape :math:`(B, H, L, Ev)`.
    """
    return sdpa(query, key, value, score_mod)
