import torch
from model.transformer import WorkflowTransformer

def main():
    model = WorkflowTransformer.load_from_checkpoint("model.pt")
    text = input("Enter workflow instructions: ")
    print(model.generate(text))

if __name__ == "__main__":
    main()