# 🚀 NexUI

NexUI est une bibliothèque de composants UI pour Django, optimisée pour HTMX et basée sur Tailwind CSS. Elle permet d'ajouter facilement des éléments interactifs à vos applications Django tout en bénéficiant des avantages d'une intégration fluide avec HTMX pour la gestion des requêtes AJAX.

---

## 📌 Installation

### Installation de base
```bash
pip install nexui
```

### Installation avec support HTMX
Si vous prévoyez d'utiliser HTMX avec vos composants :
```bash
pip install nexui[htmx]
```

Ou installez HTMX séparément plus tard :
```bash
pip install django-htmx
```

Ajoutez nexui à la liste des applications installées dans settings.py :
```python
INSTALLED_APPS = [
    ...
    'nexui',
]
```

---

## 🎨 Fonctionnalités

✅ Composants UI réutilisables pour Django  
🔥 Intégration fluide avec HTMX  
🎨 Basé sur Tailwind CSS pour un design moderne  
📦 Facile à installer et à utiliser  

---

## 🚀 Utilisation

### Charger les tags NexUI dans vos templates Django

```django
{% load nexui_tags %}
```

---

## 📖 Documentation

Consultez la documentation complète ici : [Documentation officielle](https://github.com/huguescodeur/nexui)

### 🔘 Composant Button

Le composant button permet de créer des boutons personnalisables avec des icônes et des interactions HTMX.

#### **Options disponibles :**
- `label` : Texte du bouton
- `type` : Type du bouton (`button`, `submit`, `reset`)
- `class` : Classes CSS personnalisées
- `icon` : Icône (supporte `Emoji` `Font Awesome` et `Unicode`)
- `icon_type` : Type d'icône (`emoji`, `fa`, `unicode`)
- `icon_position` : Position de l'icône (`left`, `right`)
- `icon_size` : Taille de l'icône
- `icon_color` : Couleur de l'icône
- `disabled` : Désactive le bouton (`true`)
- `url_name` : Nom de l'URL Django
- `url_params` : Paramètres dynamiques pour l'URL Django
- `attrs` : Attributs `HTML` et `HTMX` supplémentaires (`_hx-_*`, `id`, `style`, `data-*` etc.)

### **Exemples d'utilisation du Button :**

#### 1️⃣ Bouton simple
```django
{% button label="Envoyer" %}
```

#### 2️⃣ Bouton simple personnalisé
```django
{% button label="Envoyer" type="submit" class="bg-yellow-500 text-black" %}
```

#### 3️⃣ Bouton avec HTMX
```django
{% button label="Envoyer avec HTMX" type="submit" class="bg-green-500" attrs="hx-post='/submit' hx-target='#result' hx-swap='innerHTML'" %}
```

#### 4️⃣ Bouton avec URL dynamique
```django
{% button label="Dynamique URL Params" type="submit" class="bg-blue-500 text-white" url_name="update-user" url_params="2, tomate" attrs="hx-confirm='Êtes-vous sûr ?' hx-target='#result' hx-swap='innerHTML'" %}
```

#### 5️⃣ Bouton avec émojis
```django
{% button label="Télécharger" class="bg-green-500" icon="⬇️" icon_position="left" icon_size="lg" %}
```

### 📝 Composant Input

Le composant input permet de créer des champs de saisie personnalisables avec labels, icônes et intégration HTMX.

#### **Options disponibles :**
- `type` : Type de l'input (`text`, `password`, `email`, etc.)
- `name` : Nom du champ
- `id` : ID du champ (par défaut égal au `name`)
- `value` : Valeur par défaut
- `placeholder` : Texte d'aide
- `container_class` : Classes CSS pour le conteneur principal
- `wrapper_class` : Classes CSS pour le wrapper de l'input
- `label_class` : Classes CSS pour le label
- `input_class` : Classes CSS pour l'input
- `label` : Texte du label
- `required` : Champ obligatoire (`true`/`false`)
- `disabled` : Désactive le champ (`true`/`false`)
- `readonly` : Lecture seule (`true`/`false`)
- `icon` : Icône (supporte `Emoji`, `Font Awesome` et `Unicode`)
- `icon_type` : Type d'icône (`fa`, `emoji`)
- `icon_position` : Position de l'icône (`left`, `right`)
- `icon_size` : Taille de l'icône
- `icon_color` : Couleur de l'icône
- `url_name` : Nom de l'URL Django pour `HTMX`
- `method` : Méthode HTTP pour HTMX (`post` par défaut)
- `attrs` : Attributs `HTML` et `HTMX` supplémentaires

### **Exemples d'utilisation du Input :**

#### 1️⃣ Input simple avec label et icône
```django
{% input_field name="email" label="Email" icon="fas fa-envelope" icon_type="fa" icon_position="left" placeholder="Email" %}
```

#### 2️⃣ Input password avec emoji
```django
{% input_field type="password" icon="🔒" %}
```

#### 3️⃣ Input avec HTMX et confirmation
```django
{% input_field name="email" label="Email" icon="fas fa-envelope" icon_type="fa" url_name="submit-form" attrs='hx-confirm="Are you okay?"' %}
```

#### 4️⃣ Input avec recherche en temps réel
```django
{% input_field name="search" label="Recherche" icon="fas fa-search" icon_type="fa" icon_position="left" url_name="search_suggestions" attrs='hx-trigger="keyup changed delay:500ms" hx-target="#suggestions"' %}
```

#### 5️⃣ Input personnalisé avec style
```django
{% input_field container_class="py-2 flex items-center" name="email" label="Email" label_class="ml-2 text-gray-700 font-bold" input_class="w-44 pl-10 pr-3 py-2 rounded-md border border-gray-300" icon="fas fa-envelope" icon_type="fa" icon_position="left" %}
```

---

## 💡 Contribuer

Actuellement, le projet est en phase de test initial. Nous encourageons les utilisateurs intéressés à donner leur avis sur la bibliothèque.

Si vous souhaitez participer à l'évolution de **NexUI** ou si vous avez des suggestions :

1. **`Forkez` le projet** 📌
2. **`Testez` les composants et apportez vos retours** 🛠️
3. **`Créez` une issue** pour partager vos suggestions ou problèmes ✅

Nous ne pouvons pas accepter de contributions directes pour le moment, mais **vos retours sont essentiels** pour l'évolution de NexUI.

---

## 🔗 Liens utiles

- [Dépôt GitHub](https://github.com/huguescodeur/nexui) 🖥️
- [Signaler un bug](https://github.com/huguescodeur/nexui/issues) 🐞
- [Django-HTMX](https://django-htmx.readthedocs.io/en/latest/installation.html) ⚡
- [Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html) 🎨
- [HTMX](https://htmx.org/) ⚡
- [Tailwind CSS](https://tailwindcss.com/) 🎨

---

## ⚖️ Licence

Ce projet est sous licence **MIT**. Voir le fichier LICENSE pour plus de détails.