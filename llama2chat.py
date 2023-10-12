from transformers import AutoTokenizer
import torch
from transformers import pipeline


model = "meta-llama/Llama-2-7b-chat-hf"
token = "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"  # Replace with your actual Hugging Face token
tokenizer = AutoTokenizer.from_pretrained(model, use_auth_token=token)

llama_pipeline = pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float32,
    device_map="auto",
)

def get_llama_response(prompt: str) -> None:
    """
    Generate a response from the Llama model.

    Parameters:
        prompt (str): The user's input/question for the model.

    Returns:
        None: Prints the model's response.
    """

    sequences = llama_pipeline(
        prompt,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_length=256,
    )
    print("Chatbot:", sequences[0]['generated_text'])

prompt = 'Give me innovative ideas for a chatbot using question-answer on tabular data. I need to visualize output answer and anymore enhance to results output'
get_llama_response(prompt)    