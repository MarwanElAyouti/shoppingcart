# Shopping cart exercise brief

> ⚠ Please read the instructions thoroughly before you begin. Take some time to plan your work and budget **no more than 3 hours** to complete.

This is a partial implementation of a shopping till system, which you might find at a supermarket.
This implementation was started by another developer but the implementation was never completed. You have been tasked with improving and completing this project.
You may make any technical decisions you would like, but must not change the given abstract class (abc.ShoppingCart) which is used by the shopping till hardware and cannot be easily updated.
Please treat this code as an element of a larger production system.

The objectives for this exercise are as follows:
- ~~Make the receipt print items in the order that they were added.~~
- ~~Add a 'Total' line to the receipt. This should be the full price we should charge the customer.~~
- ~~Be able to fetch product prices from an external source (E.g. json file, csv, database).~~
- ~~Be able to display the product prices in different currencies (not only Euro).~~
- ~~Update the test suite to extend coverage and make the tests robust so that changes to the code should rarely require changes to the tests.~~
- Any other changes which improve the reliability of this code in production.
- Any other changes which improve the maintainability of this code for other developers.

If you do not have enough information, make any assumptions you would like and note them down with TODO comments. Feel free to annotate your work with comments that highlight completion of the tasks listed above.

The code should be production ready, clean and tested. Please ensure the code is version controlled. Please make several commits with clear and sensible commit messages while working on this.

When you are ready to submit your completed exercise, please either:
- Provide a Github/GitLab/etc. link that we can view and clone your work; or
- Use git-bundle (https://git-scm.com/docs/git-bundle) to create a bundle file and send this to us.



## Requirements
* Python
  *  v3.8.10 (exact version) using [Pyenv](https://github.com/pyenv/pyenv)

      * `pyenv install 3.8.10`
      * `pyenv versions` to confirm that **3.8.10** is in the list of Python versions
  * Inside the project directory
      * `rm -rf .venv` to remove old environment
      * `pyenv local 3.8.10` to set specific Python version at project level (not OS level)
      * `python --version` to check if it's **3.8.10**. If not, then
          * `echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc` or `~/.bash_profile`
          * `echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc` or `~/.bash_profile`
          * `echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc` or `~/.bash_profile`
      * Re-open shell and `python --version` to check if it's **3.8.10** at project level
* Install [Poetry](https://python-poetry.org/docs/)
  * `curl -sSL https://install.python-poetry.org | python3 -`
  * Inside the project directory
      * `poetry shell` to activate poetry virtual environment
      * `python --version` to confirm that **3.8.10** inside the environment as well

## Setup the development environment
* Confirm you have all system requirements above
* Clone the repository to your local machine
* Download & install dependencies by running `poetry install`

## Working with requirements/dependencies
 - For adding a requirement, you can run: `poetry add {requirement}`
 - For adding a dev requirement, you can run: `poetry add {requirement} --dev`
 - For updating a requirement, you can run: `poetry update {requirement}`
 - For removal of a requirement, you can run: `poetry remove {requirement}`

## Run lint & format
- `isort .` - sort package imports
- `black .` - format the code
## Testing
- `pytest -v` - test all directories
- `pytest {path to specific test file}`