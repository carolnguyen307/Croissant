![croissant icon](photos/imageedit_1_5470181020%20(1).png)
# Croissant Connoisseur: Sharing the Love of Croissant Craft

_By Carol Nguyen_

## Introduction to Problem Statement
 
Nearly a decade ago, I entered the world of pastry with a curious question: Why do the French have such a deep love for croissants and pastries? Is it just the sweetness and the dopamine rush that comes from eating them, or is there something deeper and more meaningful that I had not yet discovered?

In my quest for answers, I found myself in the heart of a bustling kitchen, learning the craft of pastry-making from the ground up. What began as curiosity soon evolved into a deep passion, especially for the handmade creations born from love and care. Yet, of all the pastries I encountered, the croissant held my heart captive like no other. Crafting the perfect croissant is an art form, it is not just simply following a recipe. It is about patience, precision, physical effort, and a deep understanding of both science and artistry. A perfect croissant is more than food. It is a masterpiece where every layer and fold whispers a story. When done right, a croissant is a symphony of texture and taste, a testament to the baker’s dedication. But how about a bad croissant? It is the product of shortcuts,a reflection of indifference, devoid of soul.

Yet, I could not help but notice that the croissant often goes unappreciated, brushed off by some as nothing more than a dry piece of dough. But I believe, to truly fall in love with a croissant, you have to experience the right one, the kind that inspires passion with every bite. A bad croissant will never evoke the adoration this delicate masterpiece deserves. And that got me thinking: could I change this? Could I help elevate the croissant to the status it is worthy of? This realization sparked a fire in me, fueling a mission to spread the love for croissants far and wide.
 
Since I cannot always be there to guide someone when they are choosing a croissant, I realized I needed to create something that could. Something that could always be with them, offering instant advice on whether that croissant is worth savoring. That is when the idea for Croissant Connoisseur was born, a clever app designed to help anyone identify a high-quality croissant with just a snap. Users simply take a photo of the croissant they are eyeing, and the app does the rest, analyzing key indicators like color, flakiness, and the number of visible layers. In seconds, it provides a recommendation, ensuring that each bite they take is well worth it, and helping people indulge with confidence.

As buyers begin to savor the finest croissants, their appreciation for this artisanal pastry will deepen, spreading the love for the craftsmanship and care that goes into creating the perfect croissant. Over time, Croissant Connoisseur will not just help users discover great croissants,it will also foster a genuine love and respect for the art of pastry-making.


## Problem statement

How can I design a tool that accurately determines whether the croissant a user is about to buy is high-quality or lacking?

## Table of contents

1. [Data source](#Data-source)
2. [Workflow processes](#Workflow-processes)
3. [Required Python libraries](#Required-Python-libraries)
4. [Recommended visual analysis model](#Recommended-model)
5. [Future improvement](#Future-improvement)
6. [Summary](#Summary)

### Data source
To collect the dataset of croissant images, I employed a multi-faceted approach. First, I visited several local bakeries to personally capture photographs of both high-quality and substandard croissants. In addition, my classmates contributed to the dataset by providing their own photos of croissants. Furthermore, I utilized online resources such as Google search and social media platforms, including Instagram and Facebook, to source additional images. This diverse collection process ensured a comprehensive dataset, representing a wide variety of croissant qualities and styles.

### Workflow processes
1. The workflow started off doing an exploratory visual analysis on the above data source which are images of croissants. This first stage of visual analysis gives a hint of how a good croissant looks like.
2. Next, I implemented a range of models to classify the quality of croissants, beginning with a Baseline Convolutional Neural Network (CNN) as a binary classifier to distinguish between high-quality and substandard croissants. After achieving an train accuracy of 1.0 and validation accuracy of 0.61904, I expanded the task to a multiclass classification problem to categorize different levels of croissant quality. I then applied more advanced models, including VGG-16, MobileNet V2, and EfficientNet, with MobileNet V2 achieving the highest performance with train accuracy of 0.9846, validation accuracy of 0.9524 with lowest running time among other models with 54.2478 second.

Here's a tabular comparison of the key metrics measured for 4 models mentioned above:

| Model                     | Train Accuracy	 | Validation Accuracy	  | Run Time (s) |
|---------------------------|-----------------|-----------------------|--------------|
| Baseline CNN              | 1.0000          | 0.6190                | 56.71        | 
| VGG-16                    | 1.0000          | 0.9524                | 494.72       | 
| MobileNet V2              | 0.9846          | 0.9524                | 54.25        | 
| EfficientNet              | 0.9846          | 0.8571                | 68.17        | 

Based on the above comparison, I chose the MobileNet V2 model for app deployment.
3. Extract chosen model which is MobileNet V2 to HDF5 format so it will become ready for deployment.

### Required Python libraries
1. keras
2. matplotlib
3. numpy
4. os
5. pandas
6. scikit-learn or sklearn
7. skimage
8. tensorflow
9. time

### Recommended model
I selected the MobileNet V2 model for deployment due to its strong performance, demonstrating both high training accuracy and validation accuracy, with the smallest absolute difference between the two metrics (0.0322), indicating minimal overfitting. Additionally, MobileNet V2 had the shortest running time (54.25 seconds) among the four models evaluated, making it the most efficient choice for real-time applications.

### Future improvement
In future work, I aim to extend the application of deep learning models like MobileNetV2 by not only classifying croissants based on quality but also analyzing their structural characteristics, such as the number of layers. By developing a model that can count the layers of a croissant and provide detailed numeric information about the average number of layers found in high-quality pastries, I hope to bring a more data-driven approach to food assessment. This could offer valuable insights into what truly defines a perfect croissant, combining both visual quality and structural consistency to ensure only the best pastries are recognized.

### Summary
In conclusion, the MobileNetV2 model demonstrated its superior ability to classify images with remarkable accuracy, making it a versatile tool for various applications, including something as unique as evaluating croissants. Just as it excelled in distinguishing between complex visual patterns in this project, MobileNetV2 can be applied to assess the quality of croissants by analyzing subtle details like texture, color, and structure. This powerful model, with its deep learning capabilities, can differentiate between a perfectly baked croissant and one that falls short of expectations. By leveraging its precision and efficiency, businesses or enthusiasts could use MobileNetV2 to ensure that only the finest croissants meet their standards, enhancing the overall food experience. Whether it's image classification or food quality assessment, MobileNetV2 stands out as a top performer, consistently delivering reliable results across a range of tasks.



