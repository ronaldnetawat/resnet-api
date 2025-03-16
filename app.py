from fastapi import FastAPI, UploadFile, File
import torch 
from torchvision import models, transforms
from PIL import Image
import io

app = FastAPI()

# loading the pretrained model
model = models.resnet18(pretrained=True)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(image)

    return {"prediction": output.argmax().item()}