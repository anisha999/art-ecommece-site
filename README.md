Online Art Gallery 

An online art gallery, with both physical and digital prints, integrated with a chatbot and paypal(for payments)

FEATURES:
Browse through all products
Browse through different categories
Add products to cart
Delete products from cart
Buy digital prints
Chatbot to answer different queries
Payment thrpugh paypal as well as debit card
Guest user accessibility

FILES:

Name of the application: store


models.py - Contains models for customer, the different categories, orders, order items and the shipping address.
urls.py - Contains all url paths.
views.py - Contains the view functions for adding products to the cart, the checkout process, updating items in the cart as well as processing the order.
utils.py- Contains the functions that take care of the guest session. Has a function for storing cookies, and processing the guest order 
admin.py- To register the different models

Templates:
Contains all the html files. Includes:
-templates for the various categories.
-main.html : for the homepage. all other files use main.html as an extension.
-checkout.html : checkout page with the shipping address and payment section
-cart.html: consists of the various items in the cart along with the price and the quantity. Displays the total (in USD) and the total number of items in the cart.
-store.html: layout for the homepage

STATIC FILES:

main.css - Contains all the css files for styling the website.
cart.js - Contains all the JavaScript files for updating order in the cart and adding cookies.
img - Holds all images and icons.


Justification:


This project is distinct from all previous projects so far because it is user accessible, to both, a guest user as well as a logged in user,with the help of cookies. 
It automatically updates the cart icon as you add/delete products.
It has a chatbot integrated into the website that answers the users query and provides links to the various categories as well. 
It is mobile responsive.
Provides both digital prints (that in turn doesn't require shipping details) and physical art prints.
Has paypal integrated for users comfortable with using paypal as well as debitc card payment
