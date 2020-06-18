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
<details>
<summary>[19] Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks</summary>
<br>
<!-- (../papers/model-agnostic_meta-learning_for_fast_adaptation_of_deep_networks.md) -->
<div>

</div>
</details>


<details>
<summary>[95] Probabilistic Model-agnostic Meta-learning</summary>
<br>
<!-- (../papers/probabilistic_model_agnostic_meta_learning.md) -->
<div>

</div>
</details>


<details>
<summary>[96] Online Meta-learning</summary>
<br>
<!-- (../papers/online_metalearning.md) -->
<div>

</div>
</details>


<details>
<summary>[74] Gradient-Based Meta-Learning With Learned Layerwise Metric And Subspace</summary>
<br>
<!-- (../papers/gradient_based_meta_learning_with_learned_layerwise_metric_and_subspace.md) -->
<div>

</div>
</details>


[](../papers/gradient_based_meta_learning_with_learned_layerwise_metric_and_subspace.md)