# environment_learning_and_sims2real
In Sim2Real we are interested in training a model in simulation that is able to generalize to the real-world, which is challenging since the simulation does not match the real world exactly. The classic domain randomization approach simulates a wide distribution over domains/MDPs, with the aim of training a sufficiently robust model to succeed in the real world – and has succeeded in both vision [232] and RL [148]. Nevertheless how to tune the simulation distribution is a challenge. This naturally leads to a meta- learning setup where the inner-level optimization learns a model in simulation, the outer-level optimization Lmeta evaluates the model’s performance in the real-world, and the meta-representation ω corresponds to the parameters of the simulation environment. This paradigm has been used in RL [150] as well as computer vision [149], [233]. In this case the source tasks used for meta-train tasks are not a pre- provided data distribution, but paramaterized by omega, 
<img src="https://render.githubusercontent.com/render/math?math=\mathscr{D}_{\text {source}}(\omega)">
. However, challenges remain in terms of back- propagating through a costly and long graph of learning steps of the inner task; as well as minimising the number of real-world 
<img src="https://render.githubusercontent.com/render/math?math=\mathcal{L}^{m e t a}"> 
 evaluations in the case of Sim2Real meta-learning for RL.
<!-- REFERENCE -->


<details>
<summary>[233] Meta-Sim: Learning To Generate Synthetic Datasets</summary>
<br>
<!-- (meta_sim_learning_to_generate_synthetic_datasets.md) -->

# meta_sim_learning_to_generate_synthetic_datasets.md

<!-- REFERENCE -->


[Meta-Sim: Learning To Generate Synthetic Datasets](../papers/meta_sim_learning_to_generate_synthetic_datasets.md)

</details>



<details>
<summary>[150] How To Pick The Domain Randomization Parameters For Sim-to-real Transfer Of Reinforcement Learning Policies</summary>
<br>
<!-- (how_to_pick_the_domain_randomization_parameters_for_sim_to_real_transfer_of_reinforcement_learning_policies.md) -->

# how_to_pick_the_domain_randomization_parameters_for_sim_to_real_transfer_of_reinforcement_learning_policies.md

<!-- REFERENCE -->


[How To Pick The Domain Randomization Parameters For Sim-to-real Transfer Of Reinforcement Learning Policies](../papers/how_to_pick_the_domain_randomization_parameters_for_sim_to_real_transfer_of_reinforcement_learning_policies.md)

</details>



<details>
<summary>[149] Learning To Simulate</summary>
<br>
<!-- (learning_to_simulate.md) -->

# learning_to_simulate.md

<!-- REFERENCE -->


[Learning To Simulate](../papers/learning_to_simulate.md)

</details>



<details>
<summary>[148] Learning Dexterous In-Hand Manipulation</summary>
<br>
<!-- (learning_dexterous_in_hand_manipulation.md) -->

# learning_dexterous_in_hand_manipulation.md

<!-- REFERENCE -->


[Learning Dexterous In-Hand Manipulation](../papers/learning_dexterous_in_hand_manipulation.md)

</details>



<details>
<summary>[232] Training Deep Networks With Synthetic Data: Bridging The Reality Gap By Domain Randomization</summary>
<br>
<!-- (training_deep_networks_with_synthetic_data_bridging_the_reality_gap_by_domain_randomization.md) -->

# training_deep_networks_with_synthetic_data_bridging_the_reality_gap_by_domain_randomization.md

<!-- REFERENCE -->


[Training Deep Networks With Synthetic Data: Bridging The Reality Gap By Domain Randomization](../papers/training_deep_networks_with_synthetic_data_bridging_the_reality_gap_by_domain_randomization.md)

</details>

