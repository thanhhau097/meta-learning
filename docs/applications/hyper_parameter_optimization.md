# hyper_parameter_optimization

Meta-learning can address hyperparameter optimization by considering ω to specify hyperparameters, such as regu- larization strength or learning rate. There are two main settings: we can learn hyperparameters that improve train- ing over a distribution of tasks, or hyperparameters that improve learning for a single task. The former case is usually relevant in few-shot applications, especially in optimization based methods. For instance, MAML can be improved by learning a learning rate per layer per step [76]. The case where we wish to learn hyperparameters for a single task is usually more relevant for many-shot applications [145], where some validation data can be extracted from the training dataset, as discussed in Section 2.1. Meta- learning over long inner horizons comes with memory and compute scaling issues, which is an active research area as discussed in Section 6. However, it is noteworthy that end-to-end gradient-based meta-learning has already
demonstrated promising scalability to millions of param- eters (as demonstrated by MAML [19], [145] and Dataset Distillation [144], [145], for example) in contrast to the classic approaches (such cross-validation by grid or random [69] search, or Bayesian Optimization [70]) which are usually only successful with dozens of hyper-parameters.
<!-- REFERENCE -->


<details>
<summary>[145] Optimizing Millions Of Hyperparameters By Implicit Differentiation</summary>
<br>
<!-- (optimizing_millions_of_hyperparameters_by_implicit_differentiation.md) -->

# optimizing_millions_of_hyperparameters_by_implicit_differentiation.md

<!-- REFERENCE -->


[Optimizing Millions Of Hyperparameters By Implicit Differentiation](../papers/optimizing_millions_of_hyperparameters_by_implicit_differentiation.md)

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
<summary>[144] Dataset Distillation</summary>
<br>
<!-- (dataset_distillation.md) -->

# dataset_distillation.md

<!-- REFERENCE -->


[Dataset Distillation](../papers/dataset_distillation.md)

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
<summary>[76] How To Train Your MAML</summary>
<br>
<!-- (how_to_train_your_maml.md) -->

# how_to_train_your_maml.md

<!-- REFERENCE -->


[How To Train Your MAML](../papers/how_to_train_your_maml.md)

</details>



<details>
<summary>[69] Random Search For Hyper-Parameter Optimization</summary>
<br>
<!-- (random_search_for_hyper_parameter_optimization.md) -->

# random_search_for_hyper_parameter_optimization.md

<!-- REFERENCE -->


[Random Search For Hyper-Parameter Optimization](../papers/random_search_for_hyper_parameter_optimization.md)

</details>

