# many_vs_few_shot_episode_design

The final component is to define the goal of the meta-
learning method through choice of meta-objective Lmeta, and associated data flow between inner loop episodes and outer optimizations. Most methods in the literature rely on some form of performance metric computed on a validation set, after updating the task model with ω, and using this metric as the meta-objective. This is in line with classic validation set-based approaches to hyperparameter tuning and architecture selection. However, within this framework, there are several design options:
Many vs Few-Shot Episode Design According to
whether the goal is improving few- or many-shot perfor- mance, inner loop learning episodes may be defined with many [67], [89], [91] or few- [19], [41] examples per-task.
<!-- REFERENCE -->


<details>
<summary>[19] Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks</summary>
<br>
<!-- (model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md) -->

# model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md
## What?
- Model-agnostic meta-learning algorithm that can adapt to every gradient-based models, including classisication, 
regression, reinforcement leanring
## Why?
- To adapt to any gradient-based model
- Solve new task quickly with a few gradient steps by learning initial weights

## How?
The algorithm is shown in the images below:
![alt text](../images/maml.png)

![alt text](../images/maml_few_shot_supervised.png)

![alt text](../images/maml_rl.png)

- Loss function can be any frequenly used loss function for that task.
- MAML can maximize the sensitivity of the loss functions of new tasks with respect to the parameters.
## Results? (What did they find?)
- MAML can be used with any gradient-based models.
- MAML is sensitive to change in the task, such that small changes in the parameters will produce large improvements on 
the loss function.
- Perform better than transfer learning in regression tasks, because they can learn the abstract over tasks.
- State-of-the art in regression, classification, reinforcement learning 
- Without overfitting 
## Ideas to improve?
- Handle the computation problem. The paper currently use approximate method.

## Application ideas
- use meta-learning to find the initial weights for any deep learning model.
<!-- REFERENCE -->


[Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks](../papers/model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md)

</details>



<details>
<summary>[89] Neural Optimizer Search With Reinforcement Learning</summary>
<br>
<!-- (neural_optimizer_search_with_reinforcement_learning.md) -->

# neural_optimizer_search_with_reinforcement_learning.md

<!-- REFERENCE -->


[Neural Optimizer Search With Reinforcement Learning](../papers/neural_optimizer_search_with_reinforcement_learning.md)

</details>



<details>
<summary>[91] Learned Optimizers That Scale And Generalize</summary>
<br>
<!-- (learned_optimizers_that_scale_and_generalize.md) -->

# learned_optimizers_that_scale_and_generalize.md

<!-- REFERENCE -->


[Learned Optimizers That Scale And Generalize](../papers/learned_optimizers_that_scale_and_generalize.md)

</details>



<details>
<summary>[41] Optimization As A Model For FewShot Learning</summary>
<br>
<!-- (optimization_as_a_model_for_fewshot_learning.md) -->

# optimization_as_a_model_for_fewshot_learning.md
## What?
- LSTM based meta-learner model to learn the exact optimization algorithm used to train another learner neural network classifier in the few-shot regime.
## Why?
- Handle the few-shot learning problem, the model can transfer 
## How?
This model based on the LSTM, the model modified the update rule of gradient from: 
<img src="https://render.githubusercontent.com/render/math?math=\theta_{t}=\theta_{t-1}-\alpha_{t} \nabla_{\theta_{t-1}} \mathcal{L}_{t}">

to <img src="https://render.githubusercontent.com/render/math?math=c_{t}=f_{t} \odot c_{t-1}+i_{t} \odot \tilde{c}_{t}">

if <img src="https://render.githubusercontent.com/render/math?math=f_{t}=1, c_{t-1}=\theta_{t-1}, i_{t}=\alpha_{t}"> and 
<img src="https://render.githubusercontent.com/render/math?math=\tilde{c}_{t}=-\nabla_{\theta_{t-1}} \mathcal{L}_{t}">

But we can learn the <img src="https://render.githubusercontent.com/render/math?math=i_t"> and <img src="https://render.githubusercontent.com/render/math?math=f_t">

<img src="https://render.githubusercontent.com/render/math?math=i_{t}=\sigma\left(\mathbf{W}_{I} \cdot\left[\nabla_{\theta_{t-1}} \mathcal{L}_{t}, \mathcal{L}_{t}, \theta_{t-1}, i_{t-1}\right]+\mathbf{b}_{I}\right)">

and

<img src="https://render.githubusercontent.com/render/math?math=f_{t}=\sigma\left(\mathbf{W}_{F} \cdot\left[\nabla_{\theta_{t-1}} \mathcal{L}_{t}, \mathcal{L}_{t}, \theta_{t-1}, f_{t-1}\right]+\mathbf{b}_{F}\right)">

and also we can learn the initial weights of learner, allows the optimization process more rapid.


![alt text](../images/lstm_learner.png)
![alt text](../images/lstm_learner_algorithm.png)

## Results? (What did they find?)
- Apply the LSTM to learn the learning updates of the parameters of classifier.
- Can learn the good initialization parameters and update rules.
## Ideas to improve?
- The paper shows that by learning and modify the update rules, we could get better results. Could we use this idea?

<!-- REFERENCE -->


[Optimization As A Model For FewShot Learning](../papers/optimization_as_a_model_for_fewshot_learning.md)

</details>



<details>
<summary>[67] Forward And Reverse Gradient-Based Hyperparameter Optimization</summary>
<br>
<!-- (forward_and_reverse_gradient_based_hyperparameter_optimization.md) -->

# forward_and_reverse_gradient_based_hyperparameter_optimization.md

<!-- REFERENCE -->


[Forward And Reverse Gradient-Based Hyperparameter Optimization](../papers/forward_and_reverse_gradient_based_hyperparameter_optimization.md)

</details>

