import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Get the request body
    try:
        req_body = req.get_json()
    except ValueError:
        req_body = None

    # Get query parameters
    name = req.params.get('name')
    message = req.params.get('message')

    # Echo back the request data
    if req_body:
        echo_data = {
            "echo": req_body,
            "message": "Request body echoed successfully"
        }
        return func.HttpResponse(
            body=str(echo_data),
            status_code=200,
            mimetype="application/json"
        )
    elif name or message:
        response_text = f"Echo: name={name}, message={message}"
        return func.HttpResponse(response_text, status_code=200)
    else:
        return func.HttpResponse(
            "Please pass data in the request body or use query parameters (name, message)",
            status_code=400
        )
