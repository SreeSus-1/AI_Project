import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load training files
train_data = pd.read_csv("train.csv", header=None)
train_labels = pd.read_csv("label_train.csv", header=None)

# Step 2: Load validation files
validate_data = pd.read_csv("validate.csv", header=None)
validate_labels = pd.read_csv("Label_validate.csv", header=None)  # Corrected file name

# Step 3: The data files consist of a feature vector consists of 1433 features.
# No additional action needed here as we've loaded the feature vectors in Steps 1 and 2.

# Step 4: Create population of random solutions
def generate_population(feature_count):
    population_size = np.random.randint(50, 100)  # Increased population size
    population = []
    for _ in range(population_size):
        chromosome = np.random.randint(2, size=feature_count)
        population.append(chromosome)
    return population, population_size

# Step 5: Select random generations
def select_random_generations():
    return np.random.randint(1, 10)  # Increased number of generations

from sklearn.metrics.pairwise import cosine_similarity

def evaluate_fitness(population, data, labels):
    accuracies = []
    for chromosome in population:
        selected_features = data.iloc[:, chromosome == 1]
        similarity_matrix = cosine_similarity(selected_features)
        accuracy = np.mean(similarity_matrix)
        accuracies.append(accuracy)
    return accuracies

# Step 7: Define function for selection
def selection(population, accuracies):
    # Select the top 50% of the population based on accuracies
    sorted_indices = np.argsort(accuracies)[::-1]
    selected_population = [population[i] for i in sorted_indices[:len(population)//2]]
    return selected_population

# Step 8: Define function for crossover
def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1)-1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

# Step 9: Define function for mutation
def mutation(chromosome, mutation_rate=0.1):  # Decreased mutation rate
    mutated_chromosome = chromosome.copy()
    for i in range(len(mutated_chromosome)):
        if np.random.rand() < mutation_rate:
            mutated_chromosome[i] = 1 - mutated_chromosome[i]  # Flip the bit
    return mutated_chromosome

# Example usage:
feature_count = 1433
population, population_size = generate_population(feature_count)
generations = select_random_generations()

best_accuracy = 0
final_best_features = None

print("Population Size:", population_size)
print("Generations:", generations)

# Lists to store the best accuracy for each generation
best_accuracies = []

for generation in range(generations):
    accuracies = evaluate_fitness(population, train_data, train_labels)
    print("Generation:", generation+1 , "Best selected features:", population[np.argmax(accuracies)])
    
    # Store the best accuracy for this generation
    max_accuracy_index = np.argmax(accuracies)
    best_accuracies.append(accuracies[max_accuracy_index])
    print("Best accuracy for generation", generation+1, ":", accuracies[max_accuracy_index])

    # Validation
    # validate_accuracies = evaluate_fitness(population, validate_data, validate_labels)
    # validation_accuracy = np.mean(validate_accuracies)
    # print("Validation accuracy:", validation_accuracy)

    # Selection
    selected_population = selection(population, accuracies)
    
    # Crossover
    new_population = []
    for i in range(0, len(selected_population), 2):
        if i+1 < len(selected_population):
            parent1, parent2 = selected_population[i], selected_population[i+1]
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([child1, child2])
    
    # Mutation
    mutated_population = [mutation(chromosome) for chromosome in new_population]
    
    # Combine selected population and mutated population
    population = selected_population + mutated_population
    
    # Update best features and accuracy
    if accuracies[max_accuracy_index] > best_accuracy:
        best_accuracy = accuracies[max_accuracy_index]
        final_best_features = population[max_accuracy_index]

# Plotting the fitness score graph
plt.plot(range(1, generation + 2), best_accuracies)
plt.title('Fitness Score Over Generations')
plt.xlabel('Generation')
plt.ylabel('Fitness Score')
plt.grid(True)
plt.show()

# Print final best selected features after all generations
if final_best_features is not None:
    print("\nFinal best optimized features:", final_best_features)
    print("Final features count:", np.sum(final_best_features))
    print("Final accuracy:", best_accuracy)
else:
    print("\nNo best features found.")
