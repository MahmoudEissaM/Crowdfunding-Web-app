from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Avg, Q
from .models import Project, ProjectComment, ProjectRating, ProjectReport, ProjectPicture, Category
from .forms import ProjectForm, ProjectCommentForm, ProjectRatingForm, ProjectReportForm, ProjectPictureForm

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(
            is_cancelled=False,
            end_time__gt=timezone.now()
        ).annotate(
            average_rating=Avg('ratings__rating')
        ).order_by('-created_at')  # Add this ordering
        
        if 'category' in self.kwargs:
            queryset = queryset.filter(category__slug=self.kwargs['category'])
        
        if 'search' in self.request.GET:
            search_term = self.request.GET['search']
            queryset = queryset.filter(
                Q(title__icontains=search_term) |
                Q(tags__name__icontains=search_term)
            ).distinct()
        
        return queryset
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        
        # Add comment form
        context['comment_form'] = ProjectCommentForm()
        
        # Add rating form (if user hasn't rated yet)
        if self.request.user.is_authenticated:
            user_rating = ProjectRating.objects.filter(
                project=project,
                user=self.request.user
            ).first()
            if not user_rating:
                context['rating_form'] = ProjectRatingForm()
            else:
                context['user_rating'] = user_rating
        
        # Calculate average rating
        context['average_rating'] = project.ratings.aggregate(
            avg_rating=Avg('rating')
        )['avg_rating']
        
        # Get similar projects (by tags)
        similar_projects = Project.objects.filter(
            tags__in=project.tags.all()
        ).exclude(
            id=project.id
        ).distinct()[:4]
        context['similar_projects'] = similar_projects
        
        return context

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        response = super().form_valid(form)
        
        # Handle multiple pictures upload
        pictures = self.request.FILES.getlist('pictures')
        for i, picture in enumerate(pictures):
            ProjectPicture.objects.create(
                project=self.object,
                image=picture,
                is_featured=(i == 0)  # First image is featured by default
            )
        
        messages.success(self.request, "Project created successfully!")
        return response
    
    def get_success_url(self):
        return reverse_lazy('projects:project-detail', kwargs={'pk': self.object.pk})

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        project = self.get_object()
        if project.creator != request.user:
            messages.error(request, "You can't edit this project")
            return redirect('projects:project-detail', pk=project.pk)
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('projects:project-detail', kwargs={'pk': self.object.pk})

class ProjectCancelView(LoginRequiredMixin, View):
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        
        if project.creator != request.user:
            messages.error(request, "You can't cancel this project")
            return redirect('projects:project-detail', pk=project.pk)
        
        if not project.can_be_cancelled():
            messages.error(request, "Project can't be cancelled as it has reached 25% of target")
            return redirect('projects:project-detail', pk=project.pk)
        
        project.is_cancelled = True
        project.save()
        messages.success(request, "Project cancelled successfully")
        return redirect('projects:project-detail', pk=project.pk)

# Add similar views for comments, ratings, reports following the same pattern
def add_comment(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ProjectCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()
            messages.success(request, "Comment added successfully!")
            return redirect('projects:project-detail', pk=project.pk)
    else:
        form = ProjectCommentForm()
    
    return render(request, 'projects/add_comment.html', {'form': form, 'project': project})

def add_rating(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ProjectRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project = project
            rating.user = request.user
            rating.save()
            messages.success(request, "Rating added successfully!")
            return redirect('projects:project-detail', pk=project.pk)
    else:
        form = ProjectRatingForm()
    
    return render(request, 'projects/add_rating.html', {'form': form, 'project': project})


def donate(request, pk):
    project = get_object_or_404(Project, pk=pk)
    # Add donation logic here
    return redirect('projects:project-detail', pk=pk)

def project_list(request):
    projects = Project.objects.all()  # Fetch all projects from the database
    return render(request, 'projects/project_list.html', {'projects': projects})