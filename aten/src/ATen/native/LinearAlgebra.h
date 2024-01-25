#pragma once

#define TORCH_ASSERT_ONLY_METHOD_OPERATORS
#include <ATen/core/Tensor.h>

#include <ATen/native/DispatchStub.h>
#include <c10/util/Optional.h>

namespace c10 {
class Scalar;
}

namespace at {
struct TensorIterator;
}

namespace at::native {

using addr_fn = void (*)(TensorIterator &, const Scalar& beta, const Scalar& alpha);
using weight_to_int4pack_fn = void(*)(const Tensor&, const Tensor&);
using int4pack_mm_fn = void(*)(const Tensor&, const Tensor&, const Tensor&, int64_t, const Tensor&);
using int8pack_mm_fn = void(*)(const Tensor&, const Tensor&, const Tensor&, const Tensor&);

DECLARE_DISPATCH(addr_fn, addr_stub);
DECLARE_DISPATCH(weight_to_int4pack_fn, weight_to_int4pack_stub);
DECLARE_DISPATCH(int4pack_mm_fn, int4pack_mm_stub);
DECLARE_DISPATCH(int8pack_mm_fn, int8pack_mm_stub);

} // namespace at::native
