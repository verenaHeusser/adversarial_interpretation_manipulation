1. fooling l+s
   1. propose a framework for fooling classifiers 
   2. Our approach can be used to scaffoldany biased classifier in such a way that its predictions on the inputdata distribution still remain biased, but the post hoc explanationsof the scaffolded classifier look innocuous. 
   3. --> fool the interpreter, as interpreter cannot detect biases of model
   4. thus, motivating the need fortools that can explain them in a faithful and interpretable manner.
   5. post-hoc, local explanation methods: Thesemethods estimate the contribution of individual features towards aspecific prediction by generating perturbations of a given instancein the data and observing the effect of these perturbations on theoutput of the black-box classifier.
   6. l+s learn an interpretable model around a black box classifier
   7. indroduce biases into the model by 
   8. show that Lime and shap do not capture any of the important biases employed by the biased classifiers 
   9. These results suggest that it is possible for malicious actorsto craft adversarial classifiers that are highly discriminatory, butcan effectively fool existing post hoc explanation techniques


keywords: 
black box explanations, model interpretability, bias detection, ad-versarial attacks


# interpretation methods
One way to understanding the behavior of such classifiers is to build simpler explanation models that are interpretable approximations of these black boxes.
The other way is to calculate feature importances for a given model. 

(1)  crafting of adversarial input examples
(2) crafting of adversarial classifiers / mdoels 


It must be noted that interpretability is mostly assumed to be given if the following holds : 
1. a model aiming to explain a more complex model achieves lower complexity and is thereby interpretable.
2. feature attribution is given, i.e. feature importances of single input features