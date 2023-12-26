# Fine-tuning Models with OpenAI

This project provides a comprehensive guide to fine-tuning models using OpenAI. Fine-tuning enhances model performance by training on more examples than can fit in a prompt. It provides higher quality results, token savings, and lower latency requests. Fine-tuning is preferable when few-shot learning is insufficient.

## Steps Involved

1. **Prepare and Upload Training Data**: Create a diverse dataset similar to your intended use case. Refer to `data_preparation.py` for more details.
2. **Train a New Fine-tuned Model**: Use the dataset to train the model. Check `model_training.py` for the implementation.
3. **Evaluate Results**: Assess performance and iterate if necessary. The `model_evaluation.py` file contains the necessary code.
4. **Use Your Fine-tuned Model**: Deploy the model in your application. The deployment process is outlined in `model_deployment.py`.

## Applicable Models

- GPT-4
- GPT-3.5-turbo-1106 (Recommended)
- GPT-3.5-turbo-0613
- Babbage-002
- Davinci-002

Fine-tuning already fine-tuned models is also possible.

## When to Use Fine-tuning

Consider fine-tuning when prompt engineering is insufficient. It is useful for specific applications, such as setting style, tone, or handling complex prompts. Fine-tuning is effective for reducing costs and latency.

## Preparing Your Dataset

Create a set of demonstration conversations. The dataset should mimic the format of the Chat Completions API or prompt-completion pairs. Include examples targeting cases where the prompted model underperforms.

## Crafting Prompts

Include the best set of instructions and prompts in every training example. Shortening instructions in each example is possible but could impact learning.

## Example Count Recommendations

A minimum of 10 examples is required. Typically, 50 to 100 examples provide clear improvements. Evaluate whether the initial dataset leads to improvement before expanding.

## Train and Test Splits

Split the dataset into training and test portions for better evaluation.

## Token Limits

Depends on the model selected. Each training example must fit within the model's maximum context length.

## Estimate Costs

Costs are based on input and output tokens. Refer to the OpenAI pricing page for detailed cost information.

## Fine-tuning Data Format Validation

Before fine-tuning, validate the dataset using OpenAI's provided Python script.

## Creating a Fine-tuned Model

Fine-tuning jobs can be created via the OpenAI SDK or fine-tuning UI. Requires uploading the training file and specifying the model.

## Using a Fine-tuned Model

Use the fine-tuned model in the Chat Completions or legacy Completions API. The model is immediately available for inference after training completion.

## Analyzing Your Fine-tuned Model

OpenAI provides training metrics for evaluating the model's performance. Comparing samples from the base and fine-tuned models is recommended for quality assessment.

## Iterating on Data Quality and Quantity

Adjust the training dataset by targeting remaining issues and ensuring data quality. Scaling up the number of training examples can improve performance on edge cases.

## Iterating on Hyperparameters

Hyperparameters like epochs, learning rate multiplier, and batch size can be adjusted for optimization. Refer to `hyperparameters_tuning.py` for more details.

## Fine-tuning Examples

Examples include style and tone adjustment, structured output, function calling, and legacy model migration.

## FAQs

Addresses common questions about fine-tuning versus embeddings, GPT-4 and GPT-3.5-Turbo-16k fine-tuning, cost estimation, and more. Check `faqs.md` for more details.

For detailed information and specific instructions on each step, refer to OpenAI's fine-tuning documentation.
