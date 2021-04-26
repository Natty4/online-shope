from django.shortcuts import render, get_object_or_404,redirect
from .models import Profile, User
from .forms import UserRegistrationForm,ProfileEditForm,UserEditForm,VerifyForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.conf import settings
from django.urls import reverse
from twilio.rest import Client




def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Create a new user object but avoid saving it 
			new_user = user_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.is_active = False
			new_user.save()
			#save pk on session to use later in 2nd stape of verification
			request.session['pk'] = new_user.pk
			# Create the user profile
			Profile.objects.create(user=new_user)
			return redirect(reverse('verify_me'),{'new_user':new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'account/register.html', {'user_form': user_form})

def verify_view(request):
	verify_form = VerifyForm(request.POST or None)
	pk = request.session.get('pk')

	if pk:
		user = User.objects.get(pk=pk)
		phone_num = '+251' + user.phone[1:]
		print(user)
		account_sid = settings.TWILIO_ACCOUNT_SID
		auth_token = settings.TWILIO_AUTH_TOKEN
		twilio_from_num = settings.TWILIO_FROM
		twilio_service = settings.TWILIO_SERVICE
		client = Client(account_sid, auth_token)
		if not request.POST:
			print(phone_num)
			client.verify.services(twilio_service).verifications.create(to=phone_num, channel='sms')
		
		else:
			if verify_form.is_valid():
				verf_num = request.POST.get('number')
				print(verf_num)
				verification_check = client.verify.services(twilio_service).verification_checks.create(to=f'{phone_num}', code=verf_num)
				if verification_check.status =='approved':
					login(request,user)
					print(user.is_active)
					user.is_active = True
					user.save()
					print(user.is_active)
					return redirect("dashboard") 
				else:
					return redirect('verify_me')
	return render(request, 'account/verify.html', {'verify_form':verify_form})
@login_required
def dashboard(request):
	user = request.user
	return render(request,'account/dashboard.html',{'user':user})

@login_required
def edit(request):
	if request.method == 'POST':
		user_edit_form = UserEditForm(instance=request.user, data=request.POST)
		profile_edit_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_edit_form.is_valid() and profile_edit_form.is_valid():
			user_edit_form.save()
			profile_edit_form.save()
			messages.success(request, 'Profile updated successfully')
			return render(request, 'account/dashboard.html')
	else:
		user_edit_form = UserEditForm(instance=request.user)
		profile_edit_form = ProfileEditForm(instance=request.user.profile)

	return render(request, 'account/edit.html', {'user_edit_form': user_edit_form, 'profile_edit_form': profile_edit_form})


def acc_delete(request, pk):
	user = get_object_or_404(User, pk=pk)
	if request.method =="POST":
		user.is_active = False
		user.save()
		return redirect("store:product_list") 
	return render(request, 'account/delete.html', {'user':user})

# def profile_view(request,pk):
# 	profile = get_object_or_404(User,pk=pk)
# 	return render(request,'account/profile.html',{'profile':profile})