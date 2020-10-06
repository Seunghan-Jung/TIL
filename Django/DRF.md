# DRF

DRF(**D**jango **R**est **F**ramework)란 Django 안에서 RESTful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈 소스 라이브러리이다.

## nested serializers

```python
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content')
        

class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
```

