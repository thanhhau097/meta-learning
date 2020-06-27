# architectures
Architecture discovery has always been an important area in neural networks [39], [123], and one that is not amenable to simple exhaustive search. Meta-Learning can be used to automate this very expensive process by learning architectures. Early attempts use RL and LSTMs to learn to generate a description for a good architecture [28]. Evolutionary Algorithms [27] were also used in an attempt to learn blocks within architectures modelled as graphs which could mutate by editing their graph. Gradient-based architecture representations have also been visited in the form of DARTS [26] where the forward pass during training consists in a softmax across the outputs of all possible layers in a given block, which are weighted by coefficients to be meta learned (i.e. ω). During meta-test, the architecture is discretized by only keeping the layers corresponding to the highest coefficients. The coefficients are learned greedily by alternating a single inner step and a single outer step to update architecture coefficients and network weights. Since DARTS is still relatively slow and of limited accuracy, recent efforts have focused on making architecture learning more efficient through better differentiable approximations [124], learning easy to adapt initializations [125], or architecture priors [126]. More details on neural architecture search can be found in Section 5.4.
<!-- REFERENCE -->


<details>
<summary>[125] Towards Fast Adaptation Of Neural Architectures With Meta Learning</summary>
<br>
<!-- (towards_fast_adaptation_of_neural_architectures_with_meta_learning.md) -->

# towards_fast_adaptation_of_neural_architectures_with_meta_learning.md

<!-- REFERENCE -->


[Towards Fast Adaptation Of Neural Architectures With Meta Learning](../papers/towards_fast_adaptation_of_neural_architectures_with_meta_learning.md)

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
<summary>[26] DARTS: Differentiable Architecture Search</summary>
<br>
<!-- (darts_differentiable_architecture_search.md) -->

# darts_differentiable_architecture_search.md

<!-- REFERENCE -->


[DARTS: Differentiable Architecture Search](../papers/darts_differentiable_architecture_search.md)

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
<summary>[123] Designing Neural Networks Through Neuroevolution</summary>
<br>
<!-- (designing_neural_networks_through_neuroevolution.md) -->

# designing_neural_networks_through_neuroevolution.md

<!-- REFERENCE -->


[Designing Neural Networks Through Neuroevolution](../papers/designing_neural_networks_through_neuroevolution.md)

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
<summary>[27] Regularized Evolution For Image Classifier Architecture Search</summary>
<br>
<!-- (regularized_evolution_for_image_classifier_architecture_search.md) -->

# regularized_evolution_for_image_classifier_architecture_search.md

<!-- REFERENCE -->


[Regularized Evolution For Image Classifier Architecture Search](../papers/regularized_evolution_for_image_classifier_architecture_search.md)

</details>



<details>
<summary>[126] Meta Architecture Search</summary>
<br>
<!-- (meta_architecture_search.md) -->

# meta_architecture_search.md

<!-- REFERENCE -->


[Meta Architecture Search](../papers/meta_architecture_search.md)

</details>

