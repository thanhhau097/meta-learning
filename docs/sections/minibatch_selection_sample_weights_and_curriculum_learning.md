# minibatch_selection_sample_weights_and_curriculum_learning

When the base algorithm is minibatch-based stochastic gradient descent, a design parameter of the learning strategy is the batch selection process. Various hand-designed methods [137] exist to improve on classic randomly-sampled minibatches. Meta-learning approaches to mini-batch selection define ω as an instance selection probability [138] or small neural network that picks or excludes instances [139] for inclusion in the next minibatch, while the meta-loss can be defined as the learning progress of the base model given the defined mini-batch selector. Such selection methods can also provide a way to auto-
mate the learning of a curriculum. In conventional machine learning, curricula are sequences of data or concepts to learn that are hand-designed to produce better performance than learning items in a random order [140], for instance by focusing on instances of the right difficulty while rejecting too hard or too easy (already learned) instances. Meta- learning has the potential to automate this process and select examples of the right difficulty by defining the teaching policy as the meta-knowledge and training it to optimize the progress of the student [139], [141]. Related to mini-batch selection policies are methods that
learn per-sample loss weights ω for the training set [142], [143]. This can be used to learn under label-noise by dis- counting noisy samples [142], [143], discount outliers [67], or correct for class imbalance [142].
<!-- REFERENCE -->


<details>
<summary>[137] Active Mini-batch ¨ Sampling Using Repulsive Point Processes</summary>
<br>
<!-- (active_mini_batch_sampling_using_repulsive_point_processes.md) -->

# active_mini_batch_sampling_using_repulsive_point_processes.md

<!-- REFERENCE -->


[Active Mini-batch ¨ Sampling Using Repulsive Point Processes](../papers/active_mini_batch_sampling_using_repulsive_point_processes.md)

</details>



<details>
<summary>[138] Online Batch Selection For Faster Training Of Neural Networks</summary>
<br>
<!-- (online_batch_selection_for_faster_training_of_neural_networks.md) -->

# online_batch_selection_for_faster_training_of_neural_networks.md

<!-- REFERENCE -->


[Online Batch Selection For Faster Training Of Neural Networks](../papers/online_batch_selection_for_faster_training_of_neural_networks.md)

</details>



<details>
<summary>[143] Learning To Reweight Examples For Robust Deep Learning</summary>
<br>
<!-- (learning_to_reweight_examples_for_robust_deep_learning.md) -->

# learning_to_reweight_examples_for_robust_deep_learning.md

<!-- REFERENCE -->


[Learning To Reweight Examples For Robust Deep Learning](../papers/learning_to_reweight_examples_for_robust_deep_learning.md)

</details>



<details>
<summary>[139] Learning To Teach</summary>
<br>
<!-- (learning_to_teach.md) -->

# learning_to_teach.md

<!-- REFERENCE -->


[Learning To Teach](../papers/learning_to_teach.md)

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
<summary>[140] Curriculum Learning</summary>
<br>
<!-- (curriculum_learning.md) -->

# curriculum_learning.md

<!-- REFERENCE -->


[Curriculum Learning](../papers/curriculum_learning.md)

</details>



<details>
<summary>[142] Meta-Weight-Net: Learning An Explicit Mapping For Sample Weighting</summary>
<br>
<!-- (meta_weight_net_learning_an_explicit_mapping_for_sample_weighting.md) -->

# meta_weight_net_learning_an_explicit_mapping_for_sample_weighting.md

<!-- REFERENCE -->


[Meta-Weight-Net: Learning An Explicit Mapping For Sample Weighting](../papers/meta_weight_net_learning_an_explicit_mapping_for_sample_weighting.md)

</details>



<details>
<summary>[141] Mentornet: Learning Data-driven Curriculum For Very Deep Neural Networks On Corrupted Labels</summary>
<br>
<!-- (mentornet_learning_data_driven_curriculum_for_very_deep_neural_networks_on_corrupted_labels.md) -->

# mentornet_learning_data_driven_curriculum_for_very_deep_neural_networks_on_corrupted_labels.md

<!-- REFERENCE -->


[Mentornet: Learning Data-driven Curriculum For Very Deep Neural Networks On Corrupted Labels](../papers/mentornet_learning_data_driven_curriculum_for_very_deep_neural_networks_on_corrupted_labels.md)

</details>

