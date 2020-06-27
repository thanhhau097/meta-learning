# embedding_functions

This category of methods are inspired by metric-learning approaches in con- ventional machine learning, and are therefore categorised as such in the conventional taxonomy (Section 3.1). They are mainly applied to few-shot learning. Here the meta-optimization process learns an embedding network ω that transforms raw inputs into a representation suitable for recognition by simple similarity comparison between query and support instances [20], [79], [86], [110] (e.g., with cosine similarity or euclidean distance). However, metric-learning methods can be seen to be a
special case of the feed-forward black-box models above. This is clearly the case for methods that produce logits based on inner product between the embeddings of support and query images
<img src="https://render.githubusercontent.com/render/math?math=x_{s}"> and 
<img src="https://render.githubusercontent.com/render/math?math=x_{q}"> as
<img src="https://render.githubusercontent.com/render/math?math=x_{s} \text { and } x_{q} \text { as } g_{\omega}^{T}\left(x_{q}\right) g_{\omega}\left(x_{s}\right)">
 [79], [110].
Here the support image generates weights to interpret the query example, making it a special case of a BBM where the ‘hypernetwork’ generates a linear classifier for the query set. Vanilla methods in this family have been further enhanced by making the embedding task-conditional [98], [111] or learning a more elaborate comparison metric [87], [88].
<!-- REFERENCE -->


<details>
<summary>[20] Prototypical Networks For Few Shot Learning</summary>
<br>
<!-- (prototypical_networks_for_few_shot_learning.md) -->

# prototypical_networks_for_few_shot_learning.md

<!-- REFERENCE -->


[Prototypical Networks For Few Shot Learning](../papers/prototypical_networks_for_few_shot_learning.md)

</details>



<details>
<summary>[110] A Closer Look At Few-Shot Classification</summary>
<br>
<!-- (a_closer_look_at_few_shot_classification.md) -->

# a_closer_look_at_few_shot_classification.md

<!-- REFERENCE -->


[A Closer Look At Few-Shot Classification](../papers/a_closer_look_at_few_shot_classification.md)

</details>



<details>
<summary>[86] Matching Networks For One Shot Learning</summary>
<br>
<!-- (matching_networks_for_one_shot_learning.md) -->

# matching_networks_for_one_shot_learning.md

<!-- REFERENCE -->


[Matching Networks For One Shot Learning](../papers/matching_networks_for_one_shot_learning.md)

</details>



<details>
<summary>[87] Learning To Compare: Relation Network For FewShot Learning</summary>
<br>
<!-- (learning_to_compare_relation_network_for_fewshot_learning.md) -->

# learning_to_compare_relation_network_for_fewshot_learning.md

<!-- REFERENCE -->


[Learning To Compare: Relation Network For FewShot Learning](../papers/learning_to_compare_relation_network_for_fewshot_learning.md)

</details>



<details>
<summary>[111] TADAM: Task ´ Dependent Adaptive Metric For Improved Few-shot Learning</summary>
<br>
<!-- (tadam_task_dependent_adaptive_metric_for_improved_few_shot_learning.md) -->

# tadam_task_dependent_adaptive_metric_for_improved_few_shot_learning.md

<!-- REFERENCE -->


[TADAM: Task ´ Dependent Adaptive Metric For Improved Few-shot Learning](../papers/tadam_task_dependent_adaptive_metric_for_improved_few_shot_learning.md)

</details>



<details>
<summary>[88] Few-Shot Learning With Graph Neural Networks</summary>
<br>
<!-- (few_shot_learning_with_graph_neural_networks.md) -->

# few_shot_learning_with_graph_neural_networks.md

<!-- REFERENCE -->


[Few-Shot Learning With Graph Neural Networks](../papers/few_shot_learning_with_graph_neural_networks.md)

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

