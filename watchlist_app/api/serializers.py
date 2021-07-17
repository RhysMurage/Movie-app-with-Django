from rest_framework import serializers
from watchlist_app.models import StreamPlatform, WatchList, Review

class ReviewSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Review
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True) # read only as the review can only be added from the serializer above

    class Meta:
        model = WatchList
        fields = '__all__'

# streaming platform can have many movies
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True) #should be the same as the related_name in models
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'




# def name_length(value):
#     if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#     else:
#         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self,data): #object validation
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and Description should be different!')
#         else:
#             return data

    # field validation 
    # def name_length(value):
    #     if len(value) < 2:
    #             raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
    
