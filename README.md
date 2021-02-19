# WeatherMe! - ML

This project contains a machine learning algortithm for predicting weather in the US, Canada and Israel.

*Disclaimer:* This project by no means tries to get as good as current research in weather predictions. None of th epeople working on this project are studied metrologist or have the computation power to calculate it with all the parameters required to predict the weather for tomorrow.

## Why do it?
I created this project only for one purpous: To create a ML model that can predict something. I chose the temperature for this task, because the weather is one of the things that require an insanely high amount of computation power and knowledge to predict it. And even the current methods that use complex models are getting it wrong.

So I though, this is a challenge! Let's build a model that at least can guess a little better than I do. Also I wanted to keep it simple. With simple I mean that the final model needs to be working on one or two Raspberry Pis or at least on my entry level MacBook Pro from 2017. So that means I have to limit myself to just a few parameters I want to use. And while doing some research on this topic, I found a dataset on kaggle.com which included the collected hourly weather measurements of 30 cities in Canada and the US + 5 cities in Israel. Living in germany, this doesn't really makes sense for me and I might also be changing that dataset in the feature (if I do so, I will update this README).

## Which techniques do I use?
This time I decided to use the python framework TensorFlow, specifically the framework part Keras to train and create this model. I chose to use TensorFlow because it was the first framework that comes to my mind when I hear ML or anything AI related. Also TensorFlow has a big community of users, so it is easy for me to find help when I have a problem. Another bonus of TF is that it is opensource, like this model here. In addition to TensorFlow I will use the python libraries numpy, matplotlib, pandas and seaborn, to prepare, manage and plot the dataset we will use for the training.

Another peace of software I use is anaconda, which is similiar to venv, so it helps me managing my dependencies between my devices and between projects.

Also jupyter is used in this project to visualize the data better and keep anotations and code in an easy readable file. If you do not want to use jupyter for running the code, I also will add all the code to standard python files that you can open and run.

## How can I get started working on this project?
If you want to help me building this project, or just want to train the model yourself, e.g. because you have a dataset that is similiar and want to train it, after cloning you have to do following steps.

1. Install anaconda from anaconda.org
2. run ```conda create -n tensorflow python=3.8 anaconda``` This command creates an empty virtual environment and installs some helpul dependencies
3. Insert the venv using ```conda activate tensorflow```
4. Install the dependencies. To install the project specific dependencies, you can run the command ```pip install -r REQUIREMENTS.txt```. This command will install all the project specific environments we need for training and testing.
5. Open your favourite code editor and start coding!

## Future planned:
All the parts down here will be added to the project in the future. They are already included in the README so I can keep track of my ideas.

**EVERYTHING BELOW HERE IS WORK IN PROGRESS AND WILL BE ADDED LATER TO THE CODEBASE!**

## How can I access the predictions?
To access the predictions our model creates with for example an App or IOT Device, I will create a Web API using django. Down here you will find a definition of all endpoints the API uses to make the data available to the App or Web service. In addition to the table below, you can also find the API endpoints in the api documentation in the API folder in this repository.

### API Endpoints


