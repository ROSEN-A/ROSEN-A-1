# Active Learning Algorithm: ModAL

ModAL is an active learning framework for Python, built on scikit-learn.
It is flexible and allows the user to replace parts with ease.
It supports multiple types of active learning strategies.
Active learning is a machine learning process.
It is a semi-supervised method of learning, using both labeled and unlabeled data.
The active learning algorithm can query the user to label data with the desired output during the training phase, so that the algorithm can identify what label it can best learn from.
After training on the labeled data, the algorithm can then predict the classification of unlabeled data.

## How to Use

- modAL requires Python version 3.5 or greater, NumPy version 1.13 or greater, SciPy version 0.18 or greater, and scikit-learn version 0.18 or greater.
- Install ModAL using `pip install modAL` in the terminal, or alternatively `pip install git+https://github.com/modal-python/modal.git`.
- The base active learning model is the ActiveLearner class, which the user can create objects of.
- To create an ActiveLearner object, it requires a *scikit-learn estimator object* and an optional *query strategy function*.
- There are also built-in query strategies in modAL.uncertainty, or the user can implement their own
- The user can also use initial training data if it exists.
- After initializing the ActiveLearner object, the user can use `.teach(X,y)` method to augment available training data with a new sample X and new label y, and then adjust the estimator to the augmented training dataset.
- The `.fit(X, y)` method can be used to make the learner fit to newly provided data, and forget the previous data.
- The `.query(x)` method can be used for the algorithm to select the best instances to label. This method calls the *query strategy function* the user specified during the initialization.
- The `.predict(X)` and `.score(X, y)` methods can be used to calculate the mean accuracy score, the same way you would with a *scikit-learn* classifier.
- Citation for ModAL:

```
@article{modAL2018,
    title={mod{AL}: {A} modular active learning framework for {P}ython},
    author={Tivadar Danka and Peter Horvath},
    url={https://github.com/modAL-python/modAL},
    note={available on arXiv at \url{https://arxiv.org/abs/1805.00979}}
}
```

## Advantages and Disadvantages

- The advantage of using ModAL is that it has a wide range of methods provided right away, and that it is open-source and modular.
- The disadvantage of using ModAL is that it does not include any annotation interfaces, and that the user still has to work to host a model and connect it to annotation interfaces.

## Why do we need this tool for the project?

The active learning algorithm ModAL will be used, in conjunction with Blender, to analyze the prototypes of debris inside of water pipelines.
The ModAL will be used to filter out debris found inside the pipes.
The image data for the debris inside of pipelines is unlabelled; thus, it is necessary to develop a method of identifying which kinds of objects are in the images.
Because data scientists using ROSEN will need to classify large amounts of images, it is important that there is an algorithm implemented in the software that has been trained with simulated data beforehand.
The active learning algorithm does not need to be optimized, therefore the ModAL framework is suitable for the purposes of the ROSEN project.
