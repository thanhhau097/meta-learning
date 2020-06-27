# Taxonomy

We introduce a new breakdown along three independent axes. For each axis we provide a taxonomy that reflects the current meta-learning landscape.

Meta-Representation (“What?”) The first axis is the choice of representation of meta-knowledge ω. This could span an estimate of model parameters [19] used for opti- mizer initialization, to readable code in the case of program induction [89]. Note that the base model representation θ is usually application-specific, for example a convolutional neural network (CNN) [1] in the case of computer vision.

Meta-Optimizer (“How?”) The second axis is the choice of optimizer to use for the outer level during meta-training (see Eq. 5)1. The outer-level optimizer for ω can take a va- riety of forms from gradient-descent [19], to reinforcement learning [89] and evolutionary search [23]. 

Meta-Objective (“Why?”) The third axis is the goal of meta-learning which is determined by choice of meta- objective L_meta (Eq. 5), task distribution p(T), and data- flow between the two levels. Together these can customize meta-learning for different purposes such as sample efficient few-shot learning [19], [40], fast many-shot optimization [89], [91], or robustness to domain-shift [44], [92], label noise [93], and adversarial attack [94].
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
<summary>[93] Learning To Learn From Noisy Labeled Data</summary>
<br>
<!-- (learning_to_learn_from_noisy_labeled_data.md) -->

# learning_to_learn_from_noisy_labeled_data.md

<!-- REFERENCE -->


[Learning To Learn From Noisy Labeled Data](../papers/learning_to_learn_from_noisy_labeled_data.md)

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
<summary>[94] Adversarially Robust Few-shot Learning: A Meta-learning Approach</summary>
<br>
<!-- (adversarially_robust_few_shot_learning_a_meta_learning_approach.md) -->

# adversarially_robust_few_shot_learning_a_meta_learning_approach.md

<!-- REFERENCE -->


[Adversarially Robust Few-shot Learning: A Meta-learning Approach](../papers/adversarially_robust_few_shot_learning_a_meta_learning_approach.md)

</details>



<details>
<summary>[40] A Simple Neural Attentive Meta-learner</summary>
<br>
<!-- (a_simple_neural_attentive_meta_learner.md) -->

# a_simple_neural_attentive_meta_learner.md
## What?
- A meta-learner architecture that use a novel combination of temporal convolutions and soft attention; the former to aggregate information from past experience and the latter to pinpoint specific pieces of information.
## Why?
- Handle the problems: architectures specialized to a particular application, or hard-coding algorithmic components that constrain how the meta-learner solves the task
## How?
![alt text](../images/snail.png)
![alt text](../images/snail_dense.png)
![alt text](../images/snail_tc_attention.png)
## Results? (What did they find?)
- Effective black-box using self attention 
- Note:
    - trained the SNAIL on episodes where the number of shots K was chosen uniformly at random from 1 to 5 (note that this is unlike prior works, who train separate models for each shot)
    - complicated architecture, not sure that can compare with original MAML
## Ideas to improve?

<!-- REFERENCE -->


[A Simple Neural Attentive Meta-learner](../papers/a_simple_neural_attentive_meta_learner.md)

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
<summary>[1] Deep Residual Learning For Image Recognition</summary>
<br>
<!-- (deep_residual_learning_for_image_recognition.md) -->

# deep_residual_learning_for_image_recognition.md

<!-- REFERENCE -->


[Deep Residual Learning For Image Recognition](../papers/deep_residual_learning_for_image_recognition.md)

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
<summary>[92] MetaReg: Towards Domain Generalization Using Meta-Regularization</summary>
<br>
<!-- (metareg_towards_domain_generalization_using_meta_regularization.md) -->

# metareg_towards_domain_generalization_using_meta_regularization.md

<!-- REFERENCE -->


[MetaReg: Towards Domain Generalization Using Meta-Regularization](../papers/metareg_towards_domain_generalization_using_meta_regularization.md)

</details>



<details>
<summary>[44] Feature-Critic Networks For Heterogeneous Domain Generalization</summary>
<br>
<!-- (feature_critic_networks_for_heterogeneous_domain_generalization.md) -->

# feature_critic_networks_for_heterogeneous_domain_generalization.md

<!-- REFERENCE -->


[Feature-Critic Networks For Heterogeneous Domain Generalization](../papers/feature_critic_networks_for_heterogeneous_domain_generalization.md)

</details>

