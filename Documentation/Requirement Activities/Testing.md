# System Testing



## Unit Testing Methodologies

For our project we will be using PyUnit for unit testing as Python will be mainly used in the backend, including the active learning algorithm. PyUnit testing includes various functions such as setUp() and tearDown(), which will be used to define the prerequisite and cleanup steps respectively.

We will also be defining many other test cases. Examples of tests for our project are as follows:


- Check if  a minimum of 60% of all objects in the water pipeline video footage are detected
- Check if VGG-16 converts the sample image to a vector of 4096 dimensions
- Check if timestamp matches the correct video frame
- Check if ALA accepts labeled images as input
- Check if ALA Queries add 10 new images that have not been queried before


One possible way of  structuring the unit tests is with an AAA approach - Arrange, Act. and Assert. First, we would arrange the setup and initialization of the test. Then, we would perform the action of the test. Lastly, we would assert that the test has the expected outcome.


## Quality Assurance in Accordance with Tech Stack

In order to ensure we are meeting quality standards, we will need to frequently evaluate the software system whether it meets the specified requirements or not. A variety of tests will be performed to ensure our software runs as intended. We intend to make our unit tests readable, repeatable, isolated, and deterministic.

We will practice regression testing to ensure existing code still runs correctly. This means that we will promptly correct any errors that emerge while testing our code. Regression testing will involve re-executing our test cases which may have passed before. Often, new changes can break older code, so this verifies that the newer code is compatible with the already existing codebase.


## Continuous Integration

Continuous integration is the practice of regularly merging code into the main branch of the repository, as well as regularly testing code. This practice will allow for automated testing as well. A strategy we may use is to get a continuous integration tool to streamline the continuous integration process. One possible tool is GitLab, which has features such as team planning tools and merge trains.
