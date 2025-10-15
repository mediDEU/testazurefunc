import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Echo function that returns the received message.
    
    Args:
        req: HTTP request object
        
    Returns:
        HTTP response with echoed message
    """
    logging.info('Python HTTP trigger function processed a request.')

    # Try to get the message from query parameter
    message = req.params.get('message')
    
    # If not in query params, try to get it from request body
    if not message:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            message = req_body.get('message')

    if message:
        return func.HttpResponse(
            f"Echo: {message}",
            status_code=200
        )
    else:
        return func.HttpResponse(
            "Please pass a message in the query string or in the request body",
            status_code=400
        )
