import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Passing data to the function via route parameter
# Example: http://localhost:7071/api/parameter_by_route/Markus


@app.route(route="parameter_by_route/{name}")
def parameter_by_route(req: func.HttpRequest) -> func.HttpResponse:

    # Get the value of the route parameter
    name = req.route_params.get('name')

    # Check if the parameter is a number or a string
    if name.isdigit():
        number = int(name)
        info = f"The function 'parameter_by_route' was called with the numeric parameter: {number}"
    else:
        info = f"The function 'parameter_by_route' was called with the string parameter: {name}"

    logging.info(info)

    # a http triggered function always returns a http-response
    return func.HttpResponse(info)


# Passing data to the function via query parameter
# Example http://localhost:7071/api/parameter_by_query?name=Markus
@app.route(route="parameter_by_query")
def parameter_by_query(req: func.HttpRequest) -> func.HttpResponse:

    # Get the value of the query parameter
    name = req.params.get('name')

    info = f"The function 'parameter_by_query' was called with the parameter: {name}"

    logging.info(info)

    # a http triggered function always returns a http-response
    return func.HttpResponse(info)


# Passing data to the function via message body
# Example POST http://localhost:7071/api/parameter_by_body
# Body: {"name": "Leon", "age": 18}
@app.route(route="parameter_by_body", methods=["POST"])
def parameter_by_body(req: func.HttpRequest) -> func.HttpResponse:

    # Get the value of the parameter out of the message body
    req_body = req.get_json()
    name = req_body.get('name')
    age = req_body.get('age')

    info = f"The function 'parameter_by_query' was called with the string parameter: {name} and the numeric parameter: {age}"

    logging.info(info)

    # a http triggered function always returns a http-response
    return func.HttpResponse(info)
