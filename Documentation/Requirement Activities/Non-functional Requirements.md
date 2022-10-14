# Non-functional requirements

This document will cover our non-functional requirements in our project, or also known as backlog constraints. These are set of specifications/requirements that restricts our project in order to attemp to improve functionality against different backlogs.

Keep in mind that our project will deal mainly with 1) Web interface, 2) Processing large amount of data (possibily thousands or hundreds of thousands) in form of pictures and videos

1. Performance
    a. Website should take no more than 1s to load, and will alow user to navigate right after
    b. With proper training of the Active Learning Algorithm, we expect our program to be able to execute classification and produce output within .1s to 1s
    c. We will attempt to make our program classifies simultaenously, i.e: be able to classify multiple images at a single time

2. Security
    a. Software will ensure the integrity of our client's information
    b. Software will not save client's data automatically, to prevent any access to sensitive information
    c. No database, only local storage. We will rely on full-disk encryption deal with confidential data

3. Portability and Compatibility
    a. Software must be able to run in end-users' machine (for details refer to Environmental constraint)

4. Reliability
    a. Software will be able to process large amount of data without failure
    b. Software would be able to be re-used by different users at a different time without failure

5. Usability
    a. Navigation: User will be able to learn and navigate fairly easily through the interface
    b. Features: Intuitive features will be integrated such as use of magnifying glass in images to zoom on images

6. Robustness
    a. Catching invalid input to avoid any problems
    b. Prevent any unwanted behaviour when image processing is interrupted
    c. Fail-safe software and provide meaningful response to UI when software fails at any point

7. Data Integrity
    a. Ensure that software will be classifying objects with close to a 100% accuracy
    b. Ensure enough training on ALA to minimize any image processing error
    c. Consistency in output/computation over the lifecycle of the software