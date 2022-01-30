"""Initialize the context for templating."""

from datetime import date

import subprocess

from pytemplator.exceptions import InvalidInputError
from pytemplator.utils import cd, Question as Q, Context

def generate_context(no_input, *args, **kwargs):
    """Generate context."""

    context = Context()
    try:
        default_author_name = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True).stdout.strip()
    except subprocess.CalledProcessError:
        default_author_name = None
    try:
        default_author_email = subprocess.run(["git", "config", "user.email"], capture_output=True, text=True).stdout.strip()
    except subprocess.CalledProcessError:
        default_author_email = None
    try:
        default_git_url = subprocess.run(["git", "config", "remote.origin.url"], capture_output=True, text=True).stdout.strip()
        default_git_url = default_git_url.replace("git@github.com:", "https://github.com/")
    except subprocess.CalledProcessError:
        default_git_url = None

    if not default_git_url:
        git_question = Q(
            "git_url",
            ask="URL of the remote Git repo where this project has been initialised: "
        )
        git_question.resolve(no_input)
        try:
            subprocess.run(["git", "clone", git_question.answer], check=True)
        except subprocess.CalledProcessError as error:
            raise InvalidInputError from error
    else:
        git_question = Q("git_url", ask=False, default=default_git_url)

    context.questions = [
        git_question,
        Q("pypi_name", ask="Name of the package on Pypi: "),
        Q("module_name", ask=False, default=lambda: context["pypi_name"].replace("-","_").lower()),
        Q("title", default=lambda: context["pypi_name"].replace("-"," ").title()),
        Q("description"),
        Q("author_name", default=default_author_name),
        Q("author_email", default=default_author_email),
        Q("year", default=date.today().year, ask=False),
    ]
    context.resolve(no_input)
    return context.as_dict()
