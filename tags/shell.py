from tags.models import Tag

qs = Tag.objects.all()
print(qs)
kaki = Tag.objects.last()
kaki.titre
kaki.slug

kaki.produits

kaki.produits.all().first()

exit()

# Produits

from produits.models import Produit


qs = Produit.objects.all()
print(qs)
polo = qs.first()
polo.titre
polo.description

polo.tag

polo.tags

polo.tag_set


polo.tag_set.all()


kaki.tag_set.filter(titre__icontains='kaki')