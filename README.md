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
Ajoutez `nexui` à la liste des applications installées dans `settings.py` :
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

Le composant `button` permet de créer des boutons personnalisables avec des icônes et des interactions HTMX.

#### **Options disponibles :**
- `label` : Texte du bouton
- `type` : Type du bouton (`button`, `submit`, `reset`)
- `class` : Classes CSS personnalisées
- `icon` : Icône (supporte Font Awesome et Unicode)
- `icon_type` : Type d'icône (`fa`, `unicode`, `emoji`)
- `icon_position` : Position de l'icône (`left`, `right`)
- `icon_size` : Taille de l'icône
- `icon_color` : Couleur de l'icône
- `disabled` : Désactive le bouton (`true`)
- `url_name` : Nom de l'URL Django
- `url_params` : Paramètres dynamiques pour l'URL Django
- `attrs` : Attributs HTML et HTMX supplémentaires (_hx-_*, id, style, data-\* etc.)

### **Exemples d'utilisation :**

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

#### 5️⃣ Bouton avec URL dynamique et un seul paramètres 
```django
{% button label="Dynamique URL Params" type="submit" class="bg-blue-500 text-white" url_name="update-user" url_params="1" attrs="hx-confirm='Êtes-vous sûr ?' hx-target='#result' hx-swap='innerHTML'" %}
```

#### 6️⃣ Bouton avec URL dynamique et plusieurs paramètres 
```django
{% button label="Dynamique URL Params" type="submit" class="bg-blue-500 text-white" url_name="update-user" url_params="1, developer" attrs="hx-confirm='Êtes-vous sûr ?' hx-target='#result' hx-swap='innerHTML'" %}
```


#### 7️⃣ Bouton avec émojis
```django
{% button label="Télécharger" class="bg-green-500" icon="⬇️" icon_position="left" icon_size="lg" %}
```

#### 8️⃣ Bouton désactivé
```django
{% button label="Disabled" disabled="true" %}
```

#### 9️⃣ Bouton avec Font Awesome
```django
{% button label="Éditer" icon="fa-solid fa-pen" icon_type="fa" %}
```

#### 🔟 Bouton avec code HTML
```django
{% button label="Étoile" icon="9733" icon_type="unicode" %}
```

```django
{% button label="At Symbol" icon="&#64" icon_type="unicode" %}
```

---

## 💡 Contribuer

Actuellement, le projet est en phase de test initial. Nous encourageons les utilisateurs intéressés à donner leur avis sur la bibliothèque.

Si vous souhaitez participer à l'évolution de **NexUI** ou si vous avez des suggestions :

1. **Forkez le projet** 📌
2. **Testez les composants et apportez vos retours** 🛠️
3. **Créez une issue** pour partager vos suggestions ou problèmes ✅

Nous ne pouvons pas accepter de contributions directes pour le moment, mais **vos retours sont essentiels** pour l'évolution de NexUI.

---

## 🔗 Liens utiles

- [Dépôt GitHub](https://github.com/huguescodeur/nexui) 🖥️
- [Signaler un bug](https://github.com/huguescodeur/nexui/issues)) 🐞
- [Django-HTMX](https://django-htmx.readthedocs.io/en/latest/installation.html) ⚡
- [Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html) 🎨
- [HTMX](https://htmx.org/) ⚡
- [Tailwind CSS](https://tailwindcss.com/) 🎨

---

## ⚖️ Licence

Ce projet est sous licence **MIT**. Voir le fichier `LICENSE` pour plus de détails.
