from django.db import models

class Reviews(models.Model):
    reviewId = models.BigAutoField(primary_key=True)
    storeId = models.ForeignKey('restaurants_app.Restaurant',related_name='restaurant_reviews', on_delete=models.CASCADE)
    userId = models.ForeignKey('user_app.CustomUser',related_name='user_reviews', on_delete=models.CASCADE)
    menuId = models.ForeignKey('restaurants_app.Menu',related_name='menu_reviews', on_delete=models.SET_NULL, null=True, blank=True)
    orderId = models.ForeignKey('orders_app.Order',related_name='order_reviews',on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.CharField(max_length=255, blank=True, null=True)
    reviewPictureUrl = models.TextField(blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default='일반')

    def __str__(self):
        return f"Review ID: {self.reviewId} - Restaurant: {self.storeId} - User: {self.userId}"

class CEOReviews(models.Model):
    ceoReviewId = models.BigAutoField(primary_key=True)
    reviewId = models.ForeignKey(Reviews,related_name='review',on_delete=models.CASCADE)
    content = models.CharField(max_length=255,blank=True,null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default='일반')

    def __str__(self):
        return f"CEOReview Id: {self.ceoReviewId} - review Id: {self.reviewId}"