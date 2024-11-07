Django Razorpay Integration
This is a simple Django project that demonstrates how to integrate Razorpay's payment gateway to process payments securely. Users can make payments using Razorpay, and after a successful transaction, they are redirected to a thank-you page.

Features
Razorpay payment gateway integration for secure payments.
Order processing with product ID, quantity, and price.
Payment success page with a progress bar and order details.
Automatic redirection to the homepage after a successful payment.
Minimal design and user-friendly interface for seamless payments.
Tech Stack
Backend: Django
Payment Gateway: Razorpay
Frontend: HTML, CSS
Payment Handling: Razorpay Python SDK
Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.6+
Django 3.x or later
Razorpay Account (for API keys)
pip (Python package manager)
Installation
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/razorpay-django-integration.git
cd razorpay-django-integration
2. Set up a virtual environment (optional but recommended)
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
3. Install required dependencies
bash
Copy code
pip install -r requirements.txt
4. Set up Razorpay API Keys
Create a Razorpay account here.
Get your Key ID and Key Secret from the Razorpay dashboard.
Add the following to your settings.py:
python
Copy code
RAZORPAY_KEY_ID = 'your-razorpay-key-id'
RAZORPAY_KEY_SECRET = 'your-razorpay-key-secret'
5. Apply migrations
bash
Copy code
python manage.py migrate
6. Run the development server
bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to see the payment gateway in action.

How It Works
1. Product Form
Users can fill out a form with:

Product ID
Quantity
Price
2. Initiate Payment
Once the user submits the form, a Razorpay payment request is created and a checkout page is displayed to the user.

3. Payment Success
After the payment is successfully processed, the user is redirected to a success page that:

Shows the order number
Displays a progress bar animation
Redirects to the homepage after 5 seconds.
4. Redirect
After successful payment, the user is automatically redirected to the homepage.

Files and Folders Structure
bash
Copy code
razorpay-django-integration/
│
├── payment_gateway/                # The Django app handling payments
│   ├── templates/
│   │   └── payment_success.html    # Success page after payment
│   ├── views.py                    # Views for payment processing
│   ├── urls.py                     # URL routes for the payment pages
│   ├── models.py                   # (Optional) Models if needed for tracking orders
│   └── forms.py                    # Forms to handle user input
├── manage.py                       # Django project management
├── requirements.txt                # Python dependencies
└── settings.py                     # Django project settings (API keys & other configs)
Testing
You can run tests using Django’s built-in test runner:

bash
Copy code
python manage.py test
Contribution
Feel free to fork this project and make improvements. If you find any bugs or have suggestions, please create an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Created with ❤️ by Dinesh Suthar.