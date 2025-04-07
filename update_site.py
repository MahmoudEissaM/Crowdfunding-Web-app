from django.contrib.sites.models import Site
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crowdfunding.settings')
django.setup()

def update_site():
    site = Site.objects.get(id=1)
    site.domain = '127.0.0.1:5002'  
    site.name = 'Crowdfunding'
    site.save()
    print(f"Site updated successfully: {site.domain}")

if __name__ == "__main__":
    update_site()
