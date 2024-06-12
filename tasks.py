import os

import invoke

export_command = (
    "poetry export -f requirements.txt --output requirements.txt --without-hashes"
)


def _export(c):
    c.run(export_command)


@invoke.task
def install(c):
    c.run("poetry install")


@invoke.task
def add(c, package, args=""):
    c.run(f"poetry add {package} {args}")
    _export(c)


@invoke.task
def export(c):
    _export(c)


@invoke.task
def dev(c, port=8000):
    c.run(f"uvicorn src.main:app --host 0.0.0.0 --port {port} --reload")


@invoke.task
def web(c, port=3000):
    os.chdir("interfaces/moisture-one-web")
    c.run(f"npm run start -- --port {port}")


@invoke.task
def current(c, config="src/alembic.ini"):
    c.run(f"alembic -c {config} current ")


@invoke.task
def makemigrations(c, config="src/alembic.ini", message=""):
    c.run(f"alembic -c {config} revision --autogenerate -m '{message}'")


@invoke.task
def migrate(c, config="src/alembic.ini"):
    c.run(f"alembic -c {config} upgrade head")
