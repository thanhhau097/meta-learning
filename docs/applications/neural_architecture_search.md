# neural_architecture_search
Architecture search [26]–[28], [39], [123] can be seen as cor- responding to a kind hyperparameter optimization where ω specifies the architecture of a neural network. The inner optimization trains networks with the specified architecture, and the outer optimization searches for architectures with good validation performance. NAS methods are commonly analysed [39] according to ‘search space’, ‘search strategy’, and ‘performance estimation strategy. These correspond to the hypothesis space for ω, the meta-optimization strategy, and the meta-objective. NAS is particularly challenging because: (i) Fully evaluating the inner loop is generally very expensive since it requires training a many-shot neural network to completion. This leads to approximations such
as sub-sampling the train set, early termination of the inner loop, and ultimately approximations such as interleaved descent on both ω and θ [26] as in online meta-learning. (ii.) The search space is hard to define, and optimizing it is costly. This is because most search spaces are broad, and represent architectures that aren’t differentiable. This leads to methods that perform cell-level search [26], [28] to constrain the search space; and then rely on RL [28], discrete gradient estimators that provide a differentiable approximation to the search space [26], [124], and evolution [27], [123].

Examples Some notable examples include: (i) NASNet [28], [234] where the search space is restricted to cell-level learning, and defined as a string generated by an RNN which indicates what operations should be at what parts of the cell-tree, optimized using RL. (ii) Reqularized Evolution [27] where the authors use NASNet’s search space but optimize it using regularized evolution, i.e. standard tour- nament based evolution with removal of oldest individuals after every iteration. (iii.) DARTS [26] where the authors carefully cast the space of cell architectures as a sequence of softmax selections over a number of pre-selected operations, thus making the search space differentiable. Learning the architecture then corresponds to jointly learning the softmax weights with the network parameters. This allows architec- ture learning to be sped up by 2-3 levels of magnitude both in computational overheads and wall-clock time. (iv) T-NAS [125] where the authors utilize the DARTS search space, but train it using a data-flow that enforces the architecture to be learned using very few data-points and very few updates, while keeping the generalization performance high. As a result of learning such softmax weights, they achieve few- shot architecture search. Once trained, these weights can be adapted to new tasks within seconds rather than days.

An interesting special case of NAS is activation func-
tion search [151]. While hand-designed activation functions such as ReLU are dominant in NN literature, a successful example of NAS meta-learning is the discovery of the Swish activation function [151] with RL in the space of symbolic activation functions. Swish has gone on to contribute to several influential state-of-the-art and general purpose CNN architectures [235], [236]

**Multi-Objective NAS** Architectures to be deployed on mobile devices have additional constraints besides valida- tion accuracy [7], and NAS can also be deployed to produce compact and efficient models [237]. This can be realised by defining a multi-objective meta-objective that contains terms related both to validation performance as well as latency or size of the model product by a given θ, and thus leading to good performance-cost tradeoffs.

**Topical Issues** While NAS itself can be seen as an instance of hyper-parameter or hypothesis-class meta-learning, it can also interact with meta-learning in other forms. Since NAS is costly, a topical issue is whether discovered architectures are dataset specific, or general purpose with ability to generalize to new problems [234]. Recent results suggest that meta- training across multiple datasets can lead to improved cross- task generalization of architectures [126]. While few-shot meta-learning is typically addressed
from a parameter learning perspective in the context of hand-crafted architectures [19], [20], [87], one can also define NAS meta-objectives to train an architecture suitable for few-shot learning [238], [239]. Furthermore, analogously to fast-adapting initial condition meta-learning approaches such as MAML [19], one can train good initial architectures [125] or architecture priors [126] that are easy to adapt towards specific tasks.

**Benchmarks NAS** is often evaluated on the CIFAR-10 dataset. However even on this small dataset, architecture search is costly to perform, making it inaccessible to many researchers; and furthermore results are hard to reproduce due to other confounding factors such as tuning of hy- perparameters [240]. To support reproducible and accessi- ble research, the recently released NASbenches [241], [242] provides pre-computed performance measures for a large number of network architectures.
<!-- REFERENCE -->


<details>
<summary>[26] DARTS: Differentiable Architecture Search</summary>
<br>
<!-- (darts_differentiable_architecture_search.md) -->

# darts_differentiable_architecture_search.md

<!-- REFERENCE -->


[DARTS: Differentiable Architecture Search](../papers/darts_differentiable_architecture_search.md)

</details>



<details>
<summary>[242] NAS-Bench-201: Extending The Scope Of Reproducible Neural Architecture Search</summary>
<br>
<!-- (nas_bench_201_extending_the_scope_of_reproducible_neural_architecture_search.md) -->

# nas_bench_201_extending_the_scope_of_reproducible_neural_architecture_search.md

<!-- REFERENCE -->


[NAS-Bench-201: Extending The Scope Of Reproducible Neural Architecture Search](../papers/nas_bench_201_extending_the_scope_of_reproducible_neural_architecture_search.md)

</details>



<details>
<summary>[240] Random Search And Reproducibility For Neural Architecture Search</summary>
<br>
<!-- (random_search_and_reproducibility_for_neural_architecture_search.md) -->

# random_search_and_reproducibility_for_neural_architecture_search.md

<!-- REFERENCE -->


[Random Search And Reproducibility For Neural Architecture Search](../papers/random_search_and_reproducibility_for_neural_architecture_search.md)

</details>



<details>
<summary>[239] Meta-Learning Of Neural Architectures For Few-Shot Learning</summary>
<br>
<!-- (meta_learning_of_neural_architectures_for_few_shot_learning.md) -->

# meta_learning_of_neural_architectures_for_few_shot_learning.md

<!-- REFERENCE -->


[Meta-Learning Of Neural Architectures For Few-Shot Learning](../papers/meta_learning_of_neural_architectures_for_few_shot_learning.md)

</details>



<details>
<summary>[235] EfficientNet: Rethinking Model Scaling For Convolutional Neural Networks</summary>
<br>
<!-- (efficientnet_rethinking_model_scaling_for_convolutional_neural_networks.md) -->

# efficientnet_rethinking_model_scaling_for_convolutional_neural_networks.md

<!-- REFERENCE -->


[EfficientNet: Rethinking Model Scaling For Convolutional Neural Networks](../papers/efficientnet_rethinking_model_scaling_for_convolutional_neural_networks.md)

</details>



<details>
<summary>[125] Towards Fast Adaptation Of Neural Architectures With Meta Learning</summary>
<br>
<!-- (towards_fast_adaptation_of_neural_architectures_with_meta_learning.md) -->

# towards_fast_adaptation_of_neural_architectures_with_meta_learning.md

<!-- REFERENCE -->


[Towards Fast Adaptation Of Neural Architectures With Meta Learning](../papers/towards_fast_adaptation_of_neural_architectures_with_meta_learning.md)

</details>



<details>
<summary>[20] Prototypical Networks For Few Shot Learning</summary>
<br>
<!-- (prototypical_networks_for_few_shot_learning.md) -->

# prototypical_networks_for_few_shot_learning.md

<!-- REFERENCE -->


[Prototypical Networks For Few Shot Learning](../papers/prototypical_networks_for_few_shot_learning.md)

</details>



<details>
<summary>[28] Neural Architecture Search With Reinforcement Learning</summary>
<br>
<!-- (neural_architecture_search_with_reinforcement_learning.md) -->

# neural_architecture_search_with_reinforcement_learning.md

<!-- REFERENCE -->


[Neural Architecture Search With Reinforcement Learning](../papers/neural_architecture_search_with_reinforcement_learning.md)

</details>



<details>
<summary>[234] Learning Transferable Architectures For Scalable Image Recognition</summary>
<br>
<!-- (learning_transferable_architectures_for_scalable_image_recognition.md) -->

# learning_transferable_architectures_for_scalable_image_recognition.md

<!-- REFERENCE -->


[Learning Transferable Architectures For Scalable Image Recognition](../papers/learning_transferable_architectures_for_scalable_image_recognition.md)

</details>



<details>
<summary>[124] SNAS: Stochastic Neural Architecture Search</summary>
<br>
<!-- (snas_stochastic_neural_architecture_search.md) -->

