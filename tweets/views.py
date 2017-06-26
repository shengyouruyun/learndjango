from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Tweet, HashTag
from user_profile.models import User, UserFollowers
from django.views.generic import View
from django.shortcuts import render
from tweets.form import TweetForm, SearchForm
from django.template.loader import render_to_string
from django.template import Context
import json

# Create your views here.
# def index(request):
# 	if request.method == 'GET':
# 		return HttpResponse('I am called from a get Request')
# 	elif request.method == 'POST':
# 		return HttpResponse('I am called from a post Request')


class Index(View):
	def get(self, request):
		params = {}
		params['name'] = "Django"
		return render(request, 'base.html', params)
	
	def post(self, request):
		return HttpResponse('I am called from a post Request')

class Profile(View):
	""" User Profile page reachable from /user/<username> URL"""
	#form = TweetForm()
	def get(self, request, username):

		user = request.GET.get('username')
		form = TweetForm()
		params = dict()
		userProfile = User.objects.get(username=username)
		print userProfile

		userFollower = UserFollowers.objects.get(user=userProfile)
		if userFollower.followers.filter(username=request.user.username).exists():
			params['following'] = True
		else:
			params['following'] = False
			form = TweetForm(initial={'country':'Global'})
		search_form = SearchForm()
		tweets = Tweet.objects.filter(user=userProfile).order_by('create_date')

		params['tweets'] = tweets
		params['profile'] = userProfile 
		params['form'] = form
		#params['search'] = search_form
		return render(request, 'user_profile.html', params)
	def post(self, request, username):
		follow = request.POST['following']
		print follow 
		user = User.objects.get(username=request.user.username)
		userProfile = User.objects.get(username=username)
		userFollower, status = UserFollower.objects.get_or_create(user=userProfile)
		if follow == 'true':
			userFollower.followers.add(user)
		else:
			userFollower.followers.remove(user)
		return HttpResponse(json.dumps(""), content_type='application/json')








class PostTweet(View):
	"""Tweet Post form available on page /user/<username> URL"""
	def post(self, request, username):
		params = self.request.POST
		form = TweetForm(params)
		if form.is_valid:
			user = User.objects.get(username=username)
			tweet = Tweet(text=params.get('text'), user=user,
							country=params.get('country'))
			tweet.save()
		words = params.get('text').split(" ")
		for word in words:
			if word[0] == "#":
				hashtag, created = HashTag.objects.get_or_create(name=word[1:])
				hashtag.tweet.add(tweet)
		return HttpResponseRedirect('/user/'+username)

class HashTagCloud(View):
	
	def get(self, request, hashtag):

		params = dict()
		hashtag = HashTag.objects.get(name=hashtag)
		params["tweets"] = hashtag.tweet
		return render(request, 'hashtag.html', params)
		
class Search(View):
	"""Search all tweets with query /search/?query=<query> URL"""
	def get(self,request):
		form = SearchForm()
		params = dict()
		params["search"] = form
		return render(request, 'search.html', params)
	def post(self, request):
		params = self.request.POST
		#print params

		form = SearchForm(params)
		if form.is_valid:
			query = params.get('query')

			tweets = Tweet.objects.filter(text__icontains=query)
			print query
			
		 	context = Context({"query":query, "tweets":tweets})
		 	print context
		 	
		 	return_str = render_to_string('partials/twsearch.html', context)

			return HttpResponse(json.dumps(return_str), content_type="application/json")
		else:
			return HttpResponseRedirect('/search')

class UserRedirect(View):
	
	def post(self, request):

		params = self.request.POST

		return HttpResponseRedirect('/user/'+ params['username'])

class MostFollowedUsers(View):
	def get(self, request):
		userFollowers = UserFollower.objects.order_by('count')
		params = dict()
		params['userFollowers'] = userFollowers

		return render(request, 'users.html', params)


from django.core.mail import send_mail

class TestEmail(View):
	def get(self, request):
		email_title = 'how'
		email_body = 'you doing'
		email = '1479779020@qq.com' 
		send_status = send_mail(email_title, email_body,'wangshenganlu1990@126.com', [email])
		if send_status:
			print u'it works'

		return HttpResponse("Status Code: %d" % send_status)