# Optimizer

The above parameter-centric methods usually rely on existing optimizers such as SGD with momentum or Adam [102] to refine the initialization when given some new task. Rather than relying on hand-designed optimizers, optimizer-centric approaches [41], [77], [78], [91] focus on learning the inner optimizer by training a function that takes as input optimization states such as θ and ∇θLtask and produces the optimization step to take at each base learning iteration. The trainable component ω can span simple hyper- parameters such as a fixed step size [75], [76] to more sophisticated pre-conditioning matrices [103]. Ultimately ω can be used to define a full gradient-based optimizer in the sense of defining a complex non-linear transformation of the input gradient and other metadata [41], [78], [89], [91]. The parameters to learn here can potentially be few if the optimizer is applied coordinate-wise across weights [78]. The initialization-centric and optimizer-centric methods can be merged by learning them jointly, namely having the former learn the initial condition for the latter [41], [75]. Optimizer learning methods have both been applied to for few-shot learning [41] and to accelerate and improve many- shot learning [78], [89], [91]. Finally, one can also meta-learn black-box zeroth-order optimizers [104] that only require evaluations of Ltask rather than optimizer states such as gradients. These have been shown [104] to be competitive with conventional Bayesian Optimization [70] alternatives.

### References


<!-- REFERENCE -->


<details>
<summary>[91] Learned Optimizers That Scale And Generalize</summary>
<br>
<!-- (learning_to_learn_by_selfcritique.md) -->

# learning_to_learn_by_selfcritique.md

<!-- REFERENCE -->


</details>



<details>
<summary>[70] Taking The Human Out Of The Loop: A Review Of Bayesian Optimization</summary>
<br>
<!-- (learning_to_optimize.md) -->

# learning_to_optimize.md

<!-- REFERENCE -->


</details>



<details>
<summary>[78] Learning To Learn By Gradient Descent By Gradient Descent</summary>
<br>
<!-- (siamese_neural_networks_for_one_shot_image_recognition.md) -->

# siamese_neural_networks_for_one_shot_image_recognition.md

<!-- REFERENCE -->


</details>



<details>
<summary>[103] Meta-Curvature</summary>
<br>
<!-- (a_closer_look_at_few_shot_classification.md) -->

# a_closer_look_at_few_shot_classification.md

<!-- REFERENCE -->


</details>



<details>
<summary>[41] Optimization As A Model For FewShot Learning</summary>
<br>
<!-- (using_fast_weights_to_deblur_old_memories.md) -->

# using_fast_weights_to_deblur_old_memories.md

<!-- REFERENCE -->


</details>



<details>
<summary>[75] Meta-SGD: Learning To Learn Quickly For Few Shot Learning</summary>
<br>
<!-- (meta_learning_with_memory_augmented_neural_networks.md) -->

# meta_learning_with_memory_augmented_neural_networks.md

<!-- REFERENCE -->


</details>



<details>
<summary>[89] Neural Optimizer Search With Reinforcement Learning</summary>
<br>
<!-- (online_metalearning.md) -->

# online_metalearning.md

<!-- REFERENCE -->


</details>



<details>
<summary>[102] Adam: A Method For Stochastic Optimization</summary>
<br>
<!-- (efficient_off_policy_meta_reinforcement_learning_via_probabilistic_context_variables.md) -->

# efficient_off_policy_meta_reinforcement_learning_via_probabilistic_context_variables.md

<!-- REFERENCE -->


</details>



<details>
<summary>[76] How To Train Your MAML</summary>
<br>
<!-- (meta_networks.md) -->

# meta_networks.md

<!-- REFERENCE -->


</details>



<details>
<summary>[77] Learning To Optimize</summary>
<br>
<!-- (meta_learning_and_universality_deep_representations_and_gradient_descent_can_approximate_any_learning_algorithm.md) -->

# meta_learning_and_universality_deep_representations_and_gradient_descent_can_approximate_any_learning_algorithm.md

<!-- REFERENCE -->


</details>



<details>
<summary>[104] Learning To Learn Without Gradient Descent By Gradient Descent</summary>
<br>
<!-- (tadam_task_dependent_adaptive_metric_for_improved_few_shot_learning.md) -->

# tadam_task_dependent_adaptive_metric_for_improved_few_shot_learning.md

<!-- REFERENCE -->


</details>

