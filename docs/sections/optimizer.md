# Optimizer

The above parameter-centric methods usually rely on existing optimizers such as SGD with momentum or Adam [102] to refine the initialization when given some new task. Rather than relying on hand-designed optimizers, optimizer-centric approaches [41], [77], [78], [91]
 focus on learning the inner optimizer by training a function that takes as input optimization states such as θ and 
 <img src="https://render.githubusercontent.com/render/math?math=\nabla_{\theta} \mathcal{L}^{t a s k}">
  and produces the optimization step to take at each base learning iteration. The trainable component ω can span simple hyper- parameters such as a fixed step size [75], [76] to more sophisticated pre-conditioning matrices [103]. Ultimately ω can be used to define a full gradient-based optimizer in the sense of defining a complex non-linear transformation of the input gradient and other metadata [41], [78], [89], [91]. The parameters to learn here can potentially be few if the optimizer is applied coordinate-wise across weights [78]. The initialization-centric and optimizer-centric methods can be merged by learning them jointly, namely having the former learn the initial condition for the latter [41], [75]. Optimizer learning methods have both been applied to for few-shot learning [41] and to accelerate and improve many- shot learning [78], [89], [91]. Finally, one can also meta-learn black-box zeroth-order optimizers [104] that only require evaluations of Ltask rather than optimizer states such as gradients. These have been shown [104] to be competitive with conventional Bayesian Optimization [70] alternatives.

### References


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
<summary>[77] Learning To Optimize</summary>
<br>
<!-- (learning_to_optimize.md) -->

# learning_to_optimize.md

<!-- REFERENCE -->


[Learning To Optimize](../papers/learning_to_optimize.md)

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
<summary>[70] Taking The Human Out Of The Loop: A Review Of Bayesian Optimization</summary>
<br>
<!-- (taking_the_human_out_of_the_loop_a_review_of_bayesian_optimization.md) -->

# taking_the_human_out_of_the_loop_a_review_of_bayesian_optimization.md

<!-- REFERENCE -->


[Taking The Human Out Of The Loop: A Review Of Bayesian Optimization](../papers/taking_the_human_out_of_the_loop_a_review_of_bayesian_optimization.md)

</details>



<details>
<summary>[104] Learning To Learn Without Gradient Descent By Gradient Descent</summary>
<br>
<!-- (learning_to_learn_without_gradient_descent_by_gradient_descent.md) -->

# learning_to_learn_without_gradient_descent_by_gradient_descent.md

<!-- REFERENCE -->


[Learning To Learn Without Gradient Descent By Gradient Descent](../papers/learning_to_learn_without_gradient_descent_by_gradient_descent.md)

</details>



<details>
<summary>[102] Adam: A Method For Stochastic Optimization</summary>
<br>
<!-- (adam_a_method_for_stochastic_optimization.md) -->

# adam_a_method_for_stochastic_optimization.md

<!-- REFERENCE -->


[Adam: A Method For Stochastic Optimization](../papers/adam_a_method_for_stochastic_optimization.md)

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
<summary>[103] Meta-Curvature</summary>
<br>
<!-- (meta_curvature.md) -->

# meta_curvature.md

<!-- REFERENCE -->


[Meta-Curvature](../papers/meta_curvature.md)

</details>



<details>
<summary>[76] How To Train Your MAML</summary>
<br>
<!-- (how_to_train_your_maml.md) -->

# how_to_train_your_maml.md

<!-- REFERENCE -->


[How To Train Your MAML](../papers/how_to_train_your_maml.md)

</details>



<details>
<summary>[75] Meta-SGD: Learning To Learn Quickly For Few Shot Learning</summary>
<br>
<!-- (meta_sgd_learning_to_learn_quickly_for_few_shot_learning.md) -->

# meta_sgd_learning_to_learn_quickly_for_few_shot_learning.md

<!-- REFERENCE -->


[Meta-SGD: Learning To Learn Quickly For Few Shot Learning](../papers/meta_sgd_learning_to_learn_quickly_for_few_shot_learning.md)

</details>



<details>
<summary>[78] Learning To Learn By Gradient Descent By Gradient Descent</summary>
<br>
<!-- (learning_to_learn_by_gradient_descent_by_gradient_descent.md) -->

# learning_to_learn_by_gradient_descent_by_gradient_descent.md

<!-- REFERENCE -->


[Learning To Learn By Gradient Descent By Gradient Descent](../papers/learning_to_learn_by_gradient_descent_by_gradient_descent.md)

</details>

