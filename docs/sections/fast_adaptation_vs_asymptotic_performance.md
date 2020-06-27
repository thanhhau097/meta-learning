# fast_adaptation_vs_asymptotic_performance

When val- idation loss is computed at the end of the inner learning episode, meta-training encourages better final performance of the base task. When it is computed as the sum of the validation loss after each inner optimization step, then meta- training also encourages faster learning in the base task [76], [89], [91]. Most RL applications also use this latter setting
<!-- REFERENCE -->


<details>
<summary>[89] Neural Optimizer Search With Reinforcement Learning</summary>
<br>
<!-- (neural_optimizer_search_with_reinforcement_learning.md) -->

# neural_optimizer_search_with_reinforcement_learning.md

<!-- REFERENCE -->


[Neural Optimizer Search With Reinforcement Learning](../papers/neural_optimizer_search_with_reinforcement_learning.md)

</details>



<details>
<summary>[76] How To Train Your MAML</summary>
<br>
<!-- (how_to_train_your_maml.md) -->

# how_to_train_your_maml.md
## What?
- Research the practical training techniques help training MAML more effective
## Why?
Disadvantage of original MAML:
- Training Instability: lack of any skip connections
- Second Order Derivative cost
- Absence of Batch Normalization Statistic Accumulation
- Shared (across step) Batch Normalization Bias
- Shared Inner Loop (across step and across parameter) Learning Rate
- Fixed Outer Loop Learning Rate
## How?
Handle these above problem:
- Gradient Instability → Multi-Step Loss Optimization (MSL): propose minimizing the target set loss computed by the base-network after every step towards a support set task,
the loss minimized is a weighted sum of the target set losses after every support set loss update, employ an annealed weighting for the per step losses.

<img src="https://render.githubusercontent.com/render/math?math=\theta=\theta-\beta \nabla_{\theta} \sum_{b=1}^{B} \sum_{i=0}^{N} v_{i} \mathcal{L}_{T_{b}}\left(f_{\theta_{i}^{b}}\right)">

- Second Order Derivative Cost → Derivative-Order Annealing (DA): propose to anneal the derivative-order as training progresses. More specifically, we propose to use first-order gradients for the first 50 epochs of the training phase, and to then switch to second-order gradients for the remainder of the training phase
Using first-order before starting to use second-order derivatives can be used as a strong pretraining method that learns parameters less likely to produce gradient explosion/diminishment issues.
- Absence of Batch Normalization Statistic Accumulation → Per-Step Batch Normalization Running Statistics (BNRS): instantiate N (where N is the total number of inner-loop update steps) sets of running mean and running standard deviation for each batch normalization layer in the network and update the running statistics respectively with the steps being taken during the optimization. The per-step batch normalization methodology should speed up optimization of MAML whilst potentially improving generalization performance

- Shared (across step) Batch Normalization Bias → Per-Step Batch Normalization Weights and Biases (BNWB): batch normalization will learn biases specific to the feature distributions seen at each set, which should increase convergence speed, stability and generalization performance.

- Shared Inner Loop Learning Rate (across step and across parameter) → Learning Per-Layer Per-Step Learning Rates and Gradient Directions (LSLR): we propose, learning a learning rate and direction for each layer in the network as well as learning different learning rates for each adaptation of the base-network as it takes steps

- Fixed Outer Loop Learning Rate → Cosine Annealing of Meta-Optimizer Learning Rate (CA): we propose applying the cosine annealing scheduling on the meta-model’s optimizer (i.e. the meta-optimizer)

## Results? (What did they find?)
- State of the art results, each of above techniques do improve the results
- Use validation set to get better results: ensemble of the top 3 performing per-epoch-models on the validation set were applied on the test set
## Ideas to improve?
Apply these technique when train modifications of MAML

<!-- REFERENCE -->


[How To Train Your MAML](../papers/how_to_train_your_maml.md)

</details>



<details>
<summary>[91] Learned Optimizers That Scale And Generalize</summary>
<br>
<!-- (learned_optimizers_that_scale_and_generalize.md) -->

# learned_optimizers_that_scale_and_generalize.md

<!-- REFERENCE -->


[Learned Optimizers That Scale And Generalize](../papers/learned_optimizers_that_scale_and_generalize.md)

</details>

