# environment_learning_and_sims2real
In Sim2Real we are interested in training a model in simulation that is able to generalize to the real-world, which is challenging since the simulation does not match the real world exactly. The classic domain randomization approach simulates a wide distribution over domains/MDPs, with the aim of training a sufficiently robust model to succeed in the real world – and has succeeded in both vision [232] and RL [148]. Nevertheless how to tune the simulation distribution is a challenge. This naturally leads to a meta- learning setup where the inner-level optimization learns a model in simulation, the outer-level optimization Lmeta evaluates the model’s performance in the real-world, and the meta-representation ω corresponds to the parameters of the simulation environment. This paradigm has been used in RL [150] as well as computer vision [149], [233]. In this case the source tasks used for meta-train tasks are not a pre- provided data distribution, but paramaterized by omega, 
<img src="https://render.githubusercontent.com/render/math?math=\mathscr{D}_{\text {source}}(\omega)">
. However, challenges remain in terms of back- propagating through a costly and long graph of learning steps of the inner task; as well as minimising the number of real-world 
<img src="https://render.githubusercontent.com/render/math?math=\mathcal{L}^{m e t a}"> 
 evaluations in the case of Sim2Real meta-learning for RL.
<!-- REFERENCE -->

