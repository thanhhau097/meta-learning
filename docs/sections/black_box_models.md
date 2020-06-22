# black_box_models

Another family of models trains learners ω that provide a feed-forward mapping directly from the support set to the parameters required to classify test instances, i.e., 
<img src="https://render.githubusercontent.com/render/math?math=\theta=g_{\omega}\left(\mathcal{D}^{\text {train}}\right)">
– rather than relying on gradient [78] (or zero-order [104]) iterative optimization of θ. These correspond to the black-box model-based learning in the conventional taxonomy (Section 3.1). Embedding the sup- port set is commonly achieved by recurrent networks [51], [105], [106] or convolution [40]. These methods have strong connections to Hypernet-
works. Hypernetworks [107], [108] are networks that gen- erate the weights of another neural network conditioned on some embedding – and are often used for compression or multi-task learning. Hypernetworks can also be used to synthesize predictive models by conditioning on an em- bedding of the source (aka. support) dataset [97], [109]. In this case ω is the weight synthesis hypernetwork that produces θ given a support set in a feed-forward pass. Fi- nally, memory-augmented neural networks have the ability to remember old data and assimilate new data quickly, and typically fall in the black-box model category as well. In [82], the authors adapt Neural Turing Machines [81] to the meta-learning setting by changing their memory retrieval mechanism. Meta networks [83] then improve on this model by combining fast weights (predicted per task by a network)
and slow weights (trained with REINFORCE across tasks) to access memory. We note that some methods implement both model-based and initial-condition [97] or optimizer-centric [98] meta-learning in a single framework
<!-- REFERENCE -->


<details>
<summary>[105] One-shot Imitation Learning</summary>
<br>
<!-- (one_shot_imitation_learning.md) -->

# one_shot_imitation_learning.md

<!-- REFERENCE -->


[One-shot Imitation Learning](../papers/one_shot_imitation_learning.md)

</details>



<details>
<summary>[97] Meta-Learning With Latent Embedding Optimization</summary>
<br>
<!-- (meta_learning_with_latent_embedding_optimization.md) -->

# meta_learning_with_latent_embedding_optimization.md

<!-- REFERENCE -->


[Meta-Learning With Latent Embedding Optimization](../papers/meta_learning_with_latent_embedding_optimization.md)

</details>



<details>
<summary>[83] Meta Networks</summary>
<br>
<!-- (meta_networks.md) -->

# meta_networks.md

<!-- REFERENCE -->


[Meta Networks](../papers/meta_networks.md)

</details>



<details>
<summary>[104] Learning To Learn Without Gradient Descent By Gradient Descent</summary>
<br>
<!-- (learning_to_learn_without_gradient_descent_by_gradient_descent.md) -->

# learning_to_learn_without_gradient_descent_by_gradient_descent.md

<!-- REFERENCE -->


[Learning To Learn Without Gradient Descent By Gradient Descent](../papers/learning_to_learn_without_gradient_descent_by_gradient_descent.md)

</details>



<details>
<summary>[82] Meta Learning With Memory-Augmented Neural Networks</summary>
<br>
<!-- (meta_learning_with_memory_augmented_neural_networks.md) -->

# meta_learning_with_memory_augmented_neural_networks.md

<!-- REFERENCE -->


[Meta Learning With Memory-Augmented Neural Networks](../papers/meta_learning_with_memory_augmented_neural_networks.md)

</details>



<details>
<summary>[106] Learning To Reinforcement Learn</summary>
<br>
<!-- (learning_to_reinforcement_learn.md) -->

# learning_to_reinforcement_learn.md

<!-- REFERENCE -->


[Learning To Reinforcement Learn](../papers/learning_to_reinforcement_learn.md)

</details>



<details>
<summary>[81] Neural Turing Machines</summary>
<br>
<!-- (neural_turing_machines.md) -->

# neural_turing_machines.md

<!-- REFERENCE -->


[Neural Turing Machines](../papers/neural_turing_machines.md)

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
<summary>[51] Learning To Learn Using Gradient Descent</summary>
<br>
<!-- (learning_to_learn_using_gradient_descent.md) -->

# learning_to_learn_using_gradient_descent.md

<!-- REFERENCE -->


[Learning To Learn Using Gradient Descent](../papers/learning_to_learn_using_gradient_descent.md)

</details>



<details>
<summary>[107] HyperNetworks</summary>
<br>
<!-- (hypernetworks.md) -->

# hypernetworks.md

<!-- REFERENCE -->


[HyperNetworks](../papers/hypernetworks.md)

</details>



<details>
<summary>[109] Efficient Off-Policy Meta-Reinforcement Learning Via Probabilistic Context Variables</summary>
<br>
<!-- (efficient_off_policy_meta_reinforcement_learning_via_probabilistic_context_variables.md) -->

# efficient_off_policy_meta_reinforcement_learning_via_probabilistic_context_variables.md

<!-- REFERENCE -->


[Efficient Off-Policy Meta-Reinforcement Learning Via Probabilistic Context Variables](../papers/efficient_off_policy_meta_reinforcement_learning_via_probabilistic_context_variables.md)

</details>



<details>
<summary>[108] SMASH: OneShot Model Architecture Search Through Hypernetworks</summary>
<br>
<!-- (smash_oneshot_model_architecture_search_through_hypernetworks.md) -->

# smash_oneshot_model_architecture_search_through_hypernetworks.md

<!-- REFERENCE -->


[SMASH: OneShot Model Architecture Search Through Hypernetworks](../papers/smash_oneshot_model_architecture_search_through_hypernetworks.md)

</details>



<details>
<summary>[40] A Simple Neural Attentive Meta-learner</summary>
<br>
<!-- (a_simple_neural_attentive_meta_learner.md) -->

# a_simple_neural_attentive_meta_learner.md

<!-- REFERENCE -->


[A Simple Neural Attentive Meta-learner](../papers/a_simple_neural_attentive_meta_learner.md)

</details>



<details>
<summary>[78] Learning To Learn By Gradient Descent By Gradient Descent</summary>
<br>
<!-- (learning_to_learn_by_gradient_descent_by_gradient_descent.md) -->

# learning_to_learn_by_gradient_descent_by_gradient_descent.md

<!-- REFERENCE -->


[Learning To Learn By Gradient Descent By Gradient Descent](../papers/learning_to_learn_by_gradient_descent_by_gradient_descent.md)

</details>

