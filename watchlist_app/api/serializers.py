from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()


    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['name','description','id']
        # exclude = ['name']
    
    def get_len_name(self, object):
        length = len(object.name)
        return length

    def validate(self,data): #object validation
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and Description should be different!')
        else:
            return data

    # field validation 
    def name_length(value):
        if len(value) < 2:
                raise serializers.ValidationError("Name is too short")
        else:
            return value



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
    
