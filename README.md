## Behavior-Driven Development (BDD): Python Behave

This repository demonstrates how to carry out behavior-driven development tests using Behave in Python programming language.
Behave is a bahavior-driven development framework that allows writing of test cases in human-readable format. 
It highlights how to define features, scenarios, steps, etc., and how to execute behave from the terminal.

### Setup and Installation
Before you proceed, ensure that you have Python3.x and pip install on your computer.

**Step 1**: Clone this repository and navigate to the code directory as shown below:
```bash
git clone https://github.com/ginjardev/behavior_driven_development_python_behave.git
```
```bash
cd behavior_driven_development_python_behave
```

**Step 2**: Create a virtual environment in your project folder with the following command on the terminal:
```bash 
python3 -m venv env
```

**Step 3:** Activate the environment:
```bash
source env/bin/activate
```

**Step 4:** Install the dependencies  from the cloned project directory:
```bash
pip install -r requirements.txt
```

### Authentication

**Step 5:** Set [LambdaTest](https://www.lambdatest.com/) **Username** and **Access Key** in environment variables.

In order to run your tests on LambdaTest cloud platform, you will need to set your [LambdaTest profile](https://accounts.lambdatest.com/dashboard) username and access key in the environment variables. Click the **Access Key** button at the top-right of the Automation Dashboard to access it.

See image below:
![username_access_key](access_key_username.png)

* **Linux/mac OS**
```bash
export LT_USERNAME="YOUR_USERNAME" 
export LT_ACCESS_KEY="YOUR ACCESS KEY"
```

* **Windows**
```bash
set LT_USERNAME="YOUR_USERNAME" 
set LT_ACCESS_KEY="YOUR ACCESS KEY"
```

### Executing The Test
**Step 6:** From the base repository, execute the command below in your terminal.
```bash
behave
```

Your test results would be displayed on the console and on LambdaTest automation dashboard.


### Results
View test results on LambdaTest web automation dashboard.
 ![result](behave_lambdatest_result.png)

