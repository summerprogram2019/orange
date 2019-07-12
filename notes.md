
## Backend

Django
- Why?
    - Familiarity with django
        - Two weeks is not enough time to learn a new framework  
- Speed
    - Like any good framework, most things are done for you! For the demo, we didn't have to worry about
        - hosting
        - database management
        - user authentication
    - Can develop extremely fast
    - Very well documented


## Machine learning
Demo Limitations.
Trade off between accuracy and performance (can't use models that are too computationally expensive for our mobile application).
Problem: Not enough time to gather food dataset, and to train a model. Solution: pretrained
Pretrained on the imagenet classification challenge (1000 classes). Input is an image, output is a "confidence" value for each of the 1000 classes.
Problem: Of these 1000 classes, only around 50 are food, don't want to be able to classify non-food images. Solution: Only look at the outputs of food classes to determine the most likely food, and normalize the confidence of these classes outputs.

