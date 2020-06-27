# meta_learning_and_universality_deep_representations_and_gradient_descent_can_approximate_any_learning_algorithm.md
## What?
- Prove that MAML could be a an universal function, which can approximate any learning algorithms
## Why?
- Other RNN methods in meta-learning are universal functions. 
- To find out how much MAML can generalize
## How?
- The approximate function of MAML depends on first-order derivative, not normal functions.
- The authors prove the universality of MAML (read in paper)
## Results? (What did they find?)
- There exists a form of deep neural network such that the initial weights combined with gradient descent can approximate any learning algorithm.
- the representations acquired with MAML are highly resilient to overfitting
- But it still depends on type of loss function.
## Ideas to improve?
<!-- REFERENCE -->
