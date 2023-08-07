from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer

"""
    1.get product list
    2.get a product
    3.create a product
"""

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # create an item
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        content = serializer.validated_data.get("content") or None
        if content == None:
            content = 'This is a default content'
        serializer.save(content=content)
    
product_mixin_view = ProductMixinView.as_view()

"""
    update a product
"""
class ProductUpdateAPIView(
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.title:
            instance.title = instance.content

product_update_api_view = ProductUpdateAPIView.as_view()


"""
    delete a product
"""
class ProductDeleteAPIView(
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

product_delete_api_view = ProductDeleteAPIView.as_view()