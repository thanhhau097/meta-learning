# domain_adaptation_and_domain_generalization
Domain-shift often hampers machine learning models in
practice, when the statistics of data encountered in deploy- ment differ from those used in training. Numerous domain adaptation and generalization algorithms have been studied to address this issue in supervised, unsupervised, and semi- supervised settings [57].

**Domain Generalization**
Domain generalization ap-
proaches aim to train models with increased robustness to train-test domain shift by design [255], often by exploiting a distribution over training domains. Meta-learning can be an effective tool to support this goal by defining the outer- loop validation set to have a domain shift with respect to the inner loop train set [58]. In this way different kinds of meta-knowledge such as regularizers [92], losses [44], and noise augmentation [173] can be (meta) learned so as to maximize the typical robustness of the learned model to train-test domain-shift.

**Domain Adaptation** While the extensive prior work on domain adaptation has been conventional learning [57], re- cent work [256] has begun to consider meta-learning ap- proaches to boosting domain adaptation as well.

**Benchmarks** Popular benchmarks for DA and DG are oriented around recognition of different image types such as photo/sketch/cartoon. Datasets with multiple domains are often used in order to provide a domain distribution for meta-learning. PACS [257] provides a good starter bench- mark with Visual Decathlon [44], [206], DomainNet [258] and Meta-Dataset [207] providing larger scale alternatives.
<!-- REFERENCE -->
