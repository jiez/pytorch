from typing import Any, Callable

from .. import _C, autograd


def make_autograd_impl(opdef: Any) -> Callable:
    def autograd_impl(*args):
        name: str = "GeneratedBackwardFor" + opdef._name

        def forward(ctx, *args):
            with _C._AutoDispatchBelowAutograd():
                result = opdef._opoverload(*args)
                if opdef._setup_context_fn:
                    opdef._setup_context_fn(ctx, args, result)
                return result

        def backward(ctx, *grads):
            if opdef._backward_fn:
                return opdef._backward_fn(ctx, *grads)
            raise RuntimeError(
                f"There was no autograd formula registered for {opdef}. "
                f"Please use register_autograd to add one."
            )

        Generated = type(
            name,
            (autograd.Function,),
            {
                "forward": staticmethod(forward),
                "backward": staticmethod(backward),
            },
        )

        result = Generated.apply(*args)  # type: ignore[attr-defined]
        return result

    return autograd_impl
