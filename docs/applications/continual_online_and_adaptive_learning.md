# continual_online_and_adaptive_learning
**Continual Learning** refers to the humanlike capability of
learning tasks presented in sequence. Ideally this is done while exploiting forward transfer so new tasks are learned better given past experience, without forgetting previously learned tasks, and without needing to store all past data for rehearsal against forgetting [60]. Deep Neural Networks struggle at meeting these criteria, especially as they tend to forget information seen in earlier tasks – a phenomenon known as catastrophic forgetting. Meta-learning has been applied to improve continual learning in deep nets. The requirements of continual learning can be integrated into a meta-objective, for example by defining a sequence of learning episodes in which the support set contains one new task, but the query set contains examples drawn from all tasks seen until now [160], [161]. With this meta-objective design, various meta-representations can be trained so as to improve continual learning performance. For example: weight priors [128], gradient descent preconditioning ma- trices [161], or RNN learned optimizers [160], or feature representations [253].

Although not directly applied to continual learning,
another interesting idea is meta-training representations to support local editing [254] where the authors learn a model that can quickly improve itself on single samples, without forgetting any of the information it already has learned.

**Online and Adaptive Learning** also consider tasks ar- riving in a stream, but are concerned with the ability to effectively adapt to the current task in the stream, more than remembering the old tasks. To this end an online exten- sion of MAML was proposed [96] to perform MAML-style meta-training online during a task sequence. Meanwhile others [61]–[63] consider the setting where meta-training is performed in advance on source tasks, before meta-testing adaptation capabilities on a sequence of target tasks

**Benchmarks** There exist a number of benchmarks for continual learning that work quite well with standard deep learning methods. However, most of those benchmarks cannot readily work with meta-learning approaches. Most of them would require adjustments to their sample gener- ation routines to include a large number of explicit learn- ing sets and an explicit evaluation sets. Some early steps were made towards defining meta-learning ready contin- ual benchmarks in [96], [160], [253], mainly composed of Omniglot and perturbed versions of MNIST. However, most of those were simply tasks built to demonstrate a method. More explicit benchmark work can be found in [205], where Continual Few-Shot Learning is defined as a new type of task to be tackled, and the benchmark is built for meta and non meta-learning approaches alike. In this setting, a task is composed by a number of small training sets, each potentially made of different classes, after which the learned model should generalize well on previously unseen samples from all the tasks it learned from. The benchmark proposes the usage of Omniglot and SlimageNet as the datasets to be used.

<!-- REFERENCE -->


<details>
<summary>[96] Online Metalearning</summary>
<br>
<!-- (online_metalearning.md) -->

# online_metalearning.md

<!-- REFERENCE -->


[Online Metalearning](../papers/online_metalearning.md)

</details>



<details>
<summary>[63] Learning To Adapt In Dynamic, RealWorld Environments Through Meta-Reinforcement Learning</summary>
<br>
<!-- (learning_to_adapt_in_dynamic_realworld_environments_through_meta_reinforcement_learning.md) -->

# learning_to_adapt_in_dynamic_realworld_environments_through_meta_reinforcement_learning.md

<!-- REFERENCE -->


[Learning To Adapt In Dynamic, RealWorld Environments Through Meta-Reinforcement Learning](../papers/learning_to_adapt_in_dynamic_realworld_environments_through_meta_reinforcement_learning.md)

</details>



<details>
<summary>[205] Defining Benchmarks For Continual Few-shot Learning</summary>
<br>
<!-- (defining_benchmarks_for_continual_few_shot_learning.md) -->

# defining_benchmarks_for_continual_few_shot_learning.md

<!-- REFERENCE -->


[Defining Benchmarks For Continual Few-shot Learning](../papers/defining_benchmarks_for_continual_few_shot_learning.md)

</details>



<details>
<summary>[160] Meta Continual Learning</summary>
<br>
<!-- (meta_continual_learning.md) -->

# meta_continual_learning.md

<!-- REFERENCE -->


[Meta Continual Learning](../papers/meta_continual_learning.md)

</details>



<details>
<summary>[161] Meta-Learning With Warped Gradient Descent</summary>
<br>
<!-- (meta_learning_with_warped_gradient_descent.md) -->

# meta_learning_with_warped_gradient_descent.md

<!-- REFERENCE -->


[Meta-Learning With Warped Gradient Descent](../papers/meta_learning_with_warped_gradient_descent.md)

</details>



<details>
<summary>[128] Incremental Few-shot Learning With Attention Attractor Networks</summary>
<br>
<!-- (incremental_few_shot_learning_with_attention_attractor_networks.md) -->

# incremental_few_shot_learning_with_attention_attractor_networks.md

<!-- REFERENCE -->


[Incremental Few-shot Learning With Attention Attractor Networks](../papers/incremental_few_shot_learning_with_attention_attractor_networks.md)

</details>



<details>
<summary>[253] Meta-learning Representations For Continual Learning</summary>
<br>
<!-- (meta_learning_representations_for_continual_learning.md) -->

# meta_learning_representations_for_continual_learning.md

<!-- REFERENCE -->


[Meta-learning Representations For Continual Learning](../papers/meta_learning_representations_for_continual_learning.md)

</details>



<details>
<summary>[61] Continuous Adaptation Via Meta-Learning In Nonstationary And Competitive Environments</summary>
<br>
<!-- (continuous_adaptation_via_meta_learning_in_nonstationary_and_competitive_environments.md) -->

# continuous_adaptation_via_meta_learning_in_nonstationary_and_competitive_environments.md

<!-- REFERENCE -->


[Continuous Adaptation Via Meta-Learning In Nonstationary And Competitive Environments](../papers/continuous_adaptation_via_meta_learning_in_nonstationary_and_competitive_environments.md)

</details>



<details>
<summary>[60] Lifelong Machine Learning, Second Edition</summary>
<br>
<!-- (lifelong_machine_learning_second_edition.md) -->

# lifelong_machine_learning_second_edition.md

<!-- REFERENCE -->


[Lifelong Machine Learning, Second Edition](../papers/lifelong_machine_learning_second_edition.md)

</details>



<details>
<summary>[254] Editable Neural Networks</summary>
<br>
<!-- (editable_neural_networks.md) -->

# editable_neural_networks.md

<!-- REFERENCE -->


[Editable Neural Networks](../papers/editable_neural_networks.md)

</details>

