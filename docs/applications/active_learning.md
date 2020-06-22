# active_learning
The meta-learning paradigm can also be used to train active learning, rather than supervised or reinforcement learners as discussed so far. Active learning (AL) methods wrap supervised learning, and define a policy for selective data annotation – typically in the setting where annotation can be obtained sequentially. The goal of AL is to find the optimal subset of data to annotate so as to maximize perfor- mance of downstream supervised learning with the fewest annotations. AL is a well studied problem with numerous
hand designed algorithms [252]. Meta-learning can trans- form active learning algorithm design into a learning task by: considering the inner-level optimization as a conven- tional supervised learning task on the annotated dataset so far, considering ω to be a query policy that selects the best unlabeled datapoints to annotate, or by letting the outer-level optimization train the query policy to optimize a meta-objective corresponding to downstream learning performance given the queried and annotated datapoints [175]–[177]. However, as for clustering, if labels are used to train AL algorithms, they need to generalize across tasks to amortise their training cost [177].
<!-- REFERENCE -->


<details>
<summary>[175] Learning Algorithms For Active Learning</summary>
<br>
<!-- (learning_algorithms_for_active_learning.md) -->

# learning_algorithms_for_active_learning.md

<!-- REFERENCE -->


[Learning Algorithms For Active Learning](../papers/learning_algorithms_for_active_learning.md)

</details>



<details>
<summary>[252] Active Learning</summary>
<br>
<!-- (active_learning.md) -->

# active_learning.md

<!-- REFERENCE -->


[Active Learning](../papers/active_learning.md)

</details>



<details>
<summary>[177] Meta-Learning Transferable Active Learning Policies By Deep Reinforcement Learning</summary>
<br>
<!-- (meta_learning_transferable_active_learning_policies_by_deep_reinforcement_learning.md) -->

# meta_learning_transferable_active_learning_policies_by_deep_reinforcement_learning.md

<!-- REFERENCE -->


[Meta-Learning Transferable Active Learning Policies By Deep Reinforcement Learning](../papers/meta_learning_transferable_active_learning_policies_by_deep_reinforcement_learning.md)

</details>

