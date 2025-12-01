import torch
import torch.nn as nn

class TinyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(3, 1)

    def forward(self, x):
        return self.fc(x)

model = TinyModel()
model.eval()

dummy_input = torch.randn(1, 3)  # 3 features = acc_x, acc_y, acc_z

torch.onnx.export(
    model,
    dummy_input,
    "tiny_model.onnx",
    input_names=["input"],
    output_names=["output"],
    opset_version=18,   
)

print("Exported tiny_model.onnx")
