# Why you shouldn’t trust me: A survey on Adversarial Model Interpretation Manipulations

This repository contains the code of my seminar article 'Why you shouldn’t trust me: A survey on Adversarial ModelInterpretation Manipulations'.
For this article, I have investigated diverse methods from Explainable / Interpretable AI and have played with the code of some of the open source implementations of both
interpretation methods as well as methods aiming at fooling these interpreters.

## Abstract

The accuracy of machine learning models is no longer enough: we also want the often inherently complex models to be safe, robust, and interpretable by humans. As machine learning models enter critical areas in human lives such as the criminal justice system, medicine or financial systems, the inability for humans to understand these models is dangerous and problematic. Progress in the emerging research field of explainable artificial intelligence promises to be a remedy, where interpretation methods try to uncover _how_ models work. However, while the number of studies using these methods is exploding, there are also a growing number of articles pointing out that the interpretation methods are still fundamentally flawed.  
This work provides an overview of the subfield of manipulating interpretable machine learning, with the goal of providing insight into concepts, existing research, and future directions. We want to raise awareness that interpretation methods, just like the underlying machine learning models, can be outwitted by adversaries and that there is often no way to detect adversarial attacks.

## Code

I have worked with the official open source implementations of SHAP and LIME, and have also worked with the code from [1].
All code samples can be found in the subfolder `code/`.

## Data

I have worked with the ImageNet dataset [2].

## References

[1] Heo, J., Joo, S., & Moon, T. (2019). Fooling neural network interpretations via adversarial model manipulation. arXiv preprint arXiv:1902.02041.
Code: https://github.com/rmrisforbidden/Fooling_Neural_Network-Interpretations

[2] Deng, J., Dong, W., Socher, R., Li, L. J., Li, K., & Fei-Fei, L. (2009, June). Imagenet: A large-scale hierarchical image database. In 2009 IEEE conference on computer vision and pattern recognition (pp. 248-255). Ieee.
