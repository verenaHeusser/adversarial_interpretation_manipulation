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


2. https://arxiv.org/pdf/1710.10547.pdf  ghorbani
   - interpreter fooling + explanation 
   - We systematically characterize the robustness of interpreta-tions  generated  by  several  widely-used  feature  importanceinterpretation methods
   - In allcases, our experiments show that systematic perturbations canlead to dramatically different interpretations without chang-ing the label.
   - . Our analysis of the ge-ometry of the Hessian matrix gives insight on why robustnessis a general challenge to current interpretation approaches 

   - n  this  pa-per, we introduce the notion of adversarial perturbations toneural network interpretation.
   - show that points near the decision line are especially susceptible to interpretability-based analysis
   - Our goal is to devise efficientand visually imperceptible perturbations that change the in-terpretability of the test input while preserving the predictedlabel.

3. the mythos
   - the term inerpretability has no agreed upon meaning
   - This paper makes a first step towards providing a compre-hensive taxonomy of both the desiderata and methods ininterpretability research  
   - tries to leverage the problem of a lacking commonly accepted or even flawed problem definition 
   - Even  worse,  we  could  imagine  situations,  like  machinelearning for security, where the environment might be ac-tively  adversarial
   - transparency, i.e.,how does the model work?Thesecond  consists  ofpost-hoc  explanations,  i.e.,what  elsecan the model tell me? This division is a useful organi-zationally, but we note that it is not absolute.  For examplepost-hoc analysis techniques attempt to uncover the signif-icance of various of parameters, an aim we group under theheading of transparency

4. saliency based text  https://arxiv.org/pdf/1810.03292.pdf
   - Consequently, methods that fail the proposed tests are inadequate fortasks that are sensitive to either data or model, such as, finding outliers in the data,explaining the relationship between inputs and outputs that the model learned,and debugging the mode 
   -  model parameter randomization test
   - data randomization test


keywords: 
black box explanations, model interpretability, bias detection, ad-versarial attacks


# interpretation methods
One way to understanding the behavior of such classifiers is to build simpler explanation models that are interpretable approximations of these black boxes.
The other way is to calculate feature importances for a given model. 

(1) crafting of adversarial input examples
(2) crafting of adversarial classifiers / mdoels 


It must be noted that interpretability is mostly assumed to be given if the following holds : 
1. a model aiming to explain a more complex model achieves lower complexity and is thereby interpretable.
2. feature attribution is given, i.e. feature importances of single input features

An  interpretation  may  prove  informative  even  withoutshedding  light  on  a  model’s  inner  workings.


# questions: 
- To  quantify  the  perturba-tion size: [ghorbani et al.] -> l2, linf norms --> how much the images have been perturbed (in terms of number of pixels)?



# interpretation methods 
- https://arxiv.org/pdf/1710.10547.pdf 
1. post-hoc interpretations
   1. Feature  importance  interpretation 
      - explains predictions in terms of realtive importance of features of an input test sample
   
      1. Simple Grad: 1st order lin approx of the model to detect the sensitivity of the score to perturbing each of the input dims
      2. Integrated Gradients: 
      3. LRP methods: decompose the score h_i(x_i) backwards through the network  
      4. DeepLift: Improved version of LRP

   2. Sample Importance Interpret
      - which training examples have the biggest effect on the model prediction
      1. 

# comparision of interpretations  -> metrics 

(1) quantitatively
- https://arxiv.org/pdf/1710.10547.pdf
--> comparsion of interpretations befoe and after perturbation. 
   1. Spearmans rank corr
   2. top-k intersection: intersection of the k most important features
- FSR as a general measure of 

(2) qualitatively
- by visual inspection
