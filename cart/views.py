from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView, RetrieveAPIView,UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from .serializers import CartItemSerializer,CartSerializer,IncreaseDecreaseQuantity, CouponSerializer, CouponCodeSerializer
from django.shortcuts import get_object_or_404
from .models import CartItem, Cart, Coupon
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



class IncreaseQuantity(APIView):

    def post(self, request, *args, **kwargs):
        cart_item_id = self.kwargs.get("pk")
        cart_item = get_object_or_404(CartItem, pk=cart_item_id)
        
        cart_item.quantity += 1
        cart_item.save()
        return Response({"message": "Quantity increased", "quantity": cart_item.quantity}, status=status.HTTP_200_OK)


class DecreaseQuantity(APIView):

    def post(self, request, *args, **kwargs):
        cart_item_id = self.kwargs.get("pk")
        cart_item = get_object_or_404(CartItem, pk=cart_item_id)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            return Response({"message": "Quantity decreased", "quantity": cart_item.quantity}, status=status.HTTP_200_OK)
        else:
            cart_item.delete()
            return Response({"message": "Cart item deleted because quantity reached 0"}, status=status.HTTP_204_NO_CONTENT)


class CartView(RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        user = self.request.user
        cart = get_object_or_404(Cart, user=user)
        return cart


class RemoveCartItemView(APIView):

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        cart_item_id = self.kwargs.get('pk')
        cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=user)
        cart_item.delete()
        return Response({"message": "Cart item removed successfully"}, status=status.HTTP_204_NO_CONTENT)


class DeleteCartView(APIView):

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        cart = get_object_or_404(Cart, user=user)
        CartItem.objects.filter(cart=cart).delete()
        cart.coupon = None
        cart.update_total()
        return Response({"message": "Cart deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class CouponListCreateView(ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class ApplyCouponView(UpdateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def get_object(self):
        return Cart.objects.get(user=self.request.user)

   