from prefect import task, flow, get_run_logger

@task
def print_hello(name):
    return f"Hello {name}!"

@flow(name = "Hello Flow")
def hello_world(name = "World"):
    logger = get_run_logger()
    logger.info(print_hello(name))