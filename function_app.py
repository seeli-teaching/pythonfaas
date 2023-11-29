import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="parameter_by_route/{name}")
def parameter_by_route(req: func.HttpRequest) -> func.HttpResponse:

    # Get the value of the route parameter
    name = req.route_params.get('name')

    info = f"The function 'parameter_by_route' was called with the parameter: {name}"

    logging.info(info)

    # a http triggered function always returns a http-response
    return func.HttpResponse(info)
