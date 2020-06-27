# computational_cost
Naive implementation of bilevel op- timization as shown in Section 2.1 leads to a quadratic number of learning steps, since each outer step requires multiple inner steps. Moreover, there are a large number of inner steps in the case of many-shot experiments, and these need to be stored in memory. For this reason most meta-learning frameworks are extremely expensive in both time and memory, and often limited to small architectures in the few-shot regime [19]. However there is an increasing focus on methods to tackle this problem. For instance, one can alternate inner and outer updates [44], or train surrogate models [108]. Another family of recent approaches acceler- ate meta-training via closed-form solvers in the inner loop [152], [154]. However, the cost is still quite large, and the significance of the former set heuristics for convergence is unclear. A recent method for computing the gradients for the outer loop using implicit gradients provides a cheaper alternative [153], but only focused on learning the initializa- tion of a network for MAML. While implicit gradients were then shown to work for more general meta-learning tasks such as learning an augmentation network [145], they can only learn parameters involved in the loss function directly and make several assumptions (like zero training gradients at θ∗) often leading to inaccurate ω gradients.
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
<summary>[154] Metalearning With Differentiable Closed-form Solvers</summary>
<br>
<!-- (metalearning_with_differentiable_closed_form_solvers.md) -->

# metalearning_with_differentiable_closed_form_solvers.md

<!-- REFERENCE -->


[Metalearning With Differentiable Closed-form Solvers](../papers/metalearning_with_differentiable_closed_form_solvers.md)

</details>



<details>
<summary>[153] Meta-Learning With Implicit Gradients</summary>
<br>
<!-- (meta_learning_with_implicit_gradients.md) -->

# meta_learning_with_implicit_gradients.md

<!-- REFERENCE -->


[Meta-Learning With Implicit Gradients](../papers/meta_learning_with_implicit_gradients.md)

</details>



<details>
<summary>[108] SMASH: OneShot Model Architecture Search Through Hypernetworks</summary>
<br>
<!-- (smash_oneshot_model_architecture_search_through_hypernetworks.md) -->

# smash_oneshot_model_architecture_search_through_hypernetworks.md

<!-- REFERENCE -->


[SMASH: OneShot Model Architecture Search Through Hypernetworks](../papers/smash_oneshot_model_architecture_search_through_hypernetworks.md)

</details>



<details>
<summary>[152] Meta-Learning With Differentiable Convex Optimization</summary>
<br>
<!-- (meta_learning_with_differentiable_convex_optimization.md) -->

# meta_learning_with_differentiable_convex_optimization.md

<!-- REFERENCE -->


[Meta-Learning With Differentiable Convex Optimization](../papers/meta_learning_with_differentiable_convex_optimization.md)

</details>



<details>
<summary>[145] Optimizing Millions Of Hyperparameters By Implicit Differentiation</summary>
<br>
<!-- (optimizing_millions_of_hyperparameters_by_implicit_differentiation.md) -->

# optimizing_millions_of_hyperparameters_by_implicit_differentiation.md

<!-- REFERENCE -->


[Optimizing Millions Of Hyperparameters By Implicit Differentiation](../papers/optimizing_millions_of_hyperparameters_by_implicit_differentiation.md)

</details>



<details>
<summary>[44] Feature-Critic Networks For Heterogeneous Domain Generalization</summary>
<br>
<!-- (feature_critic_networks_for_heterogeneous_domain_generalization.md) -->

# feature_critic_networks_for_heterogeneous_domain_generalization.md

<!-- REFERENCE -->


[Feature-Critic Networks For Heterogeneous Domain Generalization](../papers/feature_critic_networks_for_heterogeneous_domain_generalization.md)

</details>

