# meta_reinforcement_learning_and_robotics
Reinforcement learning is typically concerned with learning control policies that enable an agent to obtain high reward in achieving a sequential action task within an environment, in contrast to supervised learning’s focus on accuracy on a given dataset. RL typically suffers from extreme sample inefficiency due to sparse rewards, the need for exploration, and high-variance [215] optimization algorithms. However, applications also often naturally entail task families which meta-learning can exploit – for example locomoting-to or reaching-to different positions [172], navigating within dif- ferent maps/environments [40] or traversing different ter- rains [63], driving different cars [171], competing with dif- ferent competitor agents [61], and dealing with different handicaps such as failures in individual robot limbs [63]. Thus RL provides a fertile application area in which meta- learning on task distributions has had significant successes in improving sample efficiency over standard RL algo- rithms. One can intuitively understand the efficacy of these methods. For instance meta-knowledge of ‘how to stand up’ for a humanoid robot is a transferable skill for all tasks within a family that require locomotion, while meta- knowledge of a maze layout is transferable for all tasks that require navigating within the maze.

**5.2.1 Methods**

Several meta-representations that we have already seen have been explored in RL including learning the initial con- ditions [19], [159], hyperparameters [159], [164], step direc- tions [75] and step sizes [163], which enables gradient-based learning to train a neural policy with fewer environmental interactions; and training fast convolutional [40] or recurrent [22], [106] black-box models to embed the experience of of a given environment thus far and use it to synthesize a feed- forward policy. Recent work has developed improved meta- optimization algorithms [155], [156], [158] for these tasks, and provided theoretical guarantees for Meta RL [216].

**Exploration** A meta-representation that is rather unique to RL is that of the exploration policy. RL is complicated by the fact that the data distribution is not fixed, but varies ac- cording to the agent’s actions. Furthermore sparse rewards may mean that an agent must take many actions before achieving a reward that can be used to guide learning. Thus how to explore and acquire data for learning is a crucial factor in any RL algorithm. Traditionally exploration is based on sampling random actions [90], or hand-crafted exploration heuristics [217]. Several meta-RL studies have instead explicitly treated exploration strategy or curiosity function as meta-knowledge ω; and modeled their acqui- sition as meta-learning problem [24], [170], [171] – leading to significant sample efficiency improvements by ‘learning how to explore’.

**Optimization** It is worth noting that, unlike SL where optimization often leads to good local minima with perfect accuracy on the train set; RL is usually a very difficult optimization problem where the learned policy is far from optimal, even on ‘training set’ episodes. This means that, in contrast to meta-SL, meta-RL methods are more commonly deployed to increase asymptotic training performance [23], [164], [167] as well as sample-efficiency, and can lead to sig- nificantly better solutions overall. Indeed, the meta-objective of most meta-RL frameworks is the net return of the agent over a full training episode, and thus both sample efficient and asymptotically performant learning are rewarded. Op- timization difficulty also means that there has also been relatively more work on learning losses (or rewards) [113], [167], [218] which an RL agent should optimize instead of – or in addition to – the conventional sparse reward objective. Such meta-learned losses may be easier to optimize (denser, smoother) compared to the true target [23], [218]. This also links back to exploration as reward learning and can be considered to instantiate meta-learning approaches to learning intrinsic motivation [168].

**Online MetaRL** We note that a significant fraction of meta-RL studies addressed the online single-task setting, where the meta-knowledge such as loss [113], [167], reward [164], [168], hyperparameters [162], [163], or exploration strategy [169] are trained online together with the base policy while learning a single task. These methods thus do not require task families and provide a direct improvement to their respective base learners.

**On- vs Off-Policy Meta-RL** A major dichotomy in con- ventional RL methodologies is between on-policy and off- policy learning such as PPO [90] vs SAC [219]. Off-policy methods are usually significantly more sample efficient for conventional RL. However, off-policy methods have been harder to extend to meta-RL, leading to the majority of Meta-RL methods being built on on-policy base algorithms, and thus limiting the absolute performance of Meta-RL. A few recent works have begun to design meta-RL gener- alizations of off-policy methods leading to strong results [109], [113], [157], [218]. Notably off-policy learning also improves the efficiency of the meta-train stage [109], which can be very expensive in Meta-RL. It also provides new opportunities to accelerate meta-testing by replay buffer sample from meta-training stage [157].

