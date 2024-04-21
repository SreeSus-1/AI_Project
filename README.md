# AI_Project
**#Genetic Algorithm**

**Genetic Algorithm for Feature Selection**
This program implements a genetic algorithm for feature selection using cosine similarity as the fitness function. The algorithm evolves a population of binary feature vectors over multiple generations to maximize classification accuracy on a validation dataset.

**How to Run the Program**
**Data Preparation:**
Prepare your training and validation datasets in CSV format.
Ensure that the training and validation labels are provided in separate files.
In this project Datasets are: 
 **Training DataSets:**
  File train.csv 
  File label_train.csv 
  **Validation DataSets:**
  File validate.csv 
  File Label_validate.csv
**Program Execution:**
Place the program file (genetic_algorithm.py) in the same directory as your datasets.
Open the terminal or command prompt.
Navigate to the directory containing the program and datasets.
![image](https://github.com/SreeSus-1/AI_Project/assets/164704978/aa0137fd-67f4-46d1-8f29-635bfd3b200c)

Run the program using the command:
**Copy code:**
python genetic_algorithm.py train.csv label_train.csv validate.csv Label_validate.csv
Replace train.csv, label_train.csv, validate.csv, and Label_validate.csv with the filenames of your training data, training labels, validation data, and validation labels respectively.
Adjust Parameters (Optional):
You can adjust the following parameters in the program according to your requirements:
num_features: Number of features in the dataset.
population_size: Size of the population for each generation.
max_generations: Maximum number of generations for the genetic algorithm.
mutation_rate: Probability of mutation during reproduction.
**Program Output**:
After running the program, it will display the following information:

Number of classes in training and validation labels.
Final optimized feature vector accuracy on the validation dataset.
Number of qualified feature vectors and their indices.
A line graph showing the fitness score over generations.
**Requirements**:
  Python 3.x
  NumPy
  pandas
  Matplotlib
  scikit-learn
Ensure that you have the required Python packages installed before running the program.
