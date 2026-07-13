from django.shortcuts import render
from .models import Profile , Skill, Project, Education

def get_base_context():
    profile = Profile.objects.first()
    return {'profile': profile}

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    categories = ['backend', 'frontend', 'database','tools']
    skill_groups = {cat:skills.filter(category=cat) for cat in categories}
    projects = Project.objects.all()
    education = Education.objects.all()
    return render(request, 'home/index.html', {'profile':profile, 'skill_groups':skill_groups, 'projects':projects, 'education':education, })

def about(request):
    profile = Profile.objects.first()
    return render(request, 'home/about.html', {'profile': profile})

def skills(request):
    profile = Profile.objects.first()
    skill_set = Skill.objects.all()
    categories = ['backend', 'frontend', 'database', 'tools']
    skill_groups = {cat:skill_set.filter(category=cat) for cat in categories}
    return render(request, 'home/skills.html', {'profile': profile, 'skill_groups': skill_groups})

def projects(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    return render(request, 'home/projects.html', {'profile': profile, 'projects': projects,})

def education(request):
    profile = Profile.objects.first()
    education = Education.objects.all()
    return render(request, 'home/education.html', {'profile': profile, 'education': education,})

def contact(request):
    profile = Profile.objects.first()
    return render(request, 'home/contact.html', {'profile': profile})