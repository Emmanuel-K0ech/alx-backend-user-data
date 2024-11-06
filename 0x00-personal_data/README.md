# 0x00. Personal Data

## Resources
Read or watch the following resources to gain a solid understanding of personal data and logging practices:

- [What Is PII, non-PII, and Personal Data?](#)
- [Logging Documentation](#)
- [bcrypt Package](#)
- [Logging to Files, Setting Levels, and Formatting](#)

## Learning Objectives
By the end of this project, you should be able to:

1. Identify examples of Personally Identifiable Information (PII).
2. Implement a log filter that obfuscates PII fields.
3. Encrypt passwords and verify the validity of input passwords.
4. Authenticate to a database using environment variables.

## Requirements
- **Environment**: All files should be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- **Formatting**: Each file should end with a new line.
- **Shebang**: The first line of all files must be `#!/usr/bin/env python3`.
- **Documentation**:
  - A `README.md` file at the project root is mandatory.
  - Code should follow the `pycodestyle` style (version 2.5).
  - Each module, class, and function should have proper documentation.
    - **Modules**: Documented with purpose (use `python3 -c 'print(__import__("my_module").__doc__)'`).
    - **Classes**: Documented with purpose (use `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
    - **Functions**: Documented with purpose both inside and outside of classes (use `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
    - Documentation should be meaningful, explaining the purpose of each module, class, or method.
- **Executability**: All files must be executable.
- **File Length**: The length of your files will be tested using `wc`.
- **Type Annotations**: All functions must include type annotations.

---

This project will help you understand best practices in managing sensitive data, particularly for logging and securing PII data within Python applications.
