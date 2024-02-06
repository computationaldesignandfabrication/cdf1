# Computational Design and Fabrication (CDF)

## Welcome

Welcome to [**Computational Design and Fabrication**](https://computationaldesignandfabrication.github.io/computational_design_and_fabrication/), a platform dedicated to beginner-friendly creative coding tutorials and exercises for computational design and fabrication in architecture.


## Session Blocks

Title | Description | Slides  
----- | ----------- | ------
**Python Basics** | Quick start on Python | [Python Basics](https://docs.google.com/presentation/d/1VDaIxVtl5dnydUoDbgl7tOkzcTfhUV11hmd7pZFogok/edit?usp=sharing)
**Session 1** | Session 1  | Session 1 Slides
**Session 2** | Session 2  | Session 3 Slides
**Session 3** | Session 3  | Session 3 Slides



## Requirements

* Windows 10 Professional
* Rhino 7 / Grasshopper
* [Anaconda Python](https://www.anaconda.com/distribution/?gclid=CjwKCAjwo9rtBRAdEiwA_WXcFoyH8v3m-gVC55J6YzR0HpgB8R-PwM-FClIIR1bIPYZXsBtbPRfJ8xoC6HsQAvD_BwE)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Github Desktop](https://desktop.github.com/)

## Dependencies

* [COMPAS](https://compas-dev.github.io/)

## Getting started

Set up your Python environment following these instructions:

### Setting up the Anaconda environment with COMPAS

Execute the commands below in Anaconda Prompt:
	
    (base) conda config --add channels conda-forge
    (base) conda create -n cdf compas
    (base) conda activate cdf
    
#### Verify Installation

    (cdf) pip show compas
####
    Name: compas
    Version: 2.0.0
    ...

#### Install on Rhino

    (cdf) python -m compas_rhino.install -v 7.0


### Cloning the Course Repository

Firstly, create a workspace directory:

C:\Users\your_username\workspace

Then open Github Desktop and clone the [CDF repository](https://github.com/computational_design_and_fabrication/computational_design_and_fabrication) into you workspace folder.

**Now you can go to VS Code, Rhino, or Grasshopper to run the example files.**
