# A REST API predicting StackOverflow tags

For a StackOverflow question and its associated title, gives:
- the probabilities of the top 50 most popular tags on the website
- the list of the predicted tags (output a list of every tag for which P>0.5)

Made with [FastAPI](https://fastapi.tiangolo.com/), deployed on [Heroku](https://www.heroku.com/). 

## Endpoints, Swagger & documentation

Access the Swagger & doc [HERE](https://stackoverflow-tags-pred.herokuapp.com/docs)  

Get the probabilities for each tag at this endpoint (POST) : 
https://stackoverflow-tags-pred.herokuapp.com/proba

Get a list of the predicted tags at this endpoint (POST) : 
https://stackoverflow-tags-pred.herokuapp.com/prediction

## The model behind the predictions
A simple sklearn MultiOutputClassifier with logistic regressions trained on TF-IDF.

## Notebooks and slides (prensentation)
- [notebook_exploration.ipynb](https://github.com/fauconnier-n/stackoverflow_app/blob/master/notebook_exploration.ipynb) contains all the data cleaning, pre-processing, EDA, and some (failed) attempts at Dimentional Reduction

This project was made as part of my Machine Learning Engineer & Data Science degree at OpenClassrooms. 
**Files and comments are in French** (mandatory at OpenClassrooms). Don't hesitate to contact me if you have any question/misunderstanding.

nb. OpenClassrooms is the largest online education platform in France, and delivers state recognised University level trainings/diplomas.
