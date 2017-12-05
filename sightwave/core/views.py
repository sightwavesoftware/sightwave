from django.shortcuts import render


def home(request):
    """Provide Home Page
        Args:
            request: request
        Returns:
            response page with links rendered to template
    """

    return render(request, "core/base.html")
