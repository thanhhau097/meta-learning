# domain_adaption_and_domain_generalization
Domain-shift refers to the situation where source and
target tasks have the same classes but the input distribution of the target task is shifted with respect to the source task [34], [57], leading to reduced model performance upon transfer. DA is a variant of transfer learning that attempts to alleviate this issue by adapting the source-trained model using sparse or unlabeled data from the target. DG refers to methods to train a source model to be robust to such domain-shift without further adaptation. Many methods have been studied [34], [57], [58] to transfer knowledge and boost performance in the target domain. However, as for TL, vanilla DA and DG are differentiated in that there is no meta-objective that optimizes ‘how to learn’ across domains. Meanwhile, meta-learning methods can be used to perform both DA and DG, which we cover in section 5.9.

<!-- REFERENCE -->


<details>
<summary>[57] [57] G. Csurka, Domain Adaptation In Computer Vision Applications. Springer, 201</summary>
<br>
<!-- (domain_adaptation_in_computer_vision_applications.md) -->

# domain_adaptation_in_computer_vision_applications.md

<!-- REFERENCE -->


[[57] G. Csurka, Domain Adaptation In Computer Vision Applications. Springer, 201](../papers/domain_adaptation_in_computer_vision_applications.md)

</details>



<details>
<summary>[34] A Survey On Transfer Learning</summary>
<br>
<!-- (a_survey_on_transfer_learning.md) -->

# a_survey_on_transfer_learning.md
## What?
- Categorizing and reviewing the progress on transfer learning
## Why?
- Survey
## How?
![alt text](../images/transfer_learning.png)

## Results? (What did they find?)

## Ideas to improve?
<!-- REFERENCE -->


[A Survey On Transfer Learning](../papers/a_survey_on_transfer_learning.md)

</details>



<details>
<summary>[58] Learning To Generalize: Meta-Learning For Domain Generalization</summary>
<br>
<!-- (learning_to_generalize_meta_learning_for_domain_generalization.md) -->

# learning_to_generalize_meta_learning_for_domain_generalization.md
## What?
Apply meta learning method (MAML) for Domain Generalization problem
## Why?
- Reduce number of parameters and does not require training with high computation cost as previous methods:
    - The simplest approach is to train a model for each source domain. When a testing do-built on three main strategies. The simplest approach is to train a model for each source domain. When a testing do- main comes, estimate the most relevant source domain and train a model for each source domain. When a testing do- main comes, estimate the most relevant source domain and use that classifier (Xu et al. 2014). A second approach is main comes, estimate the most relevant source domain and use that classifier (Xu et al. 2014). A second approach is to presume that any
    - A second approach is to presume that any domain is composed of an underlying globally shared factor and a domain specific component. By factoring out the domain specific and domain-agnostic component during training on source domains, the domain- agnostic component can be extracted and transferred as a model that is likely to work on a new source domain
    
## How?
- Apply MAML directly to Domain Generalization
![alt text](../images/mldg.png)
## Results? (What did they find?)
- Achieve better results compare to previous methods
- Model-agnostic
- Can be applied both supervised learning and reinforcement learning
- Scale well with number of domains

## Ideas to improve?
- Try to apply another variations of MAML to the Domain Generalization problem.
<!-- REFERENCE -->


[Learning To Generalize: Meta-Learning For Domain Generalization](../papers/learning_to_generalize_meta_learning_for_domain_generalization.md)

</details>

