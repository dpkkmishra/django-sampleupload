from django.shortcuts import render
from models import Post,Story
from django.http import HttpResponse

# Create your views here.
def home(req):
	return render(req, "index.html")

def create_post(request):
	post_id = request.POST.get('post_id') 
	title = request.POST.get('title')

	desc = request.POST.get('desc')
	postTitle = request.POST.get(post_id) 
	storyTitle = request.POST.get('storyTitle')
	storyDesc = request.POST.get('storyDesc')

 	
	post = Post()
	story = Story()

#	postTitle = 

	post.title = title
	post.desc = desc
	post.save()

	story.storyTitle = storyTitle
	story.storyDesc = storyDesc
	story.save()
	return HttpResponse(title + " "  +desc+" "+storyTitle+" "+ storyDesc)