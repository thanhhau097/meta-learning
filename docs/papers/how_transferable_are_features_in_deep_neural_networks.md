# how_transferable_are_features_in_deep_neural_networks.md

## What?
- Research about the transferability of layers in neural networks
- Find out the general and specific property of those layers.
- Transfer between similar and disimilar tasks
## Why?
- To find out the ways to transfer features more effectively
## How?
- Split to 2 tasks/datasets A and B randomly (ImageNet dataset)
- Evaluate the transferability of: (k is number of first layers transfered, + is retrain those layers)
    - Seffer network: BkB, BkB+
    - Transfer networks: AkB, AkB+
- Also evaluate on similar and disimilar tasks (compare based on the similar of images in dataset: human-made vs. natural)
## Results? (What did they find?)
- AkB+ is the most effective method.
- Transfer on similar task is more effective than disimilar ones
- Transfer from any pretrained features is better than transfer randomly
## Ideas to improve?
- This can be useful for meta-learning, when we learn many tasks, we can get the knowledge of other task and do 
few-shot learning
<!-- REFERENCE -->
