# Static Code Analysis Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Insecure shell/subprocess usage | Bandit - High | `pingHub()` | The code used `subprocess.check_output()` with `shell=True`, which can create command-injection security risks. | Removed the unused subprocess-based helper and subprocess import. |
| Insecure temporary file creation | Bandit - Medium | `labelPath()` | The code used `tempfile.mktemp()`, which can create a predictable temporary filename. | Replaced it with `tempfile.NamedTemporaryFile()` with `delete=False`. |
| Mutable default argument | Pylint | `bookParcel()` | Using `history=[]` as a default argument can cause the same list to be shared between function calls. | Changed the default to `None` and initialized the list inside the function. |
| Broad exception handling | Pylint | `trackParcel()` | `except Exception` catches unrelated errors and can hide programming problems. | Changed it to `except KeyError` because a missing tracking ID raises `KeyError`. |
| Missing documentation | Pylint | Module and functions | The module and functions did not have documentation strings. | Added module and function docstrings. |
| Non-standard naming | Pylint | Multiple lines | Names such as `bookParcel`, `trackingId`, and `weightKg` did not follow Python naming conventions. | Renamed functions and variables using `snake_case`. |
| Weak random number generation | Bandit - Low | OTP generation | `random.randint()` is not appropriate for security-sensitive OTP generation. | Replaced it with `secrets.randbelow()`. |
| Formatting violations | Flake8 | Multiple lines | The original code contained whitespace, comment-spacing, comma-spacing, and blank-line violations. | Corrected the formatting according to Flake8 conventions. |