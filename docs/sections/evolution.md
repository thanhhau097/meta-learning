# evolution

Another approach for optimizing the meta- objective are evolutionary algorithms (EA) [17], [123], [181]. Many evolutionary algorithms have strong connections to reinforcement learning algorithms [182]. However, their performance does not depend on the length and reward sparsity of the inner optimization as for RL. EAs are attractive for several reasons [181] : (i) They can
optimize any type of base model and meta-objective with no requirement on differentiability. (ii) They do not rely on backpropagation, which rectifies both gradient degradation issues and avoids the cost of high-order gradient compu- tation required by conventional gradient-based methods above. (iii) They are highly parallelizable, making meta- training more easily scalable. (iv) By maintaining a diverse population of solutions, they can avoid local minima that plague gradient-based methods [123]. However, they have a number of disadvantages: (i) The size of the population required to train a model increases rapidly with the number of learn-able parameters. (ii) They can be sensitive to the mutation strategy (e.g., magnitude and direction of noise) and thus may require careful hyperparameter optimization. (iii) Their fitting ability is generally inferior to gradient- based methods, especially for large models such as CNNs. EAs are relatively more commonly applied in RL applications [23], [158] (where models are typically smaller
and inner optimizations are long and non-differentiable). However they have also been applied to learn learning rules [183], optimizers [184], architectures [27], [123] and data augmentation strategies [135] in supervised learning. They are also particularly important in learning human interpretable symbolic meta-representations [115].


<!-- REFERENCE -->


<details>
<summary>[135] Model Vulnerability To Distributional Shifts Over Image Transformation Sets</summary>
<br>
<!-- (model_vulnerability_to_distributional_shifts_over_image_transformation_sets.md) -->

# model_vulnerability_to_distributional_shifts_over_image_transformation_sets.md

<!-- REFERENCE -->


[Model Vulnerability To Distributional Shifts Over Image Transformation Sets](../papers/model_vulnerability_to_distributional_shifts_over_image_transformation_sets.md)

</details>



<details>
<summary>[123] Designing Neural Networks Through Neuroevolution</summary>
<br>
<!-- (designing_neural_networks_through_neuroevolution.md) -->

# designing_neural_networks_through_neuroevolution.md

<!-- REFERENCE -->


[Designing Neural Networks Through Neuroevolution](../papers/designing_neural_networks_through_neuroevolution.md)

</details>



<details>
<summary>[115] Improved Training Speed, Accuracy, And Data Utilization Through Loss Function Optimization</summary>
<br>
<!-- (improved_training_speed_accuracy_and_data_utilization_through_loss_function_optimization.md) -->

# improved_training_speed_accuracy_and_data_utilization_through_loss_function_optimization.md

<!-- REFERENCE -->


[Improved Training Speed, Accuracy, And Data Utilization Through Loss Function Optimization](../papers/improved_training_speed_accuracy_and_data_utilization_through_loss_function_optimization.md)

</details>



<details>
<summary>[182] Robot Skill Learning: From Reinforcement Learning To Evolution Strategies</summary>
<br>
<!-- (robot_skill_learning_from_reinforcement_learning_to_evolution_strategies.md) -->

# robot_skill_learning_from_reinforcement_learning_to_evolution_strategies.md

<!-- REFERENCE -->


[Robot Skill Learning: From Reinforcement Learning To Evolution Strategies](../papers/robot_skill_learning_from_reinforcement_learning_to_evolution_strategies.md)

</details>



<details>
<summary>[23] Evolved Policy Gradients</summary>
<br>
<!-- (evolved_policy_gradients.md) -->

# evolved_policy_gradients.md

<!-- REFERENCE -->


[Evolved Policy Gradients](../papers/evolved_policy_gradients.md)

</details>



<details>
<summary>[158] ES-MAML: Simple Hessian-Free Meta Learning</summary>
<br>
<!-- (es_maml_simple_hessian_free_meta_learning.md) -->

# es_maml_simple_hessian_free_meta_learning.md

<!-- REFERENCE -->


[ES-MAML: Simple Hessian-Free Meta Learning](../papers/es_maml_simple_hessian_free_meta_learning.md)

</details>



<details>
<summary>[183] Born To Learn: The Inspiration, Progress, And Future Of Evolved Plastic Artificial Neural Networks</summary>
<br>
<!-- (born_to_learn_the_inspiration_progress_and_future_of_evolved_plastic_artificial_neural_networks.md) -->

# born_to_learn_the_inspiration_progress_and_future_of_evolved_plastic_artificial_neural_networks.md

<!-- REFERENCE -->


[Born To Learn: The Inspiration, Progress, And Future Of Evolved Plastic Artificial Neural Networks](../papers/born_to_learn_the_inspiration_progress_and_future_of_evolved_plastic_artificial_neural_networks.md)

</details>



<details>
<summary>[17] Evolutionary Principles In Self-referential Learning</summary>
<br>
<!-- (evolutionary_principles_in_self_referential_learning.md) -->

# evolutionary_principles_in_self_referential_learning.md

<!-- REFERENCE -->


[Evolutionary Principles In Self-referential Learning](../papers/evolutionary_principles_in_self_referential_learning.md)

</details>



<details>
<summary>[27] Regularized Evolution For Image Classifier Architecture Search</summary>
<br>
<!-- (regularized_evolution_for_image_classifier_architecture_search.md) -->

# regularized_evolution_for_image_classifier_architecture_search.md

<!-- REFERENCE -->


[Regularized Evolution For Image Classifier Architecture Search](../papers/regularized_evolution_for_image_classifier_architecture_search.md)

</details>



<details>
<summary>[181] Evolution Strategies As A Scalable Alternative To Reinforcement Learning</summary>
<br>
<!-- (evolution_strategies_as_a_scalable_alternative_to_reinforcement_learning.md) -->

# evolution_strategies_as_a_scalable_alternative_to_reinforcement_learning.md

<!-- REFERENCE -->


[Evolution Strategies As A Scalable Alternative To Reinforcement Learning](../papers/evolution_strategies_as_a_scalable_alternative_to_reinforcement_learning.md)

</details>



<details>
<summary>[184] Learning To Optimize In Swarms</summary>
<br>
<!-- (learning_to_optimize_in_swarms.md) -->

# learning_to_optimize_in_swarms.md

<!-- REFERENCE -->


[Learning To Optimize In Swarms](../papers/learning_to_optimize_in_swarms.md)

</details>

