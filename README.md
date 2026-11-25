# Cinema Booking API

A cinema reservation REST API built with Django REST Framework. It manages movies, guests and seat reservations, and it shows the same API written in every DRF style, from plain Django JSON views to ViewSets.

## Features

- **Movies, guests and reservations** with linked models (a reservation joins a guest to a movie and hall)
- **Find a movie** by hall and title
- **Book a reservation** in one call: creates the guest and links it to the movie
- **Posts** with an author-only edit permission (`IsAuthorOrReadOnly`)
- Token authentication (`rest_framework.authtoken`) and a login page for the browsable API
- The same guest endpoints written seven ways, to compare the approaches:
  1. Django `JsonResponse` without REST and without a model
  2. Django `JsonResponse` from a model
  3. DRF function-based views (`@api_view`)
  4. DRF class-based views (`APIView`)
  5. DRF mixins
  6. DRF generics
  7. DRF ViewSets with a router

## API

| Endpoint | Style |
| --- | --- |
| `/django/jsonresponsenomodel/` | Plain Django, no model |
| `/django/jsonresponsefrommodel/` | Plain Django, from the model |
| `/rest/fbvlist/`, `/rest/fbv/<id>` | Function-based views |
| `/rest/cbv/`, `/rest/cbv/<id>` | Class-based views |
| `/rest/mixins/`, `/rest/mixins/<id>` | Mixins |
| `/rest/generics/`, `/rest/generics/<id>` | Generics (token authentication) |
| `/rest/viewsets/guest/`, `/rest/viewsets/movies/`, `/rest/viewsets/reservations/` | ViewSets |
| `/fbv/findmovie` | Find a movie by `hall` and `movie` |
| `/fbv/newreservation` | Create a reservation |
| `/post/generics/<id>` | Read a post, or edit it if you're the author |
| `/api-token-auth` | Get a token with username and password |
| `/api-auth` | Log in to the browsable API |

## Built with

- Python 3, Django 5.1, Django REST Framework
- SQLite

## Run it locally

```bash
git clone https://github.com/hamzakhalem/Django-Rest-Frame-work-repo.git
cd Django-Rest-Frame-work-repo
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django djangorestframework
export DJANGO_SECRET_KEY="any-long-random-string"   # PowerShell: $env:DJANGO_SECRET_KEY="..."
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then browse the API at http://127.0.0.1:8000/rest/viewsets/.

## Project structure

```
project/   Settings and all URL routes
tickets/   Models, serializers, permissions and every view style
```
