# reinforcement_learning
When the base learner includes non-differentiable steps [133], or the meta-objective <img src="https://render.githubusercontent.com/render/math?math=\mathcal{L}^{m e t a}"> is itself non-differentiable [117],
 many methods [22] resort to RL to optimize the outer objective Eq. 5. This estimates the gradient <img src="https://render.githubusercontent.com/render/math?math=\nabla_{\omega} \mathcal{L}^{\text {meta}}">, 
 typically using the policy gradient theorem. However, alleviating the requirement for differentiability in this way 
 is typically extremely costly. High-variance policy-gradient estimates for <img src="https://render.githubusercontent.com/render/math?math=\nabla_{\omega} \mathcal{L}^{\text {meta}}"> mean that many 
outer-level optimization steps are required to converge, and each of these steps are themselves costly due to wrapping task-model optimization within them.
<!-- REFERENCE -->


<details>
<summary>[117] Addressing The Loss-Metric Mismatch With Adaptive Loss Alignment</summary>
<br>
<!-- (addressing_the_loss_metric_mismatch_with_adaptive_loss_alignment.md) -->

# addressing_the_loss_metric_mismatch_with_adaptive_loss_alignment.md

<!-- REFERENCE -->


[Addressing The Loss-Metric Mismatch With Adaptive Loss Alignment](../papers/addressing_the_loss_metric_mismatch_with_adaptive_loss_alignment.md)

</details>



<details>
<summary>[133] AutoAugment: Learning Augmentation Policies From Data</summary>
<br>
<!-- (autoaugment_learning_augmentation_policies_from_data.md) -->

# autoaugment_learning_augmentation_policies_from_data.md

<!-- REFERENCE -->


[AutoAugment: Learning Augmentation Policies From Data](../papers/autoaugment_learning_augmentation_policies_from_data.md)

</details>



<details>
<summary>[22] RL2 : Fast Reinforcement Learning Via Slow Reinforcement Learning</summary>
<br>
<!-- (rl2_fast_reinforcement_learning_via_slow_reinforcement_learning.md) -->

# rl2_fast_reinforcement_learning_via_slow_reinforcement_learning.md

<!-- REFERENCE -->


[RL2 : Fast Reinforcement Learning Via Slow Reinforcement Learning](../papers/rl2_fast_reinforcement_learning_via_slow_reinforcement_learning.md)

</details>

