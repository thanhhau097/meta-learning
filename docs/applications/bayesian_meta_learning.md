# bayesian_meta_learning
Bayesian meta-learning approaches formalize meta-learning via Bayesian hierarchical modelling, and use Bayesian infer- ence for learning rather than direct optimization of parame- ters. In the meta-learning context, Bayesian learning is typ- ically intractable, and so different approximation methods can be used. Variational approaches, especially stochastic variational methods, are the most common, but sampling approaches can also be considered. One by-product of Bayesian meta-learning is that it
provides uncertainty measures for the θ parameters, and hence measures of prediction uncertainty. Knowing the uncertainty of learner’s predictions can be vital in safety critical domains such as few-shot medical tasks, and can be used for exploration in Reinforcement Learning and for some active learning methods, where a model can seek information about datapoints with high uncertainty.

Recently a number of authors have explored Bayesian
approaches to meta-learning complex models with com- petitive results. Many of these have utilized deep neural networks as components within the framework, for ex- ample extending variational autoencoders to model task variables explicitly [71]. Neural Processes [166] aim to com- bine the uncertainty quantification of Gaussian Processes with the versatility of neural networks, but they are not shown to work on modern few-shot benchmarks. Deep kernel learning is also an active research area that has been adapted to the meta-learning setting [243], and is often coupled with Gaussian Processes [213]. In [72] gradient based meta-learning is recast into a hierarchical empirical Bayes inference problem (i.e. prior learning), which models uncertainty in task-specific parameters θ. Bayesian MAML [212] improves on this model by using a Bayesian ensemble approach that allows non-Gaussian posteriors over θ, and later work removes the need for costly ensembles [199], [244]. In Probabilistic MAML [95], it is the uncertainty in the metaknowledge ω that is modelled, while a MAP estimate is used for θ. Increasingly, these Bayesian methods are shown to tackle ambiguous tasks, active learning and RL problems. Separate from the above approaches, meta-learning has
also been proposed to aid the Bayesian inference process itself. By way of example, in [245], the authors use a meta- learning framework to adapt a Bayesian sampler to provide efficient adaptive sampling methods.

Benchmarks In Bayesian meta-learning, the point is usu- ally to model the uncertainty in the predictions of our meta- learner, and so performance on standard few-shot classifica- tion benchmarks doesn’t necessarily capture what we care about. For this reason different tasks have been developed in the literature. Bayesian MAML [212] extends the sinusoidal regression task of MAML [19] to make it more challenging. Probabilistic MAML [95] provides a suite of 1D toy exam- ples capable of showing model uncertainty and how this uncertainty can be used in an active learning scenario. It also creates a binary classification task from celebA [246], where the positive class is determined by the presence of two facial attributes, but training images show three attributes, thus introducing ambiguity in which two attributes should be classified on. It is observed that sampling ω can correctly reflect this ambiguity. Active learning toy experiments are also shown in [212] as well as reinforcement learning ap- plications, and ambiguous one-shot image generation tasks are used in [199]. Finally, some researchers propose to look at the accuracy v.s. confidence of the meta-learners (i.e. their calibration) [244].


<!-- REFERENCE -->


<details>
<summary>[244] Amortized Bayesian Meta-Learning</summary>
<br>
<!-- (amortized_bayesian_meta_learning.md) -->

# amortized_bayesian_meta_learning.md

<!-- REFERENCE -->


[Amortized Bayesian Meta-Learning](../papers/amortized_bayesian_meta_learning.md)

</details>



<details>
<summary>[245] Bayesian meta sampling for fast uncertainty adaptation</summary>
<br>
<!-- (bayesian_meta_sampling_for_fast_uncertainty_adaptation.md) -->

# bayesian_meta_sampling_for_fast_uncertainty_adaptation.md

<!-- REFERENCE -->


[Bayesian meta sampling for fast uncertainty adaptation](../papers/bayesian_meta_sampling_for_fast_uncertainty_adaptation.md)

</details>



<details>
<summary>[212] Bayesian Model-Agnostic Meta-Learning</summary>
<br>
<!-- (bayesian_model_agnostic_meta_learning.md) -->

# bayesian_model_agnostic_meta_learning.md

<!-- REFERENCE -->


[Bayesian Model-Agnostic Meta-Learning](../papers/bayesian_model_agnostic_meta_learning.md)

</details>



<details>
<summary>[71] Towards A Neural Statistician</summary>
<br>
<!-- (towards_a_neural_statistician.md) -->

# towards_a_neural_statistician.md

<!-- REFERENCE -->


[Towards A Neural Statistician](../papers/towards_a_neural_statistician.md)

</details>



<details>
<summary>[19] Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks</summary>
<br>
<!-- (model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md) -->

# model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md

<!-- REFERENCE -->


[Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks](../papers/model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md)

</details>



<details>
<summary>[72] Recasting Gradient-Based Meta-Learning As Hierarchical Bayes</summary>
<br>
<!-- (recasting_gradient_based_meta_learning_as_hierarchical_bayes.md) -->

# recasting_gradient_based_meta_learning_as_hierarchical_bayes.md

<!-- REFERENCE -->


[Recasting Gradient-Based Meta-Learning As Hierarchical Bayes](../papers/recasting_gradient_based_meta_learning_as_hierarchical_bayes.md)

</details>



<details>
<summary>[243] Adaptive Deep Kernel Learning</summary>
<br>
<!-- (adaptive_deep_kernel_learning.md) -->

# adaptive_deep_kernel_learning.md

<!-- REFERENCE -->


[Adaptive Deep Kernel Learning](../papers/adaptive_deep_kernel_learning.md)

</details>



<details>
<summary>[166] Conditional Neural Processes</summary>
<br>
<!-- (conditional_neural_processes.md) -->

# conditional_neural_processes.md

<!-- REFERENCE -->


[Conditional Neural Processes](../papers/conditional_neural_processes.md)

</details>



<details>
<summary>[199] Meta-Learning Probabilistic Inference For Prediction</summary>
<br>
<!-- (meta_learning_probabilistic_inference_for_prediction.md) -->

# meta_learning_probabilistic_inference_for_prediction.md

<!-- REFERENCE -->


[Meta-Learning Probabilistic Inference For Prediction](../papers/meta_learning_probabilistic_inference_for_prediction.md)

</details>



<details>
<summary>[246] Deep Learning Face Attributes In The Wild</summary>
<br>
<!-- (deep_learning_face_attributes_in_the_wild.md) -->

# deep_learning_face_attributes_in_the_wild.md

<!-- REFERENCE -->


[Deep Learning Face Attributes In The Wild](../papers/deep_learning_face_attributes_in_the_wild.md)

</details>



<details>
<summary>[213] Deep Kernel Transfer In Gaussian Processes For Few-shot Learning</summary>
<br>
<!-- (deep_kernel_transfer_in_gaussian_processes_for_few_shot_learning.md) -->

# deep_kernel_transfer_in_gaussian_processes_for_few_shot_learning.md

<!-- REFERENCE -->


[Deep Kernel Transfer In Gaussian Processes For Few-shot Learning](../papers/deep_kernel_transfer_in_gaussian_processes_for_few_shot_learning.md)

</details>



<details>
<summary>[95] Probabilistic Model-agnostic Meta-learning</summary>
<br>
<!-- (probabilistic_model_agnostic_meta_learning.md) -->

# probabilistic_model_agnostic_meta_learning.md

<!-- REFERENCE -->


[Probabilistic Model-agnostic Meta-learning](../papers/probabilistic_model_agnostic_meta_learning.md)

</details>

