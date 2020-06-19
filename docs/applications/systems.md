# systems

**Network Compression**
Contemporary CNNs require
large amounts of memory that may be prohibitive on embedded devices. Thus network compression in various forms such as quantization and pruning are topical research areas [277], [278]. Meta-learning is beginning to be applied to this objective as well, such as training gradient generator meta-networks that allow quantized networks to be trained [187], and weight generator meta-networks that allow quan- tized networks to be trained with gradient [279].

**Communications** Deep learning has recently made waves in communications systems. For example by learning cod- ing systems that exceed the best hand designed codes for realistic channels [280]. Insofar as optimal performance is achieved by learning a coding scheme tuned for the char- acteristics of a particular channel, few-shot meta-learning can be used to provide rapid online adaptation of coding to changing channel characteristics [281].

**Learning with Label Noise** is a challenge in contem- porary deep learning when large datasets are collected by web scraping or crowd-sourcing. Again, while there are several algorithms hand-designed for this situation, recent meta-learning methods have addressed label noise by trans- ductive learning sample-wise weighs to down-weight noisy samples [142], or learning an initial condition robust to noisy label training [93].

**Adversarial Attacks and Defenses** Deep Neural Net- works can be easily fooled into misclassifying a data point that should be easily recognizable, by adding a carefully crafted human-invisible perturbation to the data [282]. Nu- merous methods have been published in recent years in- troducing stronger attack and defense methods. Typical defenses are carefully hand-designed architectures or train- ing strategies. Analogous to the case in domain-shift, an under-studied potential application of meta-learning is to train the learning algorithm end-to-end for robustness by defining a meta-loss in terms of performance under adver- sarial attack [94], [283]. New benchmarks for adversarial defenses have recently been proposed [284] where defenses should generalize to unforseen attacks. It will be interesting to see whether future meta-learning approaches can make progress on this benchmark.
<!-- REFERENCE -->
