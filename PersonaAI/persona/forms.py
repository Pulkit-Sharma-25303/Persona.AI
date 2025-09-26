from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Portfolio, Project

# --- Authentication Forms ---

class SignUpForm(UserCreationForm):
    """
    A form for new users to create an account, requiring a username and an email.
    """
    email = forms.EmailField(
        max_length=254, 
        help_text='Required. Please enter a valid email address.'
    )
    class Meta:
        model = User
        fields = ('username', 'email')

class LoginForm(AuthenticationForm):
    """
    Standard login form for existing users to authenticate.
    """
    pass


# --- Portfolio Management Forms ---

class ResumeUploadForm(forms.ModelForm):
    """
    A dedicated form for the user to upload their resume file.
    This is the primary action on the dashboard to start the AI process.
    """
    class Meta:
        model = Portfolio
        fields = ['resume']
        widgets = {
            'resume': forms.ClearableFileInput(attrs={
                'class': 'w-full text-sm text-gray-400 file:mr-4 file:py-3 file:px-4 file:rounded-md file:border-0 file:font-semibold file:bg-indigo-600 file:text-white hover:file:bg-indigo-500 cursor-pointer'
            })
        }
        labels = {
            'resume': '' # The label is handled in the HTML template for better layout control
        }


class PortfolioForm(forms.ModelForm):
    """
    A comprehensive form for users to manually edit the details of their portfolio,
    which will be pre-populated by the AI's analysis of their resume.
    """
    class Meta:
        model = Portfolio
        # Add design_template to the list of editable fields
        fields = ['design_template', 'job_title', 'about_me_generated', 'skills_input', 'background_image', 'email', 'linkedin_url', 'github_url']
        
        # Applying consistent styling to all form inputs.
        widgets = {
            # Add a widget for the new design_template field
            'design_template': forms.Select(attrs={
                'class': 'w-full bg-gray-700 text-white rounded-md p-3 border border-gray-600 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'job_title': forms.TextInput(attrs={
                'class': 'w-full bg-gray-700 text-white rounded-md p-3 border border-gray-600 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'about_me_generated': forms.Textarea(attrs={
                'class': 'w-full bg-gray-700 text-white rounded-md p-3 border border-gray-600 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500', 
                'rows': 6
            }),
            'skills_input': forms.Textarea(attrs={
                'class': 'w-full bg-gray-700 text-white rounded-md p-3 border border-gray-600 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500', 
                'rows': 4
            }),
            'background_image': forms.ClearableFileInput(attrs={
                'class': 'w-full text-sm text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-indigo-600 file:text-white hover:file:bg-indigo-500'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-gray-700 text-white rounded-md p-3 border border-gray-600 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'your.email@example.com'
            }),
            'linkedin_url': forms.URLInput(attrs={
                'class': 'w-full bg-gray-700 text-white rounded-md p-3 border border-gray-600 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'https://linkedin.com/in/yourprofile'
            }),
            'github_url': forms.URLInput(attrs={
                'class': 'w-full bg-gray-700 text-white rounded-md p-3 border border-gray-600 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'https://github.com/yourusername'
            }),
        }

class ExperienceForm(forms.ModelForm):
    """A form for editing a single Work Experience entry."""
    class Meta:
        model = Project
        fields = ['name', 'technologies', 'description_generated']
        labels = {
            'name': 'Role / Title',
            'technologies': 'Company Name',
            'description_generated': 'Description'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full bg-gray-800 text-white rounded-md p-2 border border-gray-600 focus:ring-1 focus:ring-indigo-500'}),
            'technologies': forms.TextInput(attrs={'class': 'w-full bg-gray-800 text-white rounded-md p-2 border border-gray-600 focus:ring-1 focus:ring-indigo-500'}),
            'description_generated': forms.Textarea(attrs={'class': 'w-full bg-gray-800 text-white rounded-md p-2 border border-gray-600 focus:ring-1 focus:ring-indigo-500', 'rows': 4}),
        }

class ProjectForm(forms.ModelForm):
    """A form for editing a single Project entry, including its URL."""
    class Meta:
        model = Project
        fields = ['name', 'technologies', 'description_generated', 'project_url']
        labels = {
            'name': 'Project Name',
            'technologies': 'Technologies Used (comma-separated)',
            'description_generated': 'Description',
            'project_url': 'Project URL'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full bg-gray-800 text-white rounded-md p-2 border border-gray-600 focus:ring-1 focus:ring-indigo-500'}),
            'technologies': forms.TextInput(attrs={'class': 'w-full bg-gray-800 text-white rounded-md p-2 border border-gray-600 focus:ring-1 focus:ring-indigo-500'}),
            'description_generated': forms.Textarea(attrs={'class': 'w-full bg-gray-800 text-white rounded-md p-2 border border-gray-600 focus:ring-1 focus:ring-indigo-500', 'rows': 4}),
            'project_url': forms.URLInput(attrs={'class': 'w-full bg-gray-800 text-white rounded-md p-2 border border-gray-600 focus:ring-1 focus:ring-indigo-500', 'placeholder': 'https://github.com/user/repo'}),
        }

