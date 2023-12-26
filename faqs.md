# Frequently Asked Questions (FAQs)

## What is fine-tuning?

Fine-tuning is a process that enhances model performance by training on more examples than can fit in a prompt. It provides higher quality results, token savings, and lower latency requests. Fine-tuning is preferable when few-shot learning is insufficient.

## When should I consider fine-tuning?

Consider fine-tuning when prompt engineering is insufficient. It is useful for specific applications, such as setting style, tone, or handling complex prompts. Fine-tuning is also effective for reducing costs and latency.

## What models can I fine-tune?

You can fine-tune the following models:

- GPT-4
- GPT-3.5-turbo-1106 (Recommended)
- GPT-3.5-turbo-0613
- Babbage-002
- Davinci-002

Fine-tuning already fine-tuned models is also possible.

## How do I prepare my dataset for fine-tuning?

Create a set of demonstration conversations. The dataset should mimic the format of the Chat Completions API or prompt-completion pairs. Include examples targeting cases where the prompted model underperforms. Refer to `data_preparation.py` for more details.

## How many examples do I need for fine-tuning?

A minimum of 10 examples is required. Typically, 50 to 100 examples provide clear improvements. Evaluate whether the initial dataset leads to improvement before expanding.

## How do I estimate the costs of fine-tuning?

Costs are based on input and output tokens. Refer to the OpenAI pricing page for detailed cost information.

## How do I validate my fine-tuning data format?

Before fine-tuning, validate the dataset using OpenAI's provided Python script.

## How do I create a fine-tuned model?

Fine-tuning jobs can be created via the OpenAI SDK or fine-tuning UI. This requires uploading the training file and specifying the model. Check `model_training.py` for the implementation.

## How do I use my fine-tuned model?

Use the fine-tuned model in the Chat Completions or legacy Completions API. The model is immediately available for inference after training completion. The deployment process is outlined in `model_deployment.py`.

## How do I evaluate my fine-tuned model?

OpenAI provides training metrics for evaluating the model's performance. Comparing samples from the base and fine-tuned models is recommended for quality assessment. The `model_evaluation.py` file contains the necessary code.

## How do I iterate on data quality and quantity?

Adjust the training dataset by targeting remaining issues and ensuring data quality. Scaling up the number of training examples can improve performance on edge cases.

## How do I iterate on hyperparameters?

Hyperparameters like epochs, learning rate multiplier, and batch size can be adjusted for optimization. Refer to `hyperparameters_tuning.py` for more details.

## What are some examples of fine-tuning?

Examples include style and tone adjustment, structured output, function calling, and legacy model migration.

## Can I fine-tune GPT-4 and GPT-3.5-Turbo-16k?

Yes, GPT-4 is available for eligible users via an experimental access program. GPT-3.5-Turbo-16k fine-tuning is also possible.

## How do I estimate the cost of fine-tuning?

Cost estimation is based on input and output tokens. Refer to the OpenAI pricing page for detailed cost information.

For detailed information and specific instructions on each step, refer to OpenAI's fine-tuning documentation.
