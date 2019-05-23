------------------------------------------------------------------------------------
COMP 3201 - Final Project
------------------------------------------------------------------------------------
Notes before running:

- It is recommended to have at least Python 3.5 installed when compiling and running this 
  program, as it was originally written and complied using Python 3.5 & Python 3.7.1.
- Matplotlib must be installed in order to view the graphs after the program is run,
  see https://matplotlib.org/users/installing.html for instructions to install it.
------------------------------------------------------------------------------------
Running the program:
------------------------------------------------------------------------------------
1. Ensure all the files are in the same folder
2. Run the program: (Three ways that have been tested to work successfully)
 a. Using terminal on an Unix based system (ex. Mac OS, Ubuntu, etc.), the
    program can be started by navigating to the folder that the '.py' files are in
    using 'cd' followed by the path to the folder and then entering 'python3 main.py',
    this will compile and run the program
 b. Using command-line on windows(cmd), the program can be started by navigating to
    the folder that the '.py' files are in using 'cd' followed by the path to the 
    folder and then entering 'python main.py' this will compile and run the program
 c. Python's IDLE (https://docs.python.org/3/library/idle.html) can be using to
    run this program. When IDLE is open click File-->Open then select 'main.py' 
    from the folder where it was downloaded. Next click Run-->Run Module to start
    the program.

-------------------------------------------------------------------------------------
Modifying the program:
------------------------------------------------------------------------------------- 
- Additional cities text files can be added by putting them into the main folder 
  with the title format of TSP_[country]_[#cities]
- The EA can be changed by modifying the following variables at the top of the 
  main.py file:
    * populationSize  - Set the size of the population
    * mutRate         - Set the mutation rate for the offspring
    * xOverRate       - Set the CrossOver rate for offspring recombination
    * genLimit        - Set the maximum number of generations
    * fileName        - Manually select the file name
    
   
  