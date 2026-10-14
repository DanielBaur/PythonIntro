# PythonIntro


<br>
<br>


![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)


This repository contains the materials for the Python introduction course in the Systems Analysis, Design, and Testing practical course at Munich University of Applied Sciences.

The course teaches the basics of Python programming, with a focus on scientific computing. It is based on the [Python introduction course from Heidelberg University](https://www.physi.uni-heidelberg.de/Einrichtungen/AP/Python.php) and was initially adapted for the course by Sebastian Mortag and Herbert Palm. It has then been adapted by Daniel Wiebe, who also maintains this repository.


You are cordially invited to participate in this course by working through the materials at your own pace. The course consists of interactive [Jupyter Notebooks](https://jupyter.org), which combine executable code with explanatory text, equations, images, and more.



<br>
<br>


## Course Contents

- [Python Basics Part I: Programming Fundamentals](python%20basics%20part%20I.ipynb)
- [Python Basics Part II: Control Flow](python%20basics%20part%20II.ipynb)
- [Python Basics Part III: Functions and Modules](python%20basics%20part%20III.ipynb)
- [Python Basics Part IV: Numerical Computing with NumPy](python%20basics%20part%20IV.ipynb)
- [Python Basics Part V: Plotting with Plotly](python%20basics%20part%20V.ipynb)


<br>
<br>


## Python Programming in Science

Scientific programming starts with understanding a problem and breaking it into precise steps a computer can perform. Useful programs do more than produce an answer: they are understandable, testable, and practical to maintain.

[Python](https://python.org) is a readable, general-purpose language with a rich scientific ecosystem. Its interpreted execution can be slower than compiled languages such as C, C++, or Fortran, but libraries such as NumPy use optimized native code for computationally intensive operations. This lets scientists develop and inspect analyses quickly without giving up efficient numerical tools.

Good scientific code should:

- divide complex problems into manageable parts and reuse established tools
- be clear enough for others (and your future self) to understand
- be only as optimized as the problem requires
- make its steps reproducible, so others can run the code and verify the results

These principles are central to **reproducibility** and **open science**. In this course, you will learn Python fundamentals and apply them to numerical analysis and visualization. The goal is not just to write code that runs, but to produce work that can be understood, checked, and built upon.


<br>
<br>


## Setup

Complete these steps before starting the notebooks. The commands below assume Windows PowerShell; alternatives for macOS and Linux are shown where they differ.

### 1. Install the required software

- Install [Visual Studio Code](https://code.visualstudio.com/).
- Install [Git](https://git-scm.com/downloads). Confirm it is available in a new terminal with `git --version`.
- Install [Python 3.10 or newer](https://www.python.org/downloads/) separately; the VS Code Python extension does not include the Python interpreter. On Windows, use the Python installer and enable **Add python.exe to PATH** if offered. Confirm the installation in a new terminal with `py -3 --version` (Windows) or `python3 --version` (macOS/Linux). If you install Python while VS Code is open, open a new terminal or restart VS Code so it can detect the installation.

Python must be installed separately; VS Code uses that interpreter to create and manage project environments. A virtual environment is not strictly required, but it is recommended: it keeps this course's packages separate from other Python projects and helps avoid package conflicts.

### 2. Configure Git

Set the name and email that Git should associate with your commits. Use the email associated with your GitHub account, or your GitHub-provided `noreply` address if you prefer not to expose your personal email.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

GitHub authentication is only needed to clone a private repository or push changes. For public repositories, cloning over HTTPS does not require signing in.

### 3. Install the VS Code extensions

In VS Code, open the Extensions view and install:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) by Microsoft
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) by Microsoft

VS Code includes built-in Git support. The Python extension provides Python interpreter selection; the Jupyter extension provides notebook editing and execution.

### 4. Clone the course repository

In VS Code, open a terminal and run the following commands to clone the repository and change into its folder:

```bash
git clone https://github.com/DanielBaur/PythonIntro.git
cd PythonIntro
```

The clone URL will be available on the repository's GitHub page under **Code**. Open the cloned folder in VS Code with **File > Open Folder**.


### 5. Create a project environment and install packages

We recommend creating a project-specific `.venv` with VS Code so the course dependencies are installed in an isolated environment:

1. Open the Command Palette with **Ctrl+Shift+P** (Windows/Linux) or **Cmd+Shift+P** (macOS).
2. Run **Python: Create Environment** and choose **Venv**.
3. Select the Python 3.10+ interpreter you installed.
4. When prompted for dependencies, select `requirements.txt` in the repository root.

VS Code creates `.venv`, installs the packages listed in `requirements.txt`, and selects the new environment for the workspace. The file lists NumPy, Plotly, and `ipykernel`, which the course notebooks use.



### 6. Open and run a notebook

Open a course notebook in VS Code. If prompted to select a kernel, choose the Python interpreter in the repository's `.venv`. Click **Run Cell** or press **Shift+Enter** to execute a code cell.


