import invoke

export_command = "poetry export -f requirements.txt --output requirements.txt --without-hashes"

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