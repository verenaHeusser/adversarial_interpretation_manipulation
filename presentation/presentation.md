---
title: "Why you shouldn't trust me: A survey on Adversarial Model Interpretation Manipulations"
author: "Verena Heusser"
institute: "KIT,  Intelligent System Security Research Group, Seminar Explainable Machine Learning"
topic: "Pandoc how-to"
# theme: "Frankfurt"
# colortheme: "beaver"
fonttheme: "professionalfonts"
# mainfont: "Hack Nerd Font"
fontsize: 10pt
# urlcolor: red
linkstyle: bold
aspectratio: 169
date: \today
lang: en-US
section-titles: true
toc: false
theme: metropolis
<!-- today i will present a survey in the field of explainable ml: On how to fool interpretation methods -->
---

# Motivation

## Omnipresent Machine Learning

- Machine learning algorithms are moving our of the lab into the real world <!-- autonomous driving, apps, internet: ml models have reached super human performance on a number of tasks + more and more tasks are being handled -->
- Performance comes at the cost of complexity
<!-- so instead of having a simple model, more complex modes (in terms of number of parameters) are used as they achieve better results -->

\begin{center}
\includegraphics[width=0.75\textwidth]{../paper/figures/ml_pipelines_multipage-nn_cat_onlyScore.png}
\end{center}

## Omnipresent Machine Learning

- Machine learning algorithms are moving our of the lab into the real world
- Performance comes at the cost of complexity

\begin{center}
\includegraphics[width=0.75\textwidth]{../paper/figures/ml_pipelines_multipage-bb_cat_onlyScore.png}
\end{center}

## Omnipresent Machine Learning

- Machine learning algorithms are moving our of the lab into the real world
- Performance comes at the cost of complexity

<!-- understanding these bb models is hard, even for humans. and mostly, just having a model that preforms well on a held out
test set does not give stakeholders and users enough trust -->

- so far: _what_ is the most likely label
- now also: _why_ does the model choose this label and  
  which features were important for the decision $\rightarrow$ Explainable ML

\begin{center}
\includegraphics[width=0.75\textwidth]{../paper/figures/bb_cat.png}
\end{center}

## Omnipresent Machine Learning

- Machine learning algorithms are moving our of the lab into the real world
- Performance comes at the cost of complexity

<!-- furthermore, as the application areas are also expanded to more critical areas, such as medicine, politics an even personal rights  -->
<!-- the recent discussions an the US on the california 25 cash bail discussions are one example of (as I believe) many more to come -->

- so far: _what_ is the most likely label
- now also: _why_ does the model choose this label and  
   which features were important for the decision $\rightarrow$ Explainable ML

\begin{center}
\includegraphics[width=0.75\textwidth]{../paper/figures/bb_prop25.png}
\end{center}

## Explainable Machine Learning

::: columns

:::: {.column width=60%}

- Goal: Make stakeholders and customers comfortable
- Problem: Tradeoff between complexity and interpretability

::::

 <!--
simple model (e.g. linear) is interpretable, but not so powerful
Deep model is complex, but powerful  ⇒ make interpretable
-->

:::: {.column width=30%}
![](../paper/figures/simple_vs_complex.png "simple_vs_complex"){width=99%}
::::

:::

## Explainable Machine Learning

::: columns

:::: {.column width=60%}

- Goal: Make stakeholders and customers comfortable
- Problem: Tradeoff between complexity and interpretability
- $\rightarrow$ Need for methods helping with uncovering the _why_
::::
 <!--
simple model (e.g. linear) is interpretable, but not so powerful
Deep model is complex, but powerful  ⇒ make interpretable
-->

:::: {.column width=30%}
![](../paper/figures/simple_vs_complex.png "simple_vs_complex"){width=99%}
::::

:::

## Terminology

- _Interpretability_: Observation of cause and effect ~ uncover the _why_
- _Explainability_: Observation of inner workings ~ uncover the _how_

\begin{center}
\includegraphics[width=0.75\textwidth]{../paper/figures/bb_cat.png}
\end{center}

## Terminology

- **_Interpretability_**: Observation of cause and effect ~ uncover the _why_
  - _Post-hoc_ interpretability: interpretations are computed by applying  
    methods that analyze the model after training
- _Explainability_: Observation of inner workings ~ uncover the _how_


\begin{center}
\includegraphics[width=0.75\textwidth]{../paper/figures/bb_cat.png}
\end{center}

# Interpretation Methods

## Types of Interpretation Methods

::: columns

:::: {.column width=50%}
Local Methods

- why you think this image is a cat?

Model agnostic methods

- the model is seen as black box (no access to the parameters, we can only query the model)
- the underlying model is approximated with a surrogate model

::::

:::: {.column width=50%}
Global Methods

- what does a cat look like?

Model transparent methods

- the model is known and the parameters can be accessed

::::

:::

<!-- interpretation methods can be discriminated based on different criteria
the criteria important here are whether local interpretarions are generated or global ones

but more importantly (for this work)
based on the assumptions the methods make about the underlying models
-->

## Methods

# Interpreter Fooling

## Adversarial Setting

- why are interpretations so important and why is model fooling dangerous?

Adversarial Setting:

<!-- ::: columns

:::: {.column width=50%}
Adversarial model fooling
::::

:::: {.column width=50%}
Adversarial interpreter fooling
::::

::: -->

## Implications of Interpreter Fooling

# Methods

now, we want to take a look it specific findings of researchers from the past years
