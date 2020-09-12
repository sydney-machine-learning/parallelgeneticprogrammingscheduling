

SPECIES_SIZE = 256
LAMBDA=256
NUM_SPECIES = 8

IMPROVMENT_TRESHOLD = 0.5
IMPROVMENT_LENGTH = 5
EXTINCTION_TRESHOLD = 5.0
# Parameters for GP
N_RUNS=1

NUM_GENERATIONS=40 # Number of generation to evolve  NOTE : EACH GENERATION ONLY ONE SPECIES EVOLVES SO NUM_GENERATIONS SHOULD BE ACTUAL GENERATIONS x NUM_SPECIES
MATING_PROB=0.8 # Probability of mating two individuals
MUTATION_PROB=0.2 # Probability of introducing mutation
SELECTION_POOL_SIZE=7 # Number of individuals for tournament
HEIGHT_LIMIT = 7 # Height Limit for tree

GEN_MIN_HEIGHT=2
GEN_MAX_HEIGHT=5