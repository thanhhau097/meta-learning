# black_box_model_based

In model-based (or black-box) methods the inner learning step (Eq. 6, Eq. 4) is wrapped up in the feed-forward pass of a single model, as illustrated in Eq. 7. The model embeds the current dataset D into activation state, with predictions for test data being made based on this state. Typical architectures include recurrent networks [41], [51], convolutional networks [40] or hyper- networks [79], [80] that embed training instances and labels of a given task to define a predictor that inputs testing example and predicts its label. In this case all the inner- level learning is contained in the activation states of the model and is entirely feed-forward. Outer-level learning is performed with ω containing the CNN, RNN or hyper- network parameters. The outer and inner-level optimiza- tions are tightly coupled as ω directly specifies θ. Memory- augmented neural networks [81] use an explicit storage buffer and can also be used as a model-based algorithm [82], [83]. It has been observed that model-based approaches are usually less able to generalize to out-of-distribution tasks than optimization-based methods [84]. Furthermore, while they are often very good at data efficient few-shot learning, they have been criticised for being asymptotically weaker
[84] as it isn’t clear that black-box models can successfully embed a large training set into a rich base model.
<!-- REFERENCE -->


<details>
<summary>[41] Optimization As A Model For FewShot Learning</summary>
<br>
<!-- (optimization_as_a_model_for_fewshot_learning.md) -->

# optimization_as_a_model_for_fewshot_learning.md

<!-- REFERENCE -->


[Optimization As A Model For FewShot Learning](../papers/optimization_as_a_model_for_fewshot_learning.md)

</details>



<details>
<summary>[79] Few-Shot Image Recognition By Predicting Parameters From Activations</summary>
<br>
<!-- (few_shot_image_recognition_by_predicting_parameters_from_activations.md) -->

# few_shot_image_recognition_by_predicting_parameters_from_activations.md

<!-- REFERENCE -->


[Few-Shot Image Recognition By Predicting Parameters From Activations](../papers/few_shot_image_recognition_by_predicting_parameters_from_activations.md)

</details>



<details>
<summary>[80] Dynamic Few-Shot Visual Learning Without Forgetting</summary>
<br>
<!-- (dynamic_few_shot_visual_learning_without_forgetting.md) -->

# dynamic_few_shot_visual_learning_without_forgetting.md

<!-- REFERENCE -->


[Dynamic Few-Shot Visual Learning Without Forgetting](../papers/dynamic_few_shot_visual_learning_without_forgetting.md)

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
<summary>[82] Meta Learning With Memory-Augmented Neural Networks</summary>
<br>
<!-- (meta_learning_with_memory_augmented_neural_networks.md) -->

# meta_learning_with_memory_augmented_neural_networks.md

<!-- REFERENCE -->


[Meta Learning With Memory-Augmented Neural Networks](../papers/meta_learning_with_memory_augmented_neural_networks.md)

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
<summary>[51] Learning To Learn Using Gradient Descent</summary>
<br>
<!-- (learning_to_learn_using_gradient_descent.md) -->

# learning_to_learn_using_gradient_descent.md

<!-- REFERENCE -->


[Learning To Learn Using Gradient Descent](../papers/learning_to_learn_using_gradient_descent.md)

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
<summary>[84] Meta-Learning And Universality: Deep Representations And Gradient Descent Can Approximate Any Learning Algorithm</summary>
<br>
<!-- (meta_learning_and_universality_deep_representations_and_gradient_descent_can_approximate_any_learning_algorithm.md) -->

# meta_learning_and_universality_deep_representations_and_gradient_descent_can_approximate_any_learning_algorithm.md

<!-- REFERENCE -->


[Meta-Learning And Universality: Deep Representations And Gradient Descent Can Approximate Any Learning Algorithm](../papers/meta_learning_and_universality_deep_representations_and_gradient_descent_can_approximate_any_learning_algorithm.md)

</details>

