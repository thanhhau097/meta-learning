# hierarchical_bayesian_models
Hierarchical Bayesian Models (HBM) involve Bayesian learning of parameters θ under a prior p(θ|ω). 
The prior is written as a conditional density on some other variable ω which has its own prior p(ω). 
Hierarchical Bayesian models feature strongly as models for grouped data <img src="https://render.githubusercontent.com/render/math?math=\mathcal{D} = {\mathcal{D}_i|i = 1, 2, . . . ,M}">, where each group i has its own θi. The full model is
<img src="https://render.githubusercontent.com/render/math?math=\left[\prod_{i=1}^{M} p\left(\mathcal{D}_{i} | \theta_{i}\right) p\left(\theta_{i} | \omega\right)\right] p(\omega)">.
The levels of hierarchy can be increased further; in particular ω can itself be parameterized, and hence p(ω) can
 be learnt. Learning is usually full-pipeline, but using some form
of Bayesian marginalisation to compute the posterior over ω: <img src="https://render.githubusercontent.com/render/math?math=\omega: P(\omega | \mathcal{D}) \sim p(\omega) \prod_{i=1}^{M} \int d \theta_{i} p\left(\mathcal{D}_{i} | \theta_{i}\right) p\left(\theta_{i} | \omega\right)">. The ease of
doing the marginalisation depends on the model: in some
?M ?
(e.g. Latent Dirichlet Allocation [55]) the marginalisation is exact due to the choice of conjugate exponential models, in others (see e.g. [71]), a stochastic variational approach is used to calculate an approximate posterior, from which a lower bound to the marginal likelihood is computed.
Bayesian hierarchical models provide a valuable view-
point for meta-learning, in that they provide a modeling rather than an algorithmic framework for understanding the meta-learning process. In practice, prior work in Bayesian hierarchical models has typically focused on learning sim- ple tractable models θ; most meta-learning work however considers complex inner-loop learning processes, involving many iterations. Nonetheless, some meta-learning methods like MAML [19] can be understood through the lens of HBMs [72].
<!-- REFERENCE -->


<details>
<summary>[72] Recasting Gradient-Based Meta-Learning As Hierarchical Bayes</summary>
<br>
<!-- (recasting_gradient_based_meta_learning_as_hierarchical_bayes.md) -->

# recasting_gradient_based_meta_learning_as_hierarchical_bayes.md

<!-- REFERENCE -->


[Recasting Gradient-Based Meta-Learning As Hierarchical Bayes](../papers/recasting_gradient_based_meta_learning_as_hierarchical_bayes.md)

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
<summary>[55] Latent Dirchlet allocation</summary>
<br>
<!-- (latent_dirchlet_allocation.md) -->

# latent_dirchlet_allocation.md

<!-- REFERENCE -->


[Latent Dirchlet allocation](../papers/latent_dirchlet_allocation.md)

</details>



<details>
<summary>[19] Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks</summary>
<br>
<!-- (model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md) -->

# model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md

<!-- REFERENCE -->


[Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks](../papers/model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md)

</details>

