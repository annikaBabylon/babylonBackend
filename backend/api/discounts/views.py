from rest_framework import generics, mixins
from .models import Discount
from .serializers import DiscountSerializer

"""
    1.get Discount list
    2.get a Discount
    3.create a Discount
"""

class DiscountMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
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
        content = serializer.validated_data.get("content") or None
        if content == None:
            content = 'This is a default content'
        serializer.save(content=content)
    
discount_mixin_view = DiscountMixinView.as_view()

"""
    update a Discount
"""
class DiscountUpdateAPIView(
    generics.UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.title:
            instance.title = instance.content

discount_update_api_view = DiscountUpdateAPIView.as_view()


"""
    delete a Discount
"""
class DiscountDeleteAPIView(
    generics.DestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

discount_delete_api_view = DiscountDeleteAPIView.as_view()