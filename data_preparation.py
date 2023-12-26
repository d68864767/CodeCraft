```python
import json
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """
    Load data from a JSON file.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def prepare_dataset(data, test_size=0.2):
    """
    Prepare the dataset by splitting it into training and test sets.
    """
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=42)
    return train_data, test_data

def save_data(data, file_path):
    """
    Save data to a JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file)

def main():
    # Load the data
    data = load_data('path_to_your_data.json')

    # Prepare the dataset
    train_data, test_data = prepare_dataset(data)

    # Save the training data
    save_data(train_data, 'train_data.json')

    # Save the test data
    save_data(test_data, 'test_data.json')

if __name__ == "__main__":
    main()
```
