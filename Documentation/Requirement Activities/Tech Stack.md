# Tech Stack

The tech stack includes all the technologies Project ROSEN will be built with. After 7 weeks of discussion with the client, we have decided to use the following technologies in our web application.


---


## Web User Interface


The technologies our team plans to implement for the Web User Interface are Dash, Python, and Javascript

- The Dash framwework is a visualization framework based on Python, which the client has required.

- The dash framework is based off the django framework and it will be mainly used for our web interface. We chose Dash because:

        - firstly, the client is a data scientist and he has recommended us to use dash as our visualization framework. This will ensure that user has previous experiences using dash and the interface of our application will not be so unfamiliar.
        - second, there are many documentation around dash that will be us, the developers, to better understand how to implement the technology into our system. also, the user can also benefit from the abundant resources.

- For the backend, we will use Python, which is also a requirement we must adhere to.

        - Python is a common choice for data scientists that works with a lot of data. We will provide the user with room to modify and enhance our code by implementing the software in the language the client is most comfortable with.

- Javascript will be used for the frontend, along with HTML and CSS.


---


## Prototype Modelling & Active Learning Algorithm


The technologies our team plans to implement for the Prototype Modelling and the Active Learning Algorithm are OpenCV, Blender, and VGG-16.

- OpenCV will be used for processing the video frame images.

- Blender will be used to simulate models for the pipeline prototypes.

- VGG-16 is the neural network encoder that converts the video frame images to vectors, which will be used as input for our active learning algorithm.


We are currently still researching what active learning algorithm to implement, one possibility is ModAL, an active learning framework for Python with lots of flexibility.
The active learning algorithm is first pre-trained by the development team, using manual labelling.

- The active learning algorithm will be used to classify video frame images that have been encoded by VGG-16.
