- trying to explain the black box nature of neural networks

- application of attacks and eval: eval wrt to

  - interpreter performance / output : if change, the interpreter is vulnerable
  - classification result: if change, the model is vulnerable

- Unterscheidung v manipulations:
  1. level:
     - input data
     - model params / representation space
  2. type:
     - structured (vllt auch gelernt, da loss fkt angepasst wird?)
     - random (random, small perturbation)
- Untershidung von explanation methods

  1. post-hoc: used a posteriori to explain how bb ml models produce their outcomes
     - eg counterfactuals (https://arxiv.org/abs/2009.01884)
  2.

- measure effect of attack:
  - is interpreter performance the same? -> interpreter has bees fooled
  - is model acc / output still the same -> mdoel has been fooled
- counterackt attacks + detect attacks

# wtf

- feature attributions

# prps

- nips 2020: https://proceedings.neurips.cc/paper/2020/file/9d94c8981a48d12adfeecfe1ae6e0ec1-Paper.pdf

  - code: https://github.com/zifanw/smoothed_geometry
  - smoothnessof the model’s decision surfaceis related to the transferability of attacks across multiple attribution methods
  - ==> find that smooth geometry plays a role in the robustness to attacks on large-scale models
  - counteract:
    - inexpensive regularization method
    - stochastic smoothing technique that does not require re-training

- acm 2020: https://dl.acm.org/doi/pdf/10.1145/3387514.3405859?casa_token=lCc16GOTZsEAAAAA:gypLNU1o2Wwl3wt_b8stRbb0mgxEomX8PWprPeciNdkhVften3-5E01RM50e0W9NGQaGd4TrLOhA
  - interpretability framework metis
  -
- safeai@aaai 2020 http://lcfi.ac.uk/media/uploads/files/DimanovBhattJamnikWeller_YouShouldntTrustMe.pdf
  - Here we show a straightforward method for mod-ifying a pre-trained model to manipulate the output of manypopular feature importance explanation methods with littlechange in accuracy, thus demonstrating the danger of trust-ing such explanation methods to evaluate the trustworthines

# todo + qus

- only large scale models ?
- how do attacks affect small models? scale with model size?
- is there a universal fooling scheme?\\
- reconstruction methods: can foolings be detected?\\
- model explanations are not only used to make models more interpretable, but also to make them more trustworthy. Another topic comes into play if applying the models in the real world: Fairness, which is the unbiasednes of models toward features like skin tone or gender.