**Other Trends and Challenges** We finish this section by mentioning other recent trends in meta-RL. [63] is notewor- thy in demonstrating successful meta-RL on a real-world physical robot. Knowledge transfer in robotics often makes sense to study compositionally [220]. E.g., walking, navigat- ing and object pick/place may be subroutines of cleaning up the room for a robot. However, developing meta-learners that support a compositional knowledge that transfers well is an open question, with modular meta-learning [131] being an option. Unsupervised meta-RL variants aim to perform meta-training without manually specified rewards [221], or adapt at meta-testing to a changed environment but without new rewards [222]. Continual adaptation uses meta-learning to provide an agent with the ability to adapt to a sequence of tasks within one meta-test episode [61]–[63], which is con- nected to continual learning. Finally, meta-learning has also been applied to imitation [105] and inverse reinforcement learning [223].

**5.2.2 Benchmarks**

Meta-learning benchmarks for RL should define a family of problems for an agent to solve in order to learn how
to learn, and subsequently evaluate the learner. These can be tasks (reward functions) to achieve, or domains (distinct environments or MDPs). RL benchmarks can be divided according whether they test continuous or discrete control, and actuation from state or observations such as images.

**Discrete Control RL** An early meta-RL benchmark for vision-actuated control is the arcade learning environment (ALE) [224], which defines a set of classic Atari games which can be split into meta-training and meta-testing. The typical protocol here is to evaluate return after a fixed number of timesteps in the meta-test environment. One issue with Atari games is their determinism which means that an open- loop policy is potentially sufficient to solve them, leading to efforts to insert stochasticity [224]. Another challenge is that there is great diversity (wide p(T)) across games, which makes successful meta-training hard and leads to limited benefit from knowledge transfer [224]. Another benchmark [225] is based on splitting Sonic-hedgehog levels into meta- train/meta-test. The task distribution here is narrower and beneficial meta-learning is relatively easier to achieve. Re- cently Cobbe et al. [226] proposed two purpose designed video games for benchmarking Meta-RL. CoinRun game [226] provides 232 procedurally generated levels of varying difficulty and visual appearance. They show that some 10, 000 levels of meta-train experience are required to gener- alize reliably to new levels. CoinRun is primarily designed to test direct generalization rather than fast adaptation, and can be seen as providing a distribution over MDP environments to test generalization rather than over tasks to test adaptation. To better test fast learning in a wider task distribution, ProcGen [226] provides a set of 16 procedurally generated games including CoinRun

**Continuous Control RL** While the use of common bench- marks such as gym [227] has greatly benefited RL research, there has not yet been a consensus on benchmarks for meta- RL, making existing work hard to compare. Most studies of continuous control meta-RL have proposed home-brewed benchmarks that are low dimensional parametric variants of particular tasks such as navigating to various locations or velocities [19], [109], or traversing different terrains [63]. Several multi-MDP benchmarks [228], [229] have recently been proposed but these primarily test generalization across different environmental perturbations rather than new task adaptation of interest in Meta-RL. This situation is set to improve with the release of Meta-World benchmark [230] which provides a suite of 50 continuous control tasks with state-based actuation, varying from simple parametric vari- ants such as lever-pulling and door-opening. This bench- mark should enable more comparable evaluation, and inves- tigation of generalization both within and across task distri- butions of various widths. The meta-world evaluation [230] suggests that existing Meta-RL methods struggle to gener- alize over wide task distributions and meta-train/meta-test shifts, so more work is necessary. Another recent benchmark suitable for Meta-RL is PHYRE [231] which provides a set of 50 vision-based physics task templates which can be solved with simple actions but are likely to require model-based reasoning to address efficiently. These are organised into 2 difficulty tiers, and provide within and cross-template generalization tests.

**Discussion** One complication of vision-actuated meta-RL is unpicking visual generalization and adaptation (as in common with broader computer vision) with fast learning of control strategies more generally. For example CoinRun [226] evaluation showed large benefit from standard vision techniques such as batch norm suggesting that perception is a major bottleneck. A topical issue in Meta-RL is that it is difficult to fit
wide meta-train task distributions with multi-task or meta-
learning models – before even getting to the performance of meta-testing on novel tasks. This may be due to our RL models being too weak and/or benchmarks being too small in terms of number of tasks. Even Meta-World, ProcGen and PHYRE have dozens rather than hundreds of tasks like vision benchmarks such as tieredImageNet. While these lat- est benchmarks are improving, the field would still benefit from still larger benchmarks with controllable generaliza- tion gaps. It would also be beneficial to have benchmarks with greater difficulty such as requiring memory and ab- stract reasoning, to provide opportunities for more abstract strategies to be meta-learned and exploited across tasks.

<!-- REFERENCE -->


<details>
<summary>[221] Unsupervised Curricula For Visual Meta-Reinforcement Learning</summary>
<br>
<!-- (unsupervised_curricula_for_visual_meta_reinforcement_learning.md) -->

# unsupervised_curricula_for_visual_meta_reinforcement_learning.md

<!-- REFERENCE -->


[Unsupervised Curricula For Visual Meta-Reinforcement Learning](../papers/unsupervised_curricula_for_visual_meta_reinforcement_learning.md)

</details>



<details>
<summary>[90] Proximal Policy Optimization Algorithms</summary>
<br>
<!-- (proximal_policy_optimization_algorithms.md) -->

# proximal_policy_optimization_algorithms.md

<!-- REFERENCE -->


[Proximal Policy Optimization Algorithms](../papers/proximal_policy_optimization_algorithms.md)

</details>



<details>
<summary>[215] Simple Statistical Gradient-Following Algorithms For Connectionist Reinforcement Learning</summary>
<br>
<!-- (simple_statistical_gradient_following_algorithms_for_connectionist_reinforcement_learning.md) -->

# simple_statistical_gradient_following_algorithms_for_connectionist_reinforcement_learning.md

<!-- REFERENCE -->


[Simple Statistical Gradient-Following Algorithms For Connectionist Reinforcement Learning](../papers/simple_statistical_gradient_following_algorithms_for_connectionist_reinforcement_learning.md)

</details>



<details>
<summary>[105] One-shot Imitation Learning</summary>
<br>
<!-- (one_shot_imitation_learning.md) -->

# one_shot_imitation_learning.md

<!-- REFERENCE -->


[One-shot Imitation Learning](../papers/one_shot_imitation_learning.md)

</details>



<details>
<summary>[223] SMILe: Scalable Meta Inverse Reinforcement Learning Through ContextConditional Policies</summary>
<br>
<!-- (smile_scalable_meta_inverse_reinforcement_learning_through_contextconditional_policies.md) -->

# smile_scalable_meta_inverse_reinforcement_learning_through_contextconditional_policies.md

<!-- REFERENCE -->


[SMILe: Scalable Meta Inverse Reinforcement Learning Through ContextConditional Policies](../papers/smile_scalable_meta_inverse_reinforcement_learning_through_contextconditional_policies.md)

</details>



<details>
<summary>[225] Gotta Learn Fast: A New Benchmark For Generalization In RL</summary>
<br>
<!-- (gotta_learn_fast_a_new_benchmark_for_generalization_in_rl.md) -->

# gotta_learn_fast_a_new_benchmark_for_generalization_in_rl.md

<!-- REFERENCE -->


[Gotta Learn Fast: A New Benchmark For Generalization In RL](../papers/gotta_learn_fast_a_new_benchmark_for_generalization_in_rl.md)

</details>



<details>
<summary>[158] ES-MAML: Simple Hessian-Free Meta Learning</summary>
<br>
<!-- (es_maml_simple_hessian_free_meta_learning.md) -->

# es_maml_simple_hessian_free_meta_learning.md

<!-- REFERENCE -->


[ES-MAML: Simple Hessian-Free Meta Learning](../papers/es_maml_simple_hessian_free_meta_learning.md)

</details>



<details>
<summary>[24] Meta-Learning Curiosity Algorithms</summary>
<br>
<!-- (meta_learning_curiosity_algorithms.md) -->

# meta_learning_curiosity_algorithms.md

<!-- REFERENCE -->


[Meta-Learning Curiosity Algorithms](../papers/meta_learning_curiosity_algorithms.md)

</details>



<details>
<summary>[159] MetaLearning By The Baldwin Effect</summary>
<br>
<!-- (metalearning_by_the_baldwin_effect.md) -->

# metalearning_by_the_baldwin_effect.md

<!-- REFERENCE -->


