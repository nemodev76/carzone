
from django.shortcuts import redirect # type: ignore
from django.contrib import messages # type: ignore
from django.core.mail import send_mail # type: ignore
from django.contrib.auth.models import User # type: ignore
from .forms import ContactForm  # Assuming you create this form
from .models import Contact
import logging

# Set up logging
logger = logging.getLogger('myapp')

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                user_id = 0
                # product_id = request.POST['product_id']
                product_id = form.cleaned_data['product_id']
                # product_id = request.POST.get('product_id')
                # email = request.user.email
                email = form.cleaned_data['email']
                # email = request.POST.get('email')

                if request.user.is_authenticated:
                    user_id = request.user.id
                    has_contacted = Contact.objects.filter(user_id=user_id, product_id=product_id, email=email).exists()

                    if has_contacted:
                        messages.error(request, 'You have already submitted an inquiry about this car. Please wait for our reponse within 3 business days.')
                        return redirect(f"/cars/id={product_id}")
                
                admin_info = User.objects.get(is_superuser=True)
                admin_email = admin_info.email

                # Log the email variable to verify its value
                logger.debug(f"Email used for sending: {email}")
                logger.debug(f"Admin email: {admin_email}")

                send_mail(
                    "New car inquiry",
                    f"You have a new inquiry for the car {form.data['title']}. Please login to your admin panel for more info.",
                    'ranad81@outlook.com',
                    [admin_email],
                    fail_silently=False,
                )

                contact = form.save(commit=False)
                contact.user_id = user_id
                form.save()

                messages.success(request, 'Your message has been submitted. We will get back to you shortly.')
                
                return redirect(f"/cars/id={contact.product_id}")
            except Exception as e:
                messages.error(request, f'Unable to submit data! Error: {e}')
        else:
            messages.error(request, 'Invalid form data!')

    return redirect('home')  # Adjust as necessary
