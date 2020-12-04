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

- 

# todo + qus
- only large scale models ?
- how do attacks affect small models? scale with model size?
- is there a universal fooling scheme?\\
- reconstruction methods: can foolings be detected?\\
