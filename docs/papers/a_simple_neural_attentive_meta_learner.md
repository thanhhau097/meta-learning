# a_simple_neural_attentive_meta_learner.md
## What?
- A meta-learner architecture that use a novel combination of temporal convolutions and soft attention; the former to aggregate information from past experience and the latter to pinpoint specific pieces of information.
## Why?
- Handle the problems: architectures specialized to a particular application, or hard-coding algorithmic components that constrain how the meta-learner solves the task
## How?
![alt text](../images/snail.png)
![alt text](../images/snail_dense.png)
![alt text](../images/snail_tc_attention.png)
## Results? (What did they find?)
- Effective black-box using self attention 
- Note:
    - trained the SNAIL on episodes where the number of shots K was chosen uniformly at random from 1 to 5 (note that this is unlike prior works, who train separate models for each shot)
    - complicated architecture, not sure that can compare with original MAML
## Ideas to improve?

<!-- REFERENCE -->
