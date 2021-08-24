# Compatibility Learning



## 2. Importance of Categories

There are two types of categories in the [MetaData](https://drive.google.com/file/d/13-J4fAPZahauaGycw3j_YvbAHO7tOTW5/view), i.e. **category_id** and **semantic_category**.
A possible explaination for the performance of the existing Compatibility Learning models is that these models are learning categories. We discuss that if there is similar categories in the negetive outfit samples (low quality negative samples), the model can perform well in compatibility learning task when it only learns categories. To evaluate this assumption, we train some predictive models on the dataset when only the category of the images are present in the dataset.

### 2.1. Training on category_id
We use the compatibility list provided in the polyvore dataset. This list includes 16,995 positive and 16,995 negetive samples of outfits. For each instance, we only include the category_id in the training dataset. category_id is an integer number for each image. The integer is between 1-224. Similarly we treat the test dataset which includes 15,145 positve instances and 15,145 negative instances. You can use creat_dataset_from_metadata_handler.py to generate these lists.

We train a Decision Tree, a Logistic Regression, and a MLP network on this training set (cat_id_importance_eval.py). The results show no better than random prediction for all three models.

Decision Tree:
<img width="471" alt="image" src="https://user-images.githubusercontent.com/71953974/130694146-ead84976-d5e8-4355-bef7-c08422a40841.png">

Logistic Regression:
<img width="473" alt="image" src="https://user-images.githubusercontent.com/71953974/130694283-58f08ece-b7a6-48a5-85a6-840da16bdc44.png">

MLP:
<img width="470" alt="image" src="https://user-images.githubusercontent.com/71953974/130694352-dbe64612-9393-4171-819f-23555b4317fb.png">


# Compatibility_Learning_StyleGan
Compatibility Learning 
