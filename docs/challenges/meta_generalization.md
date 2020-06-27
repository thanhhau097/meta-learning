# meta_generalization
Meta-learning suffers from a gener- alization challenge across tasks analogous to the challenge of generalising across instances in conventional machine learning. There are three sub-challenges: (i) The first chal- lenge is fitting a meta-learner to a wide distribution of tasks p(T), which as we have seen is challenging for ex- isting methods [206], [207], [230], and may be partly due to conflicting gradients between tasks [285]. (ii) The second challenge is generalising from meta-train to novel meta- test tasks drawn from p(T). This is exacerbated because the number of tasks available for meta-training is typically low (much less than the number of instances available in conventional supervised learning), making it difficult to fit complex task distributions. Thus meta-learners’ biggest suc- cesses have thus far been within very similar task families. (iii) The third challenge is generalising to meta-test tasks drawn from a different distribution than the training tasks. This is inevitable in many potential practical applications of meta-learning, for example generalising few-shot visual learning from everyday training images of ImageNet to specialist domains such as medical images [208]. From the perspective of a learner, this is a meta-level generalization of the domain-shift problem, as observed in supervised learn- ing. Addressing these issues through meta-generalizations
of regularization, transfer learning, domain adaptation, and domain generalization are emerging directions [173]. Fur- thermore, we have yet to understand which kinds of meta- representations tend to generalize better under certain types of domain shifts. Another interesting direction could be investigating
how introducing yet another level of learning abstractions could affect generalization performance, that is, meta-meta- learning. By learning how to do meta-learning, perhaps we can find meta-optimizers that can generalize very strongly across a large variety of types and intensities of domain and even modality shifts. Of course computational costs would be exponentially larger.
<!-- REFERENCE -->


<details>
<summary>[285] Gradient Surgery For Multi-Task Learning</summary>
<br>
<!-- (gradient_surgery_for_multi_task_learning.md) -->

# gradient_surgery_for_multi_task_learning.md

<!-- REFERENCE -->


[Gradient Surgery For Multi-Task Learning](../papers/gradient_surgery_for_multi_task_learning.md)

</details>



<details>
<summary>[206] Learning Multiple Visual Domains With Residual Adapters</summary>
<br>
<!-- (learning_multiple_visual_domains_with_residual_adapters.md) -->

# learning_multiple_visual_domains_with_residual_adapters.md

<!-- REFERENCE -->


[Learning Multiple Visual Domains With Residual Adapters](../papers/learning_multiple_visual_domains_with_residual_adapters.md)

</details>



<details>
<summary>[230] Meta-world: A Benchmark And Evaluation For Multitask And Meta Reinforcement Learning</summary>
<br>
<!-- (meta_world_a_benchmark_and_evaluation_for_multitask_and_meta_reinforcement_learning.md) -->

# meta_world_a_benchmark_and_evaluation_for_multitask_and_meta_reinforcement_learning.md

<!-- REFERENCE -->


[Meta-world: A Benchmark And Evaluation For Multitask And Meta Reinforcement Learning](../papers/meta_world_a_benchmark_and_evaluation_for_multitask_and_meta_reinforcement_learning.md)

</details>



<details>
<summary>[208] A New Benchmark For Evaluation Of Cross-Domain Few-Shot Learning</summary>
<br>
<!-- (a_new_benchmark_for_evaluation_of_cross_domain_few_shot_learning.md) -->

# a_new_benchmark_for_evaluation_of_cross_domain_few_shot_learning.md

<!-- REFERENCE -->


[A New Benchmark For Evaluation Of Cross-Domain Few-Shot Learning](../papers/a_new_benchmark_for_evaluation_of_cross_domain_few_shot_learning.md)

</details>



<details>
<summary>[207] Meta-Dataset: A Dataset Of Datasets For Learning To Learn From Few Examples</summary>
<br>
<!-- (meta_dataset_a_dataset_of_datasets_for_learning_to_learn_from_few_examples.md) -->

# meta_dataset_a_dataset_of_datasets_for_learning_to_learn_from_few_examples.md

<!-- REFERENCE -->


[Meta-Dataset: A Dataset Of Datasets For Learning To Learn From Few Examples](../papers/meta_dataset_a_dataset_of_datasets_for_learning_to_learn_from_few_examples.md)

</details>

