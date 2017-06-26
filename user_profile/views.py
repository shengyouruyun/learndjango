from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from django.shortcuts import render
from django.template import Context
from django.template.loader import render_to_string
from user_profile.forms import InvitationForm
from django.core.mail import EmailMultiAlternatives
from user_profile.models import Invitation, User
from django.http import HttpResponseRedirect
import hashlib
class Invite(View):

	def get(self, request):

		params = dict()
		success = request.GET.get('success')
		email = request.GET.get('email')
		invite = InvitationForm()
		params["invite"] = invite
		params['success'] = success
		params['email'] = email
		return render(request, 'invite.html', params)

	def post(self, request):
		form = InvitationForm(self.request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			subject = "Invitation to join MyTweet"
			sender_name = request.session["username"]
			print sender_name
			sender_email = 'wangshenganlu1990@126.com'
			invite_code = Invite.generate_invite_code(email)
			link = 'http://%s/invite/accept/%s/' % (settings.SITE_HOST, invite_code)
			context = Context({"sender_name":sender_name, 
				"sender_email":sender_email, "email":email, "link":link})

			invite_email_template = render_to_string('partials/twsearch.html', context)
			msg = EmailMultiAlternatives(subject, invite_email_template, settings.EMAIL_HOST_USER,
				[email], cc=[settings.EMAIL_HOST_USER])

			user = User.objects.get(username=sender_name)
			invitation = Invitation()
			invitation.email = email
			invitation.code = invite_code
			invitation.sender = user 
			invitation.save()
			success = msg.send()
			return HttpResponseRedirect('invite?success='+str(success)+'&email='+'email')
	@staticmethod
	def generate_invite_code(email):
		secret = settings.SECRET_KEY
		if isinstance(email, unicode):
			email = email.encode('utf-8')
			activation_key = hashlib.sha1(secret+email).hexdigest()
			return activation_key



	




	











