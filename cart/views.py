from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView, RetrieveAPIView,UpdateAPIView
from .serializers import CartItemSerializer,CartSerializer,IncreseDecreseQuantity
from django.shortcuts import get_object_or_404
from .models import CartItem, Cart
from product.models import ProductItem
from rest_framework.response import Response
from rest_framework import status

class AddToCartView(CreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        cart = get_object_or_404(Cart, user=user)
        product_item_id = self.request.data.get('product_item')
        product_item_obj = get_object_or_404(ProductItem, pk=product_item_id)

        # Check if the cart item already exists
        cart_item = CartItem.objects.filter(cart=cart, product_item=product_item_obj).first()

        # Get the quantity to add, default to 1 if quantity is not provided or blank
        quantity_to_add = self.request.data.get('quantity', 1)
        if quantity_to_add in [None, '']:
            quantity_to_add = 1
        else:
            quantity_to_add = int(quantity_to_add)

        if cart_item:
            # If it exists, update the quantity
            cart_item.quantity += quantity_to_add
            cart_item.save()
            serializer.instance = cart_item
        else:
            # If it does not exist, create a new cart item
            cart_item = CartItem.objects.create(
                cart=cart,
                product_item=product_item_obj,
                quantity=quantity_to_add
            )
            serializer.instance = cart_item

        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)


class CartView(RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        user = self.request.user
        cart = get_object_or_404(Cart, user=user)
        return cart


class IncreaseQuantity(UpdateAPIView):
    serializer_class = IncreseDecreseQuantity

    def get_object(self):
        kwargs = {
            "pk": self.kwargs.get("pk", None)
        }
        cart_item = get_object_or_404(CartItem, **kwargs)
        return cart_item

    def perform_update(self, serializer):
        cart_item = self.get_object()
        cart_item.quantity += 1
        cart_item.save()
        
        serializer.instance = cart_item
        serializer.save()


class DecreaseQuantity(UpdateAPIView):
    serializer_class = IncreseDecreseQuantity

    def get_object(self):
        kwargs = {
            "pk": self.kwargs.get("pk", None)
        }
        cart_item = get_object_or_404(CartItem, **kwargs)
        return cart_item

    def perform_update(self, serializer):
        cart_item = self.get_object()
        cart_item.quantity -= 1

        if cart_item.quantity <= 0:
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            cart_item.save()
            serializer.instance = cart_item
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)