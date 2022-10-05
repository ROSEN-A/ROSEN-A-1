# Design Activity

## This document will be our starting tool to approach our design for the upcoming project
Note: This is considered a research for at the moment, for
1) The team's understanding and how to approach design strategies, and
2) Our team is yet to receive specific instructions or specifications from our client.
Once we are clear with what our requirements are and specifications, we will come up with a better and concrete design details.

## Design Architecture
**Definition:** 
- High-level design software to which developers can start adding details on the project.
- Definite/specific features can be added to the design as details of the project starts coming
- This helps to collaborate and start sketching out the big picture of the development, including creating a prototype

## How to design software architecture?
- Clear understanding of requirements
    - High level view or sketch, such as mind-mapping the requirements
    - Divide into functional and non-functional requirements needed
- Breaking down requirements into one-unit component
    - i.e: dividing architectural design into slices
- Create the prototype
    - Make sure it follows all guidelines
    - Revisions or peer review from team members
- Consider performance, scalability, portability, extensibility and compliance in design

## Example of design architecture
![Design Architecture](https://d3i71xaburhd42.cloudfront.net/4cd105262aa01f62b88baeda78570325661f67d3/3-Figure1-1.png)
 
## Best Practices in software architecture design
- **Always** visualize the design (diagram, blueprint, etc)
- Design is an iteration. Revisions are necessary
- Be cautious of requirements, you don't want requirements to adversely affect the design, consequently the project
- Keep components and design updates in your mind as revisions are made

## What design architecture tools will we use? [To be changed]
With the given circumstances of not having specific requirements , we cannot really tell what design architecture we will be moving forward with. (To be changed)
There will be a couple of options that we could use to designing and extracting software architecture:
- Doxygen (as given in the lecture)
- Gitbook
- Swagger.io
- Confluence
- MkDocs
- Sphinx

## Applying UI Design
There are some guidelines that we will have to adhere to in terms of making UI design
Following from [design firefox photon guidelines](https://design.firefox.com/photon/introduction/principles.html) is the closest we can get to achieving best interface for our client. Since our product will deal with web application, this following points are necessary to be kept in mind as we are progressing through our project
1) Adaptable
    - Simple features that will be easy to use for new users regardless of tech experience
2) Quick
    - Responsive features
    - Give accurate animation on task completion (and make sure it's fast!)
3) Aware
    - Prompt user to make them feel safe to browse around
    - Act upon users' agreement
4) Approachable
    - Welcoming design, minimalistic, and inclusive
5) Supportive
    - Provide as much as we can to meet as much users' need and desires
    - i.e: proactive website
6) Whimsical
    - Fun to use product
    - i.e: highly interactive responses, but not intimidating

## Privacy By Design by Ann Cavoukian
- "data protection through technology design"
- Privacy can't be assured solely by compliance, but it needs to be default mode of operation in software development process
- 7 foundational principles:
    1) Proactive not Reactive; Preventative not Remedial
    2) Privacy is the Default Setting
    3) Privacy Embedded into Design
    4) Full Functionality — Positive-Sum, not Zero-Sum
    5) End-to-End Security — Full Lifecycle Protection
    6) Visibility and Transparency — Keep it Open
    7) Respect for User Privacy — Keep it User-Centric Incorporate 

## Design database technology
For our projects, we will be dealing with thousands or millions possible data source that will be sourced by our client. The purpose of this data is to be ran against our soon to be created Active Learning Algorithm. 
Focusing on the tools that we will be creating, the data will be utilized in the following manner:
Given:
- Working Active Learning Algorithm (ALA)
- User Interface - Website in our case
 
To do:
- Create a database to store data source (pictures)
- Create a back-end to process the data source (pictures)
- Connect back-end and front-end framework
    - front-end giving user the output as will be discussed/intended
    - back-end use to run the data source against the ALA created

## Database Technology
(To be changed)
Re-iterating what has been mentioned earlier, given the circumstances that the final product requirements is still unknown at the time this document is being made.
We will find a suitable database that can be easily connected and compatible to the front-end tools we will be using.
However, to our knowledge we know that efficieny and performance is at utmost importance in deciding which database to be used, hence:
1) Data model: 
    - Relational database or non-relational database
    - our data will mostly be used to store pictures
    - the affect on performance is quite large when storing images/videos
    - We might end up using MySQL (if we are looking at relational database)
    - with these points in mind, MongoDB is the safest to use at the moment regarding performance
    - Relatively quick retrieval using MongoDB will save us a lot of time when retrieving images

2) Storage model:
    - Column-oriented data model
    - Excellency in compression in column-oriented data model
    - faster performance compared to a row-oriented one

3) Distributed vs. Centralized:
    - We will be using centralized database
    - easier to access and coordinate data
    - confidentiality in client is very important in our project, hence we will lean to avoid using distributed database