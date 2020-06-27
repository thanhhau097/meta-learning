# Parameter Initialization 

In this first family of methods <img src="https://render.githubusercontent.com/render/math?math=\omega"> corresponds to 
the initial parameters of a neural network. In MAML [19], [95], [96] these are interpreted as initial conditions of the 
inner optimization. A good initialization is just a few gradient steps away from a solution to any task 
<img src="https://render.githubusercontent.com/render/math?math=\mathcal{T}"> drawn from
<img src="https://render.githubusercontent.com/render/math?math=p(\mathcal{T})">. These approaches are widely used for 
few-shot learning, where target problems can be learned without over-fitting using few examples, given such a carefully 
chosen initial condition. A key challenge with this approach is that the outer optimization needs to solve for as many 
parameters as the inner optimization (potentially hundreds of millions in large CNNs). This leads to a line of work on 
isolating a subset of parameters to meta- learn. For example by subspace [74], [97], by layer [79], [97], [98], or by 
separating out scale and shift [99]. While inner loop initialization is a popular and effective choice of 
meta-representation, a key debate here is whether a single initial condition is sufficient to provide fast learning for
a wide range of potential tasks, or if one is limited to fairly narrow distributions p(T). This has led to variants 
that model mixtures over multiple initial conditions [97], [100], [101].

## Reference

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
<summary>[99] Meta-Transfer Learning For Few-Shot Learning</summary>
<br>
<!-- (meta_transfer_learning_for_few_shot_learning.md) -->

# meta_transfer_learning_for_few_shot_learning.md

<!-- REFERENCE -->


[Meta-Transfer Learning For Few-Shot Learning](../papers/meta_transfer_learning_for_few_shot_learning.md)

</details>



<details>
<summary>[74] Gradient-Based Meta-Learning With Learned Layerwise Metric And Subspace</summary>
<br>
<!-- (gradient_based_meta_learning_with_learned_layerwise_metric_and_subspace.md) -->

# gradient_based_meta_learning_with_learned_layerwise_metric_and_subspace.md
## What?
- MT-net: which enables the meta-learner to learn on each layer’s activation space a subspace that the task-specific learner performs gradient descent on.
## Why?
- reduce the sensitivity to the choice of initial learning rates than previous gradient-based meta-learning methods
## How?
- Basic idea: Separate the parameters to 2 groups: 
    - T: will not be updated in learner, and be shared across task-specific model. 
    - W: will be updated in learner
- Use a mask to determine wich parameters are to be updated.
- By doing this, we can specify that T is use as general knowledge
![alt text](../images/learned_layerwise_metric.png)
## Results? (What did they find?)

## Ideas to improve?
<!-- REFERENCE -->


[Gradient-Based Meta-Learning With Learned Layerwise Metric And Subspace](../papers/gradient_based_meta_learning_with_learned_layerwise_metric_and_subspace.md)

</details>



<details>
<summary>[96] Online Metalearning</summary>
<br>
<!-- (online_metalearning.md) -->

# online_metalearning.md

<!-- REFERENCE -->


[Online Metalearning](../papers/online_metalearning.md)

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
<summary>[100] Multimodal Model-Agnostic Meta-Learning Via Task-Aware Modulation</summary>
<br>
<!-- (multimodal_model_agnostic_meta_learning_via_task_aware_modulation.md) -->

# multimodal_model_agnostic_meta_learning_via_task_aware_modulation.md

<!-- REFERENCE -->


[Multimodal Model-Agnostic Meta-Learning Via Task-Aware Modulation](../papers/multimodal_model_agnostic_meta_learning_via_task_aware_modulation.md)

</details>



<details>
<summary>[101] Hierarchically Structured Meta-learning</summary>
<br>
<!-- (hierarchically_structured_meta_learning.md) -->

# hierarchically_structured_meta_learning.md

<!-- REFERENCE -->


[Hierarchically Structured Meta-learning](../papers/hierarchically_structured_meta_learning.md)

</details>



<details>
<summary>[95] Probabilistic Model-agnostic Meta-learning</summary>
<br>
<!-- (probabilistic_model_agnostic_meta_learning.md) -->

# probabilistic_model_agnostic_meta_learning.md

<!-- REFERENCE -->


[Probabilistic Model-agnostic Meta-learning](../papers/probabilistic_model_agnostic_meta_learning.md)

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
<summary>[79] Few-Shot Image Recognition By Predicting Parameters From Activations</summary>
<br>
<!-- (few_shot_image_recognition_by_predicting_parameters_from_activations.md) -->

# few_shot_image_recognition_by_predicting_parameters_from_activations.md

<!-- REFERENCE -->


[Few-Shot Image Recognition By Predicting Parameters From Activations](../papers/few_shot_image_recognition_by_predicting_parameters_from_activations.md)

</details>