# snas_stochastic_neural_architecture_search.md

<!-- REFERENCE -->


[SNAS: Stochastic Neural Architecture Search](../papers/snas_stochastic_neural_architecture_search.md)

</details>



<details>
<summary>[87] Learning To Compare: Relation Network For FewShot Learning</summary>
<br>
<!-- (learning_to_compare_relation_network_for_fewshot_learning.md) -->

# learning_to_compare_relation_network_for_fewshot_learning.md

<!-- REFERENCE -->


[Learning To Compare: Relation Network For FewShot Learning](../papers/learning_to_compare_relation_network_for_fewshot_learning.md)

</details>



<details>
<summary>[126] Meta Architecture Search</summary>
<br>
<!-- (meta_architecture_search.md) -->

# meta_architecture_search.md

<!-- REFERENCE -->


[Meta Architecture Search](../papers/meta_architecture_search.md)

</details>



<details>
<summary>[39] Neural Architecture Search: A Survey</summary>
<br>
<!-- (neural_architecture_search_a_survey.md) -->

# neural_architecture_search_a_survey.md

<!-- REFERENCE -->


[Neural Architecture Search: A Survey](../papers/neural_architecture_search_a_survey.md)

</details>



<details>
<summary>[7] AI Benchmark: All About Deep Learning On Smartphones In 2019</summary>
<br>
<!-- (ai_benchmark_all_about_deep_learning_on_smartphones_in_2019.md) -->

# ai_benchmark_all_about_deep_learning_on_smartphones_in_2019.md

<!-- REFERENCE -->


[AI Benchmark: All About Deep Learning On Smartphones In 2019](../papers/ai_benchmark_all_about_deep_learning_on_smartphones_in_2019.md)

</details>



<details>
<summary>[151] Searching For Activation Functions</summary>
<br>
<!-- (searching_for_activation_functions.md) -->

# searching_for_activation_functions.md

<!-- REFERENCE -->


[Searching For Activation Functions](../papers/searching_for_activation_functions.md)

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
<summary>[238] Auto-Meta: Automated Gradient Based Meta Learner Search</summary>
<br>
<!-- (auto_meta_automated_gradient_based_meta_learner_search.md) -->

# auto_meta_automated_gradient_based_meta_learner_search.md

<!-- REFERENCE -->


[Auto-Meta: Automated Gradient Based Meta Learner Search](../papers/auto_meta_automated_gradient_based_meta_learner_search.md)

</details>



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
<summary>[123] Designing Neural Networks Through Neuroevolution</summary>
<br>
<!-- (designing_neural_networks_through_neuroevolution.md) -->

# designing_neural_networks_through_neuroevolution.md

<!-- REFERENCE -->


[Designing Neural Networks Through Neuroevolution](../papers/designing_neural_networks_through_neuroevolution.md)

</details>



<details>
<summary>[236] Searching For Mobilenetv3</summary>
<br>
<!-- (searching_for_mobilenetv3.md) -->

# searching_for_mobilenetv3.md

<!-- REFERENCE -->


[Searching For Mobilenetv3](../papers/searching_for_mobilenetv3.md)

</details>



<details>
<summary>[241] NAS-Bench-101: Towards Reproducible Neural Architecture Search</summary>
<br>
<!-- (nas_bench_101_towards_reproducible_neural_architecture_search.md) -->

# nas_bench_101_towards_reproducible_neural_architecture_search.md

<!-- REFERENCE -->


[NAS-Bench-101: Towards Reproducible Neural Architecture Search](../papers/nas_bench_101_towards_reproducible_neural_architecture_search.md)

</details>



<details>
<summary>[237] Mnasnet: Platform-aware Neural Architecture Search For Mobile</summary>
<br>
<!-- (mnasnet_platform_aware_neural_architecture_search_for_mobile.md) -->

# mnasnet_platform_aware_neural_architecture_search_for_mobile.md

<!-- REFERENCE -->


[Mnasnet: Platform-aware Neural Architecture Search For Mobile](../papers/mnasnet_platform_aware_neural_architecture_search_for_mobile.md)

</details>

