from django.shortcuts import render_to_response


def handler404(request, exception, template_name="404_error.html"):
    """
    View that displayes the 404 error page
    """
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, exception, template_name="500_error.html"):
    """
    View that displayes the 500 error page
    """
    response = render_to_response(template_name)
    response.status_code = 500
    return response
