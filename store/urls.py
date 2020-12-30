from django.urls import path
from . import views
from store.views import category,store,product,updateItem,updateab,processOrder

urlpatterns=[
    path('',views.store,name="store"),
    path('cart/',views.cart, name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('products/', views.product, name="product"),
    # path(r'^(?P<category_slug>[-\w]+)/$',
    #     views.product_list,
    #     name='product_list_by_category'),
    path('categories/<str:title>',views.category,name="category"),
    path('abstract/', views.abstract, name="abstract"),
    path('surrealism/', views.surrealism, name="surrealism"),
    path('contemporary/', views.contemporary, name="contemporary"),
    path('impressionism/', views.impressionism, name="impressionism"),
    path('cubism/', views.cubism, name="cubism"),       
    path('modern/', views.modern, name="modern"),
    path('update_item/',views.updateItem,name="update_item"),
    path('update_itemab/',views.updateab,name="update_itemab"),
    path('process_order/',views.processOrder,name="process_order"),

    
    # path('update_item/',views.updateItem2,name="update_item"),

    ]
