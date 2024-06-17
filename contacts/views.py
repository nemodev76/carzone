

from django.shortcuts import redirect # type: ignore
from django.contrib import messages
from .forms import ContactForm  # Assuming you create this form
from .models import Contact

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                if request.user.is_authenticated:
                    user_id = request.user.id
                    # product_id = form.cleaned_data['product_id']
                    product_id = form.data['product_id']
                    # product_id = request.POST.get('product_id')
                    email = form.cleaned_data['email']

                    has_contacted = Contact.objects.filter(user_id=user_id, product_id=product_id, email=email).exists()

                    if has_contacted:
                        messages.error(request, 'You have already submitted an inquiry about this car. Please wait for our reponse within 3 business days.')
                        return redirect(f"/cars/id={product_id}")
                    
                contact = form.save()
                messages.success(request, 'Your message has been submitted. We will get back to you shortly.')
                return redirect(f"/cars/id={contact.product_id}")
            except Exception as e:
                messages.error(request, f'Unable to submit data! Error: {e}')
        else:
            messages.error(request, 'Invalid form data!')

    return redirect('home')  # Adjust as necessary
