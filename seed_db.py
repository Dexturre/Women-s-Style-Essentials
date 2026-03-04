import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luxury_beauty.settings')
django.setup()

from core.models import Category, Product

def seed():
    # Create Categories
    cats = [
        {'name': 'Luxury Beauty', 'slug': 'beauty'},
        {'name': 'Designer-Inspired Bags', 'slug': 'bags'},
        {'name': 'Skincare Essentials', 'slug': 'skincare'},
        {'name': 'Elegant Accessories', 'slug': 'accessories'},
    ]
    
    cat_objs = {}
    for c in cats:
        obj, created = Category.objects.get_or_create(name=c['name'], slug=c['slug'])
        cat_objs[c['slug']] = obj
        print(f"Category {obj.name} created/exists.")

    # Products (simplified migration of the 4 products)
    products = [
        {
            'title': 'Biodance Collagen Hydrogel Overnight Face Mask',
            'cat': 'skincare',
            'img': 'image.png',
            'short': 'Wake up to visibly smoother, hydrated skin with this Korean collagen mask.',
            'full': 'If your skin feels tired, dry, or lacking firmness, this collagen-infused overnight hydrogel mask is designed to restore moisture and improve skin elasticity while you sleep.'
        },
        {
            'title': 'Estée Lauder Pure Color Melt-On Gloss Stick',
            'cat': 'beauty',
            'img': 'Gemini_Generated_Image_nf3odxnf3odxnf3o.png',
            'short': 'A high-shine gloss stick that melts into lips, delivering juicy hydration.',
            'full': 'If you love the look of glossy lips but want the comfort of a balm, this melt-on gloss stick delivers both in one effortless swipe.'
        },
        {
            'title': 'LIANGW Cute Black Cat Canvas Tote Bag',
            'cat': 'bags',
            'img': 'Gemini_Generated_Image_w3xq71w3xq71w3xq.png',
            'short': 'A charming black cat floral tote designed for everyday errands.',
            'full': 'Featuring a whimsical vintage-style floral design with an adorable black cat print, this tote adds a creative touch to your daily routine.'
        },
        {
            'title': 'XZQTIVE 3-Pack Women’s Slim Faux Leather Belts',
            'cat': 'accessories',
            'img': 'Gemini_Generated_Image_qdsnpmqdsnpmqdsn.png',
            'short': 'An elegant 3-piece slim belt set with gold buckles.',
            'full': 'A well-chosen belt can instantly refine an outfit — and this three-piece slim belt set offers both versatility and timeless elegance.'
        }
    ]

    for p in products:
        if not Product.objects.filter(title=p['title']).exists():
            prod = Product(
                title=p['title'],
                category=cat_objs[p['cat']],
                short_description=p['short'],
                full_description=p['full']
            )
            # Try to load the image if it exists in the root
            img_path = p['img']
            if os.path.exists(img_path):
                with open(img_path, 'rb') as f:
                    prod.image.save(p['img'], File(f), save=False)
            prod.save()
            print(f"Product {prod.title} seeded.")

if __name__ == '__main__':
    seed()
