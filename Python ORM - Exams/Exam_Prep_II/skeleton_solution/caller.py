import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Product, Profile, Order


def get_profiles(search_string=None):
    if search_string is None:
        return ''

    profiles = (Profile.objects
                .annotate(orders_count=Count('orders'))
                .filter(Q(full_name__icontains=search_string)
                        |
                        Q(phone_number__icontains=search_string)
                        |
                        Q(email__icontains=search_string))
                .order_by('full_name')
                )

    if not profiles:
        return ''

    result = []

    for p in profiles:
        result.append(f"Profile: {p.full_name}, "
                      f"email: {p.email}, phone number: {p.phone_number}, orders: {p.orders_count}")

    return '\n'.join(result)

# print(get_profiles('pro'))


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ''

    result = []

    for p in profiles:
        result.append(f"Profile: {p.full_name}, orders: {p.orders_count}")

    return '\n'.join(result)

# print(get_loyal_profiles())


def get_last_sold_products():
    last_order = (Order.objects
                  .prefetch_related('products')
                  .annotate(products_count=Count('products'))
                  .filter(products_count__gt=0)
                  .order_by('creation_date')
                  .last()
                  )

    if not last_order:
        return ''

    products_names = [p.name for p in last_order.products.all().order_by('name')]

    return f"Last sold products: {', '.join(products_names)}"


# print(get_last_sold_products())

def get_top_products():
    products = (Product.objects
                .annotate(orders_count=Count('orders'))
                .filter(orders_count__gt=0)
                .order_by('-orders_count', 'name')
                )[:5]

    if not products:
        return ''

    result = ['Top products:']

    for p in products:
        result.append(f"{p.name}, sold {p.orders_count} times")

    return '\n'.join(result)

# print(get_top_products())


def apply_discounts():
    orders = (Order.objects
              .annotate(products_count=Count('products'))
              .filter(products_count__gt=2, is_completed=False)
              .update(total_price=F('total_price') * 0.9)
              )

    return f"Discount applied to {orders} orders."

# print(apply_discounts())


def complete_order():
    order = (Order.objects
             .prefetch_related('products')
             .filter(is_completed=False)
             .order_by('creation_date')
             .first()
             )

    if not order:
        return ''

    for p in order.products.all():
        p.in_stock -= 1

        if p.in_stock == 0:
            p.is_available = False

        p.save()

    order.is_completed = True
    order.save()

    return "Order has been completed!"


# print(complete_order())