# Reflection

## 1. What did you learn from using static code analysis tools?

I learned that static code analysis can identify code quality, security, naming, exception-handling, and formatting problems without depending only on manual testing. Pylint helped identify code-quality and maintainability problems, Bandit identified security-related issues, and Flake8 identified style and formatting problems.

## 2. Which tool was most useful and why?

Bandit was particularly useful for identifying security problems such as insecure temporary-file creation, shell/subprocess usage, and weak random-number generation. Pylint was also useful because it identified several code-quality problems and provided an overall quality score.

## 3. How did the tools improve your code?

The tools encouraged me to use clearer names, add documentation, avoid mutable default arguments, handle specific exceptions, use safer temporary-file handling, use secure random-number generation, and follow consistent Python formatting.

## 4. How would you use static analysis in a larger project?

In a larger software project, I would run Pylint, Bandit, and Flake8 automatically as part of the development and CI/CD process. Code could be checked before merging changes so that quality, security, and style problems are detected early.