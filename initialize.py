"""Initialize the context for templating."""

from datetime import date
import subprocess
from pytemplator.utils import Question as Q, Context

def generate_context():
    """Generate context."""

    context = Context()
    try:
        default_author_name = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True).stdout.strip()
    except FileNotFoundError:
        default_author_name = None
    try:
        default_author_email = subprocess.run(["git", "config", "user.email"], capture_output=True, text=True).stdout.strip()
    except FileNotFoundError:
        default_author_email = None

    context.questions = [
        Q("pypi_name", ask="Name of the package on Pypi"),
        Q("module_name", ask=False, default=lambda: context["pypi_name"].replace("-","_").lower()),
        Q("title", default=lambda: context["pypi_name"].replace("-"," ").title()),
        Q("description"),
        Q("author_name", default=default_author_name),
        Q("author_email", default=default_author_email),
        Q("year", default=date.today().year, ask=False),
    ]
    context.resolve()
    return context.as_dict()
