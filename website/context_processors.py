from .models import Project

def get_public_projects(request):

    projects_full = []

    projects = Project.objects.filter(is_public=True)

    # Relate project with its languages and framewworks
    for project in projects:
        related_languages = project.languages.all()
        related_frameworks = project.framework.all()
        related_libraries = project.libraries.all()

        if related_libraries.filter(name__in=("Pandas","Numpy","Seaborn","MatPlotLib")).exists():
            filter_identifier = "filter-datascience filter-python"
        elif related_frameworks.filter(name="Django").exists():
            filter_identifier = "filter-django filter-python"
        elif related_languages.filter(name="Python").exists():
            filter_identifier = "filter-python"
        else:
            filter_identifier = None

        # Create dictionary with project and its tags
        full_project = {
            "project":project,
            "languages":related_languages,
            "framework":related_frameworks,
            "libraries":related_libraries,
            "filter":filter_identifier,
        }
        
        # Add dictionary to the list of projects
        projects_full.append(full_project)
    

    # return context
    return ({"projects_full":projects_full})

