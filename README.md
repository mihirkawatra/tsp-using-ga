# tsp-using-ga
Solving the Traveling Salesman Problem using Genetic Algorithm in Python

## Running in Jupyter Notebook(Anaconda)

    conda create -n new-env python=3.8 
    conda activate new-env
    pip install jupyter==1.0.0
    pip install scipy==1.3.2
    pip install matplotlib==3.1.1

Open Jupyter Notebook by typing: `jupyter-notebook`

## Running via terminal

    usage: travelling-salesman.py [-h] [-n N_CITIES] [-x CROSS_RATE] [-m MUT_RATE] [-p POP_SIZE] [-g GENS]
    
      
    
    optional arguments:
    
    -h, --help  show this help message and exit
    
    -n, --n-cities N_CITIES Number of Cities
    
    -x, --cross-rate CROSS_RATE Cross Rate
    
    -m, --mut-rate MUT_RATE Mutation Rate
    
    -p, --pop-size POP_SIZE Size of Population
    
    -g, --gens GENS  Number of Generation

### Sample Execution:

    python travelling-salesman.py -n 20 -x 0.1 -m 0.02 -p 500 -g 500

