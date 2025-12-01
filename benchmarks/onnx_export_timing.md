# ⏱️ ONNX Export Timing (Week 1 – Day 4)

This benchmark captures how long it took to export our `TinyModel` from PyTorch to ONNX on the **Raspberry Pi 5 (8 GB)**.

---

## 🧪 Test Environment

**Device:** Raspberry Pi 5  
**OS:** Raspberry Pi OS 64-bit  
**Python:** 3.11  
**PyTorch:** Installed via pip  
**Model:** TinyModel (fully-connected + ReLU)  
**Input shape:** [1, 10]  
**ONNX opset:** Auto-upgraded to 18  
**Venv:** `edge_bootcamp`

---

## ⏱️ Timing Script Used

```python
import time
import torch
from dummy_to_onnx import TinyModel

model = TinyModel()
dummy_input = torch.randn(1, 10)

t0 = time.time()

torch.onnx.export(
    model,
    dummy_input,
    "tiny_model.onnx",
    input_names=["input"],
    output_names=["output"],
    opset_version=17,  # auto-promoted to 18 by PyTorch
)

elapsed = time.time() - t0
print(f"ONNX export time: {elapsed:.4f} seconds")