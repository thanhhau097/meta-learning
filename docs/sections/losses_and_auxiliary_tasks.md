# losses_and_auxiliary_tasks
Analogously to the meta- learning approach to optimizer design, these approaches aim to learn the inner task-loss <img src="https://render.githubusercontent.com/render/math?math=\mathcal{L}_{\omega}^{\operatorname{task}}(.)"> for the base model.
Loss-learning approaches typically define a small neural network that inputs quantities that are typically inputs to losses (e.g., predictions, features, or model parameters) and outputs a scalar to be treated as a loss by the inner (task) optimizer. This has potential benefits such as leading to a learned loss that is easier to optimize (e.g., less local minima) than commonly used ones [23], [112], [113], 
leads to faster learning with improved generalization [45], [114], [115], or one whose minima correspond to a model more robust to domain shift [44]. 
Furthermore, loss learning methods have also been used to learn to learn from unlabeled instances [98], [116]. Other applications include learning <img src="https://render.githubusercontent.com/render/math?math=\mathcal{L}_{\omega}^{\operatorname{task}}(.)"> as
a differentiable approximation to a true non-differentiable task loss such as area under precision recall curve [117], [118].

<!-- REFERENCE -->


<details>
<summary>[116] Semi-Supervised Few-Shot Learning With MAML</summary>
<br>
<!-- (semi_supervised_few_shot_learning_with_maml.md) -->

# semi_supervised_few_shot_learning_with_maml.md

<!-- REFERENCE -->


[Semi-Supervised Few-Shot Learning With MAML](../papers/semi_supervised_few_shot_learning_with_maml.md)

</details>



<details>
<summary>[113] Online Meta-Critic Learning For Off-Policy Actor-Critic Methods</summary>
<br>
<!-- (online_meta_critic_learning_for_off_policy_actor_critic_methods.md) -->

# online_meta_critic_learning_for_off_policy_actor_critic_methods.md

<!-- REFERENCE -->


[Online Meta-Critic Learning For Off-Policy Actor-Critic Methods](../papers/online_meta_critic_learning_for_off_policy_actor_critic_methods.md)

</details>



<details>
<summary>[114] OnlineWithin-Online Meta-Learning</summary>
<br>
<!-- (onlinewithin_online_meta_learning.md) -->

# onlinewithin_online_meta_learning.md

<!-- REFERENCE -->


[OnlineWithin-Online Meta-Learning](../papers/onlinewithin_online_meta_learning.md)

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
<summary>[44] Feature-Critic Networks For Heterogeneous Domain Generalization</summary>
<br>
<!-- (feature_critic_networks_for_heterogeneous_domain_generalization.md) -->

# feature_critic_networks_for_heterogeneous_domain_generalization.md

<!-- REFERENCE -->


[Feature-Critic Networks For Heterogeneous Domain Generalization](../papers/feature_critic_networks_for_heterogeneous_domain_generalization.md)

</details>



<details>
<summary>[98] Learning To Learn By SelfCritique</summary>
<br>
<!-- (learning_to_learn_by_selfcritique.md) -->

# learning_to_learn_by_selfcritique.md

<!-- REFERENCE -->


[Learning To Learn By SelfCritique](../papers/learning_to_learn_by_selfcritique.md)

</details>



<details>
<summary>[117] Addressing The Loss-Metric Mismatch With Adaptive Loss Alignment</summary>
<br>
<!-- (addressing_the_loss_metric_mismatch_with_adaptive_loss_alignment.md) -->

# addressing_the_loss_metric_mismatch_with_adaptive_loss_alignment.md

<!-- REFERENCE -->


[Addressing The Loss-Metric Mismatch With Adaptive Loss Alignment](../papers/addressing_the_loss_metric_mismatch_with_adaptive_loss_alignment.md)

</details>



<details>
<summary>[112] Learning To Learn: Meta-critic Networks For Sample Efficient Learning</summary>
<br>
<!-- (learning_to_learn_meta_critic_networks_for_sample_efficient_learning.md) -->

# learning_to_learn_meta_critic_networks_for_sample_efficient_learning.md

<!-- REFERENCE -->


[Learning To Learn: Meta-critic Networks For Sample Efficient Learning](../papers/learning_to_learn_meta_critic_networks_for_sample_efficient_learning.md)

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
<summary>[118] Learning Surrogate Losses</summary>
<br>
<!-- (learning_surrogate_losses.md) -->

# learning_surrogate_losses.md

<!-- REFERENCE -->


[Learning Surrogate Losses](../papers/learning_surrogate_losses.md)

</details>



<details>
<summary>[45] Learning To Learn Around A Common Mean</summary>
<br>
<!-- (learning_to_learn_around_a_common_mean.md) -->

# learning_to_learn_around_a_common_mean.md

<!-- REFERENCE -->


[Learning To Learn Around A Common Mean](../papers/learning_to_learn_around_a_common_mean.md)

</details>

