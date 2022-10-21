# Non-functional requirements

*[NOTE]: Our project scope will be redefined in the near future, some of these non-functional requirements are to be changed accordingly*

This document will cover our non-functional requirements in our project, or also known as backlog constraints. These are set of specifications/requirements that restricts our project in order to attemp to improve functionality against different backlogs.

Keep in mind that our project will deal mainly with 1) Web interface, 2) Processing large amount of data (possibily thousands or hundreds of thousands) in form of pictures and videos

1. Performance
    a. Website should take no more than 1s to load, and will alow user to navigate right after
    b. With proper training of the Active Learning Algorithm, we expect our program to be able to execute classification and produce output within .1s to 1s
    c. We will attempt to make our program classifies simultaenously, i.e: be able to classify multiple images at a single time
    d. Active Learning Algorithm will be able to classified images after couple of iterations, which means manual intervention will be minimized in order to train the algorithm.

2. Security
    a. Software will ensure the integrity of our client's information
    b. Software will not save client's data automatically, to prevent any access to sensitive information
    c. Databases:
        - Database might be integrated in our program for the sake of simplicity in storing and retrieving information to and from the user
        1) If used, we will ensure that database doesn't store any confidential information that will be received from any client's, i.e: Database will only consist of models we will be creating from blender, and our active learning algorithm to ensure that images store in the cloud is public data.
        2) If not used, we will stay in using local storage as our main point of communication of data transfer. With this, we will ensure local disk encryption is maintained so data is fully secured.

3. Portability and Compatibility
    a. Software must be able to run in end-users' machine (for details refer to Environmental constraint)

4. Reliability
    a. Software will be able to process large amount of data without failure
    b. Software would be able to be re-used by different users at a different time without failure

5. Usability
    a. Navigation: User will be able to learn and navigate fairly easily through the interface
    b. Features: Intuitive features will be integrated such as use of magnifying glass in images to zoom on images
    c. Software created will encapsulate all the processing as 'behind the scene', hence the user will only need to input and receive final output without any details during the process.

6. Robustness
    a. Catching invalid input to avoid any problems.
        1) Only images and videos are allowed as input
        2) Any other input will be prevented to avoid unwanted behaviour.
    b. Prevent any unwanted behaviour when image processing is interrupted
    c. Fail-safe software and provide meaningful response to UI when software fails at any point

7. Data Integrity
    a. Ensure that software will be classifying objects with close to a 100% accuracy
    b. Ensure enough training on ALA to minimize any image processing error
    c. Consistency in output/computation over the lifecycle of the software

8. Scalability.
    a. Program will be made based on local system (of developers), which might not be able to handle large amount of rendering or processing since it might take a large computer requirements.
    b. Ensuring that program will run without issues for certain set amount of data (minimum requirements from client)
