# gradient

A large family of methods use gradient descent on the meta parameters ω [19], [41], [44], [67]. This requires computing derivatives 
<img src="https://render.githubusercontent.com/render/math?math=d \mathcal{L}^{m e t a} / d \omega">
 of the outer objective, which are typically connected via the chain rule to the model parameter θ, 
<img src="https://render.githubusercontent.com/render/math?math=d \mathcal{L}^{m e t a} / d \omega=\left(d \mathcal{L}^{m e t a} / d \theta\right)(d \theta / d \omega)">
  These methods are potentially the most efficient as they exploit analytical gradients of ω. However key challenges include: 
  (i) Efficiently differentiating through long computation graphs where the inner optimization uses many steps, for example through careful design of 
  auto-differentiation algorithms [25], [178] and implicit differentiation [145], [153], [179], and dealing tractably with the required second-order gradients [180].
   (ii) Reducing the inevitable gradient degradation problems whose severity increases with the number of inner loop optimization steps.
    (iii) Calculating gradients when the base learner, ω, or <img src="https://render.githubusercontent.com/render/math?math=\mathcal{L}^{\text {task}}"> include discrete or other non- differentiable operations.
<!-- REFERENCE -->


<details>
<summary>[41] Optimization As A Model For FewShot Learning</summary>
<br>
<!-- (optimization_as_a_model_for_fewshot_learning.md) -->

# optimization_as_a_model_for_fewshot_learning.md

<!-- REFERENCE -->


[Optimization As A Model For FewShot Learning](../papers/optimization_as_a_model_for_fewshot_learning.md)

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
<summary>[179] Fixing Implicit Derivatives: Trust-Region Based Learning Of Continuous Energy Functions</summary>
<br>
<!-- (fixing_implicit_derivatives_trust_region_based_learning_of_continuous_energy_functions.md) -->

# fixing_implicit_derivatives_trust_region_based_learning_of_continuous_energy_functions.md

<!-- REFERENCE -->


[Fixing Implicit Derivatives: Trust-Region Based Learning Of Continuous Energy Functions](../papers/fixing_implicit_derivatives_trust_region_based_learning_of_continuous_energy_functions.md)

</details>



<details>
<summary>[44] Feature-Critic Networks For Heterogeneous Domain Generalization</summary>
<br>
<!-- (feature_critic_networks_for_heterogeneous_domain_generalization.md) -->

# feature_critic_networks_for_heterogeneous_domain_generalization.md

<!-- REFERENCE -->


[Feature-Critic Networks For Heterogeneous Domain Generalization](../papers/feature_critic_networks_for_heterogeneous_domain_generalization.md)

</details>



<details>
<summary>[67] Forward And Reverse Gradient-Based Hyperparameter Optimization</summary>
<br>
<!-- (forward_and_reverse_gradient_based_hyperparameter_optimization.md) -->

# forward_and_reverse_gradient_based_hyperparameter_optimization.md

<!-- REFERENCE -->


[Forward And Reverse Gradient-Based Hyperparameter Optimization](../papers/forward_and_reverse_gradient_based_hyperparameter_optimization.md)

</details>



<details>
<summary>[19] Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks</summary>
<br>
<!-- (model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md) -->

# model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md

<!-- REFERENCE -->


[Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks](../papers/model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md)

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
<summary>[178] Gradient-based Hyperparameter Optimization Through Reversible Learning</summary>
<br>
<!-- (gradient_based_hyperparameter_optimization_through_reversible_learning.md) -->

# gradient_based_hyperparameter_optimization_through_reversible_learning.md

<!-- REFERENCE -->


[Gradient-based Hyperparameter Optimization Through Reversible Learning](../papers/gradient_based_hyperparameter_optimization_through_reversible_learning.md)

</details>



<details>
<summary>[25] Bilevel Programming For Hyperparameter Optimization And Meta-learning</summary>
<br>
<!-- (bilevel_programming_for_hyperparameter_optimization_and_meta_learning.md) -->

# bilevel_programming_for_hyperparameter_optimization_and_meta_learning.md

<!-- REFERENCE -->


[Bilevel Programming For Hyperparameter Optimization And Meta-learning](../papers/bilevel_programming_for_hyperparameter_optimization_and_meta_learning.md)

</details>



<details>
<summary>[180] On First-Order MetaLearning Algorithms</summary>
<br>
<!-- (on_first_order_metalearning_algorithms.md) -->

# on_first_order_metalearning_algorithms.md

<!-- REFERENCE -->


[On First-Order MetaLearning Algorithms](../papers/on_first_order_metalearning_algorithms.md)

</details>

