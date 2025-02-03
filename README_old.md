# NexUI

🚀 **NexUI** est une bibliothèque de composants UI pour **Django**, optimisée pour **HTMX** et basée sur **Tailwind CSS**.

## 📌 Installation

Ajoutez **NexUI** à votre projet Django en exécutant la commande suivante :

```bash
pip install nexui
```

Puis ajoutez `nexui` à la liste des applications installées dans `settings.py` :

```python
INSTALLED_APPS = [
    ...
    'nexui',
]
```

## 🎨 Fonctionnalités
- ✅ Composants UI réutilisables pour Django
- 🔥 Intégration fluide avec **HTMX**
- 🎨 Basé sur **Tailwind CSS** pour un design moderne
- 📦 Facile à installer et à utiliser

## 🚀 Utilisation

Ajoutez un composant UI NexUI dans vos templates Django :

```html
{% load nexui %}

<div class="container mx-auto p-4">
    {% nexui_button "Cliquez-moi" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" %}
</div>
```

## 📖 Documentation

Consultez la documentation complète ici : [Documentation officielle](https://github.com/huguescodeur/nexui)

## 💡 Contribuer

Les contributions sont les bienvenues !

1. Forkez le projet 📌
2. Créez une branche (`git checkout -b ma-feature`)
3. Apportez vos modifications 🛠️
4. Commitez vos changements (`git commit -m "Ajout de ma feature"`)
5. Poussez la branche (`git push origin ma-feature`)
6. Créez une **Pull Request** ✅

## 🔗 Liens utiles
- [Dépôt GitHub](https://github.com/huguescodeur/nexui)
- [Signaler un bug](https://github.com/huguescodeur/nexui/issues)
- [HTMX](https://htmx.org/)
- [Tailwind CSS](https://tailwindcss.com/)

## ⚖️ Licence

Ce projet est sous licence **MIT**. Voir le fichier [`LICENSE`](https://github.com/huguescodeur/nexui/blob/main/LICENSE) pour plus de détails.

- **attrs** : Attributs HTML supplémentaires (_hx-_, id, style, data-\* etc.)