
# Create your views here.
from django.shortcuts import render
from .forms import InquiryForm
import requests



def inquiry_create(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Create an instance of the InquiryForm with the POST data
        form = InquiryForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Create a new inquiry object with the form data, but do not save it to the database yet
            inquiry = form.save(commit=False)
            
            # Set the source_webpage field of the inquiry to the value of the 'HTTP_REFERER' header from the request
            inquiry.source_webpage = request.META.get('HTTP_REFERER', '')
            
            # Set the source_ip field of the inquiry to the client IP address of the request
            inquiry.source_ip = get_client_ip(request)
            
            # Set the country_from_ip field of the inquiry to the country code obtained from the client IP address
            inquiry.country_from_ip = get_country_from_ip(inquiry.source_ip)
            
            # Save the inquiry object to the database
            inquiry.save()
            
            # Render the 'indicator-submitted.html' template
            return render(request,'form_handlers/indicator-submitted.html')
    
    else:
        # If the request method is not POST, create a new instance of the InquiryForm
        form = InquiryForm()
    
    # Render the 'indicator-submitted.html' template with the form object
    return render(request, 'form_handlers/indicator-submitted.html', {'form': form})

# ... other functions ...



def get_client_ip(request):
    """
    Get the client IP address from the request object.

    Args:
        request (HttpRequest): The request object.

    Returns:
        str: The client IP address.
    """
    # Check if the 'X-Forwarded-For' header is present in the request
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    # If the 'X-Forwarded-For' header is present, extract the first IP address
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        # Otherwise, fallback to the 'REMOTE_ADDR' header for the IP address
        ip = request.META.get('REMOTE_ADDR')

    # Return the client IP address
    return ip


def get_country_from_ip(ip):
    try:
        response = requests.get(f"https://freegeoip.app/json/{ip}",timeout=10)
        data = response.json()
        return data.get('country_name', '')
    except Exception as e:
        return ''

