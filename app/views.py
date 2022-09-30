from django.shortcuts import render
from django.http.response import HttpResponse
from dataclasses import dataclass

# Create your views here.


@dataclass
class Team:
    name: str
    description: str
    members: list


def home(request):
    content = {"content": ["Management",
                           "Community", "Documentation", "Procurement"]}
    return render(request, 'home.html', content)


def team_name(request, team_name):
    context = {
        "team_name": team_name,
        "content": {
            "Management": Team(
                "Management",
                "Management team is responsible for managing the works of other content.",
                ["Kevin", "Chevy", "Erin", "Lukas", "Andrew", "Brooks"]
            ),
            "Community": Team(
                "Community",
                "Community team is responsible for managing community events and other celebratory events like birthdays.",
                ["Eric", "Joshua (me)", "Malcolm", "Amber", "JW", "Angela"]
            ),
            "Documentation": Team(
                "Documentation",
                "Documentation team is responsible for documenting all of the activities of bcca.",
                ["Cannon", "Gabbie", "Antonio", "Colt", "Cooper", "Isaiah"]
            ),
            "Procurement": Team(
                "Procurement",
                "Procurement team is responsible for managing the kitchen, keeping it stocked and providing meals.",
                ["River", "Dylan", "Zaul", "Anna", "Mike", "Luke"]
            )
        }
    }

    return render(request, 'info.html', context)
