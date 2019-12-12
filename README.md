# Programming for Data Analysis Project
This repository is based on the project instructions found [here](https://github.com/brianmcgmit/ProgDA/raw/master/ProgDA_Project.pdf).

# Required Software
[Python](https://www.python.org/downloads/)

## Required Python Packages
- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Pandas](https://pandas.pydata.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Scipy](https://scipy.org/install.html)
- [iteround](https://pypi.org/project/iteround/)
- [Jupyter](https://jupyter.org/install.html)

# Download
The repository can be downloaded from [here](https://github.com/ANihill/fundamentalsProject.git).

# Summary of Project
The English Premier League Table has some interesting factors after all games have been played. There is the phenomenon of hoem field advantage; the fact that teams almost universally perform better when playing their games at home. In generating a random data that bore the characteristics of the real world Premier League table it was important to account for this difference in performance. Data was first generated for the number of goals teams scored and conceded at home, this in turn led to number of goals scored and conceded away from home. 

What about points accrued by teams? Analysis of the real world data pointed towards a strong correlation between a teams goal diffence, i.e. the difference between their goals scored and conceded, and the amount of points they gained. Once a distribution was decided on for generating points data, points were assigned to teams based on their goal difference.

The code used to generated the random data is presented in two ways. Firstly, the code was presented in blocks detailing each step of the process in the notebook and secondly, it was compiled into a python script that can be run from the notebook outputting a random completed table in order to see how examples of home the code works.

# References 
- https://www.researchgate.net/publication/285968917_Home_advantage_in_soccer_Variations_in_its_magnitude_and_a_literature_review_of_the_inter-related_factors_associated_with_its_existence
- https://www.betfair.com.au/hub/poisson-distribution/
- https://stackoverflow.com/a/44308018
- https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/
- https://docs.scipy.org/doc/numpy-1.14.1/reference/generated/numpy.random.poisson.html
- https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.normal.html
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncnorm.html
- https://seaborn.pydata.org/tutorial.html
- https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html
- https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html