[MetaLearning By The Baldwin Effect](../papers/metalearning_by_the_baldwin_effect.md)

</details>



<details>
<summary>[231] Phyre: A New Benchmark For Physical Reasoning</summary>
<br>
<!-- (phyre_a_new_benchmark_for_physical_reasoning.md) -->

# phyre_a_new_benchmark_for_physical_reasoning.md

<!-- REFERENCE -->


[Phyre: A New Benchmark For Physical Reasoning](../papers/phyre_a_new_benchmark_for_physical_reasoning.md)

</details>



<details>
<summary>[164] Humanlevel Performance In 3D Multiplayer Games With Populationbased Reinforcement Learning</summary>
<br>
<!-- (humanlevel_performance_in_3d_multiplayer_games_with_populationbased_reinforcement_learning.md) -->

# humanlevel_performance_in_3d_multiplayer_games_with_populationbased_reinforcement_learning.md

<!-- REFERENCE -->


[Humanlevel Performance In 3D Multiplayer Games With Populationbased Reinforcement Learning](../papers/humanlevel_performance_in_3d_multiplayer_games_with_populationbased_reinforcement_learning.md)

</details>



<details>
<summary>[157] Meta-QLearning</summary>
<br>
<!-- (meta_qlearning.md) -->

# meta_qlearning.md

<!-- REFERENCE -->


[Meta-QLearning](../papers/meta_qlearning.md)

</details>



<details>
<summary>[170] Some Considerations On Learning To Explore Via Meta-Reinforcement Learning</summary>
<br>
<!-- (some_considerations_on_learning_to_explore_via_meta_reinforcement_learning.md) -->

# some_considerations_on_learning_to_explore_via_meta_reinforcement_learning.md

<!-- REFERENCE -->


[Some Considerations On Learning To Explore Via Meta-Reinforcement Learning](../papers/some_considerations_on_learning_to_explore_via_meta_reinforcement_learning.md)

</details>



<details>
<summary>[219] Soft ActorCritic: Off-Policy Maximum Entropy Deep Reinforcement Learning With A Stochastic Actor</summary>
<br>
<!-- (soft_actorcritic_off_policy_maximum_entropy_deep_reinforcement_learning_with_a_stochastic_actor.md) -->

# soft_actorcritic_off_policy_maximum_entropy_deep_reinforcement_learning_with_a_stochastic_actor.md

<!-- REFERENCE -->


[Soft ActorCritic: Off-Policy Maximum Entropy Deep Reinforcement Learning With A Stochastic Actor](../papers/soft_actorcritic_off_policy_maximum_entropy_deep_reinforcement_learning_with_a_stochastic_actor.md)

</details>



<details>
<summary>[61] Continuous Adaptation Via Meta-Learning In Nonstationary And Competitive Environments</summary>
<br>
<!-- (continuous_adaptation_via_meta_learning_in_nonstationary_and_competitive_environments.md) -->

# continuous_adaptation_via_meta_learning_in_nonstationary_and_competitive_environments.md

<!-- REFERENCE -->


[Continuous Adaptation Via Meta-Learning In Nonstationary And Competitive Environments](../papers/continuous_adaptation_via_meta_learning_in_nonstationary_and_competitive_environments.md)

</details>



<details>
<summary>[216] Provably Convergent Policy Gradient Methods For Model-Agnostic MetaReinforcement Learning</summary>
<br>
<!-- (provably_convergent_policy_gradient_methods_for_model_agnostic_metareinforcement_learning.md) -->

# provably_convergent_policy_gradient_methods_for_model_agnostic_metareinforcement_learning.md

<!-- REFERENCE -->


[Provably Convergent Policy Gradient Methods For Model-Agnostic MetaReinforcement Learning](../papers/provably_convergent_policy_gradient_methods_for_model_agnostic_metareinforcement_learning.md)

</details>



<details>
<summary>[167] Discovery Of Useful Questions As Auxiliary Tasks</summary>
<br>
<!-- (discovery_of_useful_questions_as_auxiliary_tasks.md) -->

# discovery_of_useful_questions_as_auxiliary_tasks.md

<!-- REFERENCE -->


[Discovery Of Useful Questions As Auxiliary Tasks](../papers/discovery_of_useful_questions_as_auxiliary_tasks.md)

</details>



<details>
<summary>[171] A Meta-MDP Approach To Exploration For Lifelong Reinforcement Learning</summary>
<br>
<!-- (a_meta_mdp_approach_to_exploration_for_lifelong_reinforcement_learning.md) -->

# a_meta_mdp_approach_to_exploration_for_lifelong_reinforcement_learning.md

<!-- REFERENCE -->


[A Meta-MDP Approach To Exploration For Lifelong Reinforcement Learning](../papers/a_meta_mdp_approach_to_exploration_for_lifelong_reinforcement_learning.md)

</details>



<details>
<summary>[113] Online Meta-Critic Learning For Off-Policy Actor-Critic Methods</summary>
<br>
<!-- (online_meta_critic_learning_for_off_policy_actor_critic_methods.md) -->

# online_meta_critic_learning_for_off_policy_actor_critic_methods.md

<!-- REFERENCE -->


[Online Meta-Critic Learning For Off-Policy Actor-Critic Methods](../papers/online_meta_critic_learning_for_off_policy_actor_critic_methods.md)

</details>



<details>
<summary>[169] Learning To Explore With Meta-Policy Gradient</summary>
<br>
<!-- (learning_to_explore_with_meta_policy_gradient.md) -->

# learning_to_explore_with_meta_policy_gradient.md

<!-- REFERENCE -->


[Learning To Explore With Meta-Policy Gradient](../papers/learning_to_explore_with_meta_policy_gradient.md)

</details>



<details>
<summary>[226] Quantifying Generalization In Reinforcement Learning</summary>
<br>
<!-- (quantifying_generalization_in_reinforcement_learning.md) -->

# quantifying_generalization_in_reinforcement_learning.md

<!-- REFERENCE -->


[Quantifying Generalization In Reinforcement Learning](../papers/quantifying_generalization_in_reinforcement_learning.md)

</details>



<details>
<summary>[156] ProMP: Proximal Meta-Policy Search</summary>
<br>
<!-- (promp_proximal_meta_policy_search.md) -->

# promp_proximal_meta_policy_search.md

<!-- REFERENCE -->


[ProMP: Proximal Meta-Policy Search](../papers/promp_proximal_meta_policy_search.md)

</details>



<details>
<summary>[131] Neu- ´ ral Relational Inference With Fast Modular Meta-learning</summary>
<br>
<!-- (neu_ral_relational_inference_with_fast_modular_meta_learning.md) -->

# neu_ral_relational_inference_with_fast_modular_meta_learning.md

<!-- REFERENCE -->


[Neu- ´ ral Relational Inference With Fast Modular Meta-learning](../papers/neu_ral_relational_inference_with_fast_modular_meta_learning.md)

</details>



<details>
<summary>[23] Evolved Policy Gradients</summary>
<br>
<!-- (evolved_policy_gradients.md) -->

# evolved_policy_gradients.md

<!-- REFERENCE -->


[Evolved Policy Gradients](../papers/evolved_policy_gradients.md)

</details>



<details>
<summary>[168] On Learning Intrinsic Rewards For Policy Gradient Methods</summary>
<br>
<!-- (on_learning_intrinsic_rewards_for_policy_gradient_methods.md) -->

# on_learning_intrinsic_rewards_for_policy_gradient_methods.md

<!-- REFERENCE -->


[On Learning Intrinsic Rewards For Policy Gradient Methods](../papers/on_learning_intrinsic_rewards_for_policy_gradient_methods.md)

</details>



<details>
<summary>[75] Meta-SGD: Learning To Learn Quickly For Few Shot Learning</summary>
<br>
<!-- (meta_sgd_learning_to_learn_quickly_for_few_shot_learning.md) -->

# meta_sgd_learning_to_learn_quickly_for_few_shot_learning.md

<!-- REFERENCE -->


[Meta-SGD: Learning To Learn Quickly For Few Shot Learning](../papers/meta_sgd_learning_to_learn_quickly_for_few_shot_learning.md)

</details>



<details>
<summary>[162] Meta-Gradient Reinforcement Learning</summary>
<br>
<!-- (meta_gradient_reinforcement_learning.md) -->

# meta_gradient_reinforcement_learning.md

<!-- REFERENCE -->


[Meta-Gradient Reinforcement Learning](../papers/meta_gradient_reinforcement_learning.md)

</details>



<details>
<summary>[22] RL2 : Fast Reinforcement Learning Via Slow Reinforcement Learning</summary>
<br>
<!-- (rl2_fast_reinforcement_learning_via_slow_reinforcement_learning.md) -->

# rl2_fast_reinforcement_learning_via_slow_reinforcement_learning.md

<!-- REFERENCE -->


[RL2 : Fast Reinforcement Learning Via Slow Reinforcement Learning](../papers/rl2_fast_reinforcement_learning_via_slow_reinforcement_learning.md)

</details>



<details>
<summary>[229] Investigating Generalisation In Continuous Deep Reinforcement Learning</summary>
<br>
<!-- (investigating_generalisation_in_continuous_deep_reinforcement_learning.md) -->

# investigating_generalisation_in_continuous_deep_reinforcement_learning.md

<!-- REFERENCE -->


[Investigating Generalisation In Continuous Deep Reinforcement Learning](../papers/investigating_generalisation_in_continuous_deep_reinforcement_learning.md)

</details>



<details>
<summary>[222] Norml: No-reward Meta Learning</summary>
<br>
<!-- (norml_no_reward_meta_learning.md) -->

# norml_no_reward_meta_learning.md

<!-- REFERENCE -->


[Norml: No-reward Meta Learning](../papers/norml_no_reward_meta_learning.md)

</details>



<details>
<summary>[224] Revisiting The Arcade Learning Environment: Evaluation Protocols And Open Problems For General Agents</summary>
<br>
<!-- (revisiting_the_arcade_learning_environment_evaluation_protocols_and_open_problems_for_general_agents.md) -->

# revisiting_the_arcade_learning_environment_evaluation_protocols_and_open_problems_for_general_agents.md

<!-- REFERENCE -->


[Revisiting The Arcade Learning Environment: Evaluation Protocols And Open Problems For General Agents](../papers/revisiting_the_arcade_learning_environment_evaluation_protocols_and_open_problems_for_general_agents.md)

</details>



<details>
<summary>[106] Learning To Reinforcement Learn</summary>
<br>
<!-- (learning_to_reinforcement_learn.md) -->

# learning_to_reinforcement_learn.md

<!-- REFERENCE -->


[Learning To Reinforcement Learn](../papers/learning_to_reinforcement_learn.md)

</details>



<details>
<summary>[163] Metatrace Actor-Critic: Online Step-Size Tuning By Meta-gradient Descent For Reinforcement Learning Control</summary>
<br>
<!-- (metatrace_actor_critic_online_step_size_tuning_by_meta_gradient_descent_for_reinforcement_learning_control.md) -->

# metatrace_actor_critic_online_step_size_tuning_by_meta_gradient_descent_for_reinforcement_learning_control.md

<!-- REFERENCE -->


[Metatrace Actor-Critic: Online Step-Size Tuning By Meta-gradient Descent For Reinforcement Learning Control](../papers/metatrace_actor_critic_online_step_size_tuning_by_meta_gradient_descent_for_reinforcement_learning_control.md)

</details>



<details>
<summary>[172] MetaReinforcement Learning Of Structured Exploration Strategies</summary>
<br>
<!-- (metareinforcement_learning_of_structured_exploration_strategies.md) -->

# metareinforcement_learning_of_structured_exploration_strategies.md

<!-- REFERENCE -->


[MetaReinforcement Learning Of Structured Exploration Strategies](../papers/metareinforcement_learning_of_structured_exploration_strategies.md)

</details>



<details>
<summary>[109] Efficient Off-Policy Meta-Reinforcement Learning Via Probabilistic Context Variables</summary>
<br>
<!-- (efficient_off_policy_meta_reinforcement_learning_via_probabilistic_context_variables.md) -->

# efficient_off_policy_meta_reinforcement_learning_via_probabilistic_context_variables.md

<!-- REFERENCE -->


[Efficient Off-Policy Meta-Reinforcement Learning Via Probabilistic Context Variables](../papers/efficient_off_policy_meta_reinforcement_learning_via_probabilistic_context_variables.md)

</details>



<details>
<summary>[220] A Review Of Robot Learning For Manipulation: Challenges, Representations, And Algorithms</summary>
<br>
<!-- (a_review_of_robot_learning_for_manipulation_challenges_representations_and_algorithms.md) -->

# a_review_of_robot_learning_for_manipulation_challenges_representations_and_algorithms.md

<!-- REFERENCE -->


[A Review Of Robot Learning For Manipulation: Challenges, Representations, And Algorithms](../papers/a_review_of_robot_learning_for_manipulation_challenges_representations_and_algorithms.md)

</details>



<details>
<summary>[230] Meta-world: A Benchmark And Evaluation For Multitask And Meta Reinforcement Learning</summary>
<br>
<!-- (meta_world_a_benchmark_and_evaluation_for_multitask_and_meta_reinforcement_learning.md) -->

# meta_world_a_benchmark_and_evaluation_for_multitask_and_meta_reinforcement_learning.md

<!-- REFERENCE -->


[Meta-world: A Benchmark And Evaluation For Multitask And Meta Reinforcement Learning](../papers/meta_world_a_benchmark_and_evaluation_for_multitask_and_meta_reinforcement_learning.md)

</details>



<details>
<summary>[228] Assessing Generalization In Deep Reinforcement Learning</summary>
<br>
<!-- (assessing_generalization_in_deep_reinforcement_learning.md) -->

# assessing_generalization_in_deep_reinforcement_learning.md

<!-- REFERENCE -->


[Assessing Generalization In Deep Reinforcement Learning](../papers/assessing_generalization_in_deep_reinforcement_learning.md)

</details>



<details>
<summary>[63] Learning To Adapt In Dynamic, RealWorld Environments Through Meta-Reinforcement Learning</summary>
<br>
<!-- (learning_to_adapt_in_dynamic_realworld_environments_through_meta_reinforcement_learning.md) -->

# learning_to_adapt_in_dynamic_realworld_environments_through_meta_reinforcement_learning.md

<!-- REFERENCE -->


[Learning To Adapt In Dynamic, RealWorld Environments Through Meta-Reinforcement Learning](../papers/learning_to_adapt_in_dynamic_realworld_environments_through_meta_reinforcement_learning.md)

</details>



<details>
<summary>[19] Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks</summary>
<br>
<!-- (model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md) -->

# model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md

<!-- REFERENCE -->


[Model-Agnostic Meta-learning For Fast Adaptation Of Deep Networks](../papers/model_agnostic_meta_learning_for_fast_adaptation_of_deep_networks.md)

</details>



<details>
<summary>[218] Improving Generalization In Meta Reinforcement Learning Using Learned Objectives</summary>
<br>
<!-- (improving_generalization_in_meta_reinforcement_learning_using_learned_objectives.md) -->

# improving_generalization_in_meta_reinforcement_learning_using_learned_objectives.md

<!-- REFERENCE -->


[Improving Generalization In Meta Reinforcement Learning Using Learned Objectives](../papers/improving_generalization_in_meta_reinforcement_learning_using_learned_objectives.md)

</details>



<details>
<summary>[155] Taming MAML: Efficient Unbiased Meta-reinforcement Learning</summary>
<br>
<!-- (taming_maml_efficient_unbiased_meta_reinforcement_learning.md) -->

# taming_maml_efficient_unbiased_meta_reinforcement_learning.md

<!-- REFERENCE -->


[Taming MAML: Efficient Unbiased Meta-reinforcement Learning](../papers/taming_maml_efficient_unbiased_meta_reinforcement_learning.md)

</details>



<details>
<summary>[217] Policy Search In Continuous Action Domains: An Overview</summary>
<br>
<!-- (policy_search_in_continuous_action_domains_an_overview.md) -->

# policy_search_in_continuous_action_domains_an_overview.md

<!-- REFERENCE -->


[Policy Search In Continuous Action Domains: An Overview](../papers/policy_search_in_continuous_action_domains_an_overview.md)

</details>



<details>
<summary>[40] A Simple Neural Attentive Meta-learner</summary>
<br>
<!-- (a_simple_neural_attentive_meta_learner.md) -->

# a_simple_neural_attentive_meta_learner.md

<!-- REFERENCE -->


[A Simple Neural Attentive Meta-learner](../papers/a_simple_neural_attentive_meta_learner.md)

</details>



<details>
<summary>[227] OpenAI Gym</summary>
<br>
<!-- (openai_gym.md) -->

# openai_gym.md

<!-- REFERENCE -->


[OpenAI Gym](../papers/openai_gym.md)

</details>

