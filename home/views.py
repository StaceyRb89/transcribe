from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'home/index.html'

def contact_view(request):
    # Your contact view implementation
    return render(request, 'contact/contact.html') 

#added

# the team
# views.py
def team(request):
    # Your logic to fetch team information goes here
    team_info = {
        'team_members': [
            {'name': 'Member 1', 'position': 'Position 1'},
            {'name': 'Member 2', 'position': 'Position 2'},
            # Add more team members as needed
        ]
    }


    return render(request, 'home/team.html', {'team_info': team_info})


def faq (request):
    return render(request, 'home/faq.html')