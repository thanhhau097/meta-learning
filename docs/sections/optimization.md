# optimization
Previous [73], [74] categorizations of meta-learning meth- ods have tended to produce a three-way taxonomy across optimization-based methods, model-based (or black box) methods, and metric-based (or non-parametric) methods. Optimization Optimization-based methods include those where the inner-level task (Eq. 6) is literally solved as an optimization problem, and focuses on extracting meta- knowledge ω required to improve optimization perfor- mance. The most famous of these is perhaps MAML [19], where the meta-knowledge ω is the initialization of the model parameters in the inner optimization, namely θ0. The goal is to learn θ0 such that a small number of inner steps on a small number of train instances produces a classifier that performs well on validation data. This is also performed by gradient descent, differentiating through the updates to the base model. More elaborate alternatives also learn step sizes [75], [76] or train recurrent networks to predict steps from gradients [41], [77], [78]. Meta-optimization by gradi- ent leads to the challenge of efficiently evaluating expen- sive second-order derivatives and differentiating through a graph of potentially thousands of inner optimization steps (see Section 6). For this reason it is often applied to few-shot learning where few inner-loop steps may be sufficient
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
<summary>[19] Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks</summary>
<br>
<!-- (model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md) -->

# model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md

<!-- REFERENCE -->


[Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks](../papers/model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md)

</details>



<details>
<summary>[74] Gradient-Based Meta-Learning With Learned Layerwise Metric And Subspace</summary>
<br>
<!-- (gradient_based_meta_learning_with_learned_layerwise_metric_and_subspace.md) -->

# gradient_based_meta_learning_with_learned_layerwise_metric_and_subspace.md

<!-- REFERENCE -->


[Gradient-Based Meta-Learning With Learned Layerwise Metric And Subspace](../papers/gradient_based_meta_learning_with_learned_layerwise_metric_and_subspace.md)

</details>



<details>
<summary>[73] Automated Relational Meta-learning</summary>
<br>
<!-- (automated_relational_meta_learning.md) -->

# automated_relational_meta_learning.md

<!-- REFERENCE -->


[Automated Relational Meta-learning](../papers/automated_relational_meta_learning.md)

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
<summary>[78] Learning To Learn By Gradient Descent By Gradient Descent</summary>
<br>
<!-- (learning_to_learn_by_gradient_descent_by_gradient_descent.md) -->

# learning_to_learn_by_gradient_descent_by_gradient_descent.md

<!-- REFERENCE -->


[Learning To Learn By Gradient Descent By Gradient Descent](../papers/learning_to_learn_by_gradient_descent_by_gradient_descent.md)

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

