```python
import openai
import json

def load_data(file_path):
    """
    Load data from a JSON file.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def create_finetuned_model(train_data, model_name):
    """
    Create a fine-tuned model using the OpenAI API.
    """
    # Initialize the OpenAI API
    openai.api_key = 'your_openai_api_key'

    # Create a new fine-tuned model
    model = openai.FineTuning.create(
        model=model_name,
        dataset=train_data,
        learning_rate_multiplier=0.1,
        epochs=10,
        batch_size=4
    )

    return model

def save_model(model, file_path):
    """
    Save the fine-tuned model to a file.
    """
    with open(file_path, 'w') as file:
        file.write(model.id)

def main():
    # Load the training data
    train_data = load_data('train_data.json')

    # Create a new fine-tuned model
    model = create_finetuned_model(train_data, 'gpt-3.5-turbo')

    # Save the model
    save_model(model, 'model.txt')

if __name__ == "__main__":
    main()
```
