# Non-functional requirements

*[NOTE]: Our project scope will be redefined in the near future, some of these non-functional requirements are to be changed accordingly*

This document will cover our non-functional requirements in our project, or also known as backlog constraints. These are set of specifications/requirements that restricts our project in order to attemp to improve functionality against different backlogs.

Keep in mind that our project will deal mainly with 1) Web interface, 2) Processing large amount of data (possibily thousands or hundreds of thousands) in form of pictures and videos

1. Performance
    a. Website should take no longer than 1 second to load
    b. Active Learning Algorithm should be able to query database within 1-2s

2. Security
    a. Software will not save data automatically, this will be an option to user
    b. Database will only store filepath, hence images will not be floating around in cloud
    c. Real images will be stored locally, confidential data is kept local

3. Reliability
    a. Software will be able to handle large amount of image processing without failure
    b. Ensure software will be able to classify image as close to 100% accuracy
    c. Ensure consistency in input processing and output over the lifecycle of the software

4. Usability
    a. Website will be simple and easy to navigate and browse around
    b. Intuitive features will be integrated to website such as magnifying glass to zoom into image

5. Robustness
    a. Software will catch any invalid input to avoid any processing problems
    b. Prevent any unwanted behaviors when image processing or learning algorithm is under progress
