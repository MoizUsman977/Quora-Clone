from cloudinary.forms import CloudinaryFileField
from django import forms
from topics.models import Topic

class TopicForm(forms.ModelForm):
    topic_pictures = CloudinaryFileField(required=False)

    class Meta:
        model = Topic
        fields = ["title", "description", "topic_pictures"]
    
    def save(self, commit=True):
        topic = super().save(commit=False)
        topic_pictures = self.cleaned_data.get("topic_pictures")
        if topic_pictures:
            topic.topic_pictures = topic_pictures
            topic.save() 
        return topic   
    