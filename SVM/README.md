# Support Vector Machine

## What is SVM?
- Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection. 

- The objective of the support vector machine algorithm is to find a hyperplane in an N-dimensional space(N — the number of features) that distinctly classifies the data points.

### Advantages of SVM
- Effective in high dimensional spaces.

- Still effective in cases where number of dimensions is greater than the number of samples.

- Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

## Hyperplane
- A hyperplane is a decision boundary that differentiates the two classes in SVM. A data point falling on either side of the hyperplane can be attributed to different classes. 

- The dimension of the hyperplane depends on the number of input features in the dataset. If we have 2 input features the hyper-plane will be a line. likewise, if the number of features is 3, it will become a two-dimensional plane.

## Support vector
- Support vectors are the data points that are nearest to the hyper-plane and affect the position and orientation of the hyper-plane. 

- We have to select a hyperplane, for which the margin, i.e the distance between support vectors and hyper-plane is maximum. Even a little interference in the position of these support vectors can change the hyper-plane.

## How SVM works?
There are few rules that can help us to identify the best solution.

### Maximum classification
- The selected line must be able to successfully segregate all the data points into the respective classes.

### Best Separation
- We must choose a line such that it is perfectly able to separate the points.

# Faiss
- Faiss is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning.

- Faiss is written in C++ with complete wrappers for Python. Some of the most useful algorithms are implemented on the GPU.

## What is similarity search?
- Given a set of vectors *x*<sub>i</sub> in dimension *d*, Faiss build a data structure in RAM from it. After the structure is constructed, when given a new vector *x* in dimension *d* it performs efficiently the operation:

> *j* = *argmin*<sub>i</sub>||*x*-*x*<sub>i</sub>||

- where ||•|| is the Euclidean distance (L<sup>2</sup>).

- In Faiss terms, the data structure is an *index*, an object that has an add method to add *x*<sub>i</sub> vectors. Note that the *x*<sub>i</sub>’s are assumed to be fixed.

- Computing the argmin is the *search* operation on the index.

- This is all what Faiss is about. It can also: return not just the nearest neighbor, but also the 2nd nearest, 3rd, …, k-th nearest neighbor search several vectors at a time rather than one (batch processing). 

- For many index types, this is faster than searching one vector after another trade precision for speed, ie. give an incorrect result 10% of the time with a method that’s 10x faster or uses 10x less memory perform maximum inner product search *argmax*<sub>i</sub><x, x<sub>i</sub>> instead of minimum Euclidean search. There is also limited support for other distances (L1, Linf, etc.).

- Return all elements that are within a given radius of the query point (range search)store the index on disk rather than in RAM.

## Install 
- The recommended way to install Faiss is through Conda:

> `$ conda install -c pytorch faiss-cpu`

- The `faiss-gpu` package povides CUDA-enabled indices: 

> `$ conda install -c pytorch faiss-gpu`

- Note that either package should be installed, but not both, as the latter is a superset of the former.





