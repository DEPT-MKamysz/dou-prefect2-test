from prefect import task, flow

@task
def print_hello(name):
    print(f"Hello {name}!")

@flow(name = "Hello Flow"):
def hello_world(name = "World"):
    print_hello(name)