from fastapi import FastAPI
from src.model.transformer import WorkflowTransformer
from src.model.tokenizer import WorkflowTokenizer

app = FastAPI()
model = WorkflowTransformer().eval()  # Load pretrained in production
tokenizer = WorkflowTokenizer()

@app.post("/generate")
async def generate_workflow(text: str):
    tokens = tokenizer.encode(text)
    output = model(torch.tensor([tokens]))
    return {"workflow": decode_to_workflow(output)}  # Implement decoder