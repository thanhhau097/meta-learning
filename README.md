# meta-learning
This repository based on the survey paper: [Meta-Learning in Neural Networks: A Survey](http://arxiv.org/abs/2004.05439)
# Documentations
- [Awesome Meta Learning](https://github.com/sudharsan13296/Awesome-Meta-Learning): A curated list of Meta Learning papers, code, books, blogs, videos, datasets and other resources.
- https://github.com/dragen1860/awesome-meta-learning

# Github
- Dataset and Benchmark: https://github.com/google-research/meta-dataset
- Data Loader and Benchmark: https://github.com/tristandeleu/pytorch-meta
- MAML pytorch: https://github.com/dragen1860/MAML-Pytorch
- MAML Tensorflow (original): https://github.com/cbfinn/maml

# Meta-Representation
Meta-learning methods make different choices about what ω should be, i.e. which aspects of the learning strategy should be learned; and (by exclusion) which aspects should be considered fixed
<details>
<summary>Parameter Initialization</summary>
<br>
<!-- (./docs/meta-representation/parameter-initialization.md) -->
<div>

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




