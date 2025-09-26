from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .forms import (
    SignUpForm, LoginForm, PortfolioForm, ResumeUploadForm,
    ExperienceForm, ProjectForm
)
from .models import Portfolio, Project
from . import ai_service

def home_view(request):
    """Renders the public-facing homepage."""
    return render(request, 'persona/home.html')

def signup_view(request):
    """Handles new user registration."""
    if request.user.is_authenticated:
        return redirect('persona:dashboard')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Let's build your portfolio.")
            return redirect('persona:dashboard')
    else:
        form = SignUpForm()
    return render(request, 'persona/signup.html', {'form': form})

def login_view(request):
    """Handles existing user login."""
    if request.user.is_authenticated:
        return redirect('persona:dashboard')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('persona:dashboard')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'persona/login.html', {'form': form})

def logout_view(request):
    """Logs the current user out."""
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('persona:home')

@login_required
def dashboard_view(request):
    """
    Manages the user's dashboard, including the main portfolio form
    and formsets for editing multiple experience and project entries.
    """
    portfolio = request.user.portfolio
    
    ExperienceFormSet = modelformset_factory(Project, form=ExperienceForm, extra=0)
    ProjectFormSet = modelformset_factory(Project, form=ProjectForm, extra=0)

    experience_queryset = portfolio.get_experiences()
    project_queryset = portfolio.get_projects()

    if request.method == 'POST':
        upload_form = ResumeUploadForm(instance=portfolio)
        details_form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        experience_formset = ExperienceFormSet(request.POST, queryset=experience_queryset, prefix='experience')
        project_formset = ProjectFormSet(request.POST, queryset=project_queryset, prefix='project')
        
        if 'upload_resume' in request.POST:
            upload_form = ResumeUploadForm(request.POST, request.FILES, instance=portfolio)
            if upload_form.is_valid():
                upload_form.save()
                try:
                    ai_service.process_resume(portfolio)
                    messages.success(request, 'Resume processed! Review the extracted details.')
                except Exception as e:
                    messages.error(request, f"AI processing error: {e}")
                return redirect('persona:dashboard')
        
        elif 'update_details' in request.POST:
            if details_form.is_valid() and experience_formset.is_valid() and project_formset.is_valid():
                details_form.save()
                experience_formset.save()
                project_formset.save()
                messages.success(request, 'Your portfolio has been updated successfully.')
                return redirect('persona:dashboard')
            else:
                messages.error(request, 'Please correct the errors below.')

    else:
        upload_form = ResumeUploadForm(instance=portfolio)
        details_form = PortfolioForm(instance=portfolio)
        experience_formset = ExperienceFormSet(queryset=experience_queryset, prefix='experience')
        project_formset = ProjectFormSet(queryset=project_queryset, prefix='project')

    context = {
        'portfolio': portfolio,
        'upload_form': upload_form,
        'details_form': details_form,
        'experience_formset': experience_formset,
        'project_formset': project_formset,
    }
    return render(request, 'persona/dashboard.html', context)

def portfolio_view(request, slug):
    """
    Displays a user's public portfolio page, rendering the template
    they have selected in their dashboard.
    """
    portfolio = get_object_or_404(Portfolio, slug=slug)

    template_map = {
        'modern': 'persona/public_portfolio_modern.html',
        'minimalist': 'persona/public_portfolio_minimalist.html',
        'creative': 'persona/public_portfolio_creative.html',
        'professional': 'persona/public_portfolio_professional.html',
        'experimental': 'persona/public_portfolio_experimental.html',
    }
    
    template_name = template_map.get(portfolio.design_template, 'persona/public_portfolio_modern.html')

    context = {
        'portfolio': portfolio,
    }
    return render(request, template_name, context)