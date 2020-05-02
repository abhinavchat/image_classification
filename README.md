# Cat-Dog Image Classification

[![Build Status](https://travis-ci.org/abhinavchat/image_classification.svg?branch=master)](https://travis-ci.org/abhinavchat/image_classification)

## Why
Tensorflow is hard enough to wrap one's head around. It has several parts that deal with preparing data, defining and training a model and finally, outputting a model that can then be used to categorize (infer) other data. There's math involved, new vocabulary to learn and on top, a toolchain which revolves around Python.
This project only addresses serving a Tensorflow pre-trained image categorization model, otherwise called the Inception model.  

## Prerequisites
- Python 3.6 or greater
- Tensorflow 2.1 or greater


## Run
```flask run```

Navigate to http://localhost:5000 and upload an image. The backend will categorize the image and output the result along with the probability.