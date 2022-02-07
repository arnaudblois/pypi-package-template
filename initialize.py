"""Initialize the context for templating."""

from datetime import date

from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory

from pytemplator import __version__ as PYTEMPLATOR_VERSION
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
            ask="URL of the remote Git repo where this new package has been initialised: "
        )
        git_question.resolve(no_input)
        git_project_name = git_question.answer.split("/")[-1]
        try:
            with TemporaryDirectory() as tempdir:
                tempdir = Path(tempdir)
                with cd(tempdir):
                    subprocess.run(["git", "clone", git_question.answer], check=True)
                shutil.copytree(tempdir / git_project_name, Path.cwd(), dirs_exist_ok=True)
        except subprocess.CalledProcessError as error:
            raise InvalidInputError from error
    else:
        git_question = Q("git_url", ask=False, default=default_git_url)
        git_project_name = default_git_url.split("/")[-1].replace(".git", "")

    licenses = ["AGPL", "APACHE", "BOOST", "GPL", "LGPL", "MIT", "MOZILLA", "UNLICENSE"]

    context.questions = [
        git_question,
        Q("pypi_name", ask="Name of the package on Pypi", default=lambda: git_project_name.replace("_","-").lower()),
        Q("module_name", ask=False, default=lambda: context["pypi_name"].replace("-","_").lower()),
        Q("title", default=lambda: context["pypi_name"].replace("-"," ").title()),
        Q("description"),
        Q("license", ask="Please choose your license\nValid choices:" + "  - ".join(licenses) + "\nPlease select", default="MIT"),
        Q("author_name", default=default_author_name),
        Q("author_email", default=default_author_email),
        Q("year", default=date.today().year, ask=False),
        Q("pytemplator_version", default=PYTEMPLATOR_VERSION, ask=False)
    ]
    context.resolve(no_input)
    return context.as_dict()
