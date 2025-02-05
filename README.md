# 🚀 NexUI

NexUI is a UI component library for Django, optimized for HTMX and based on Tailwind CSS. It allows you to easily add interactive elements to your Django applications while benefiting from seamless integration with HTMX for AJAX request handling.

---

## 📌 Installation

### Basic Installation
```bash
pip install nexui
```

### Installation with HTMX support
If you plan to use HTMX with your components:
```bash
pip install nexui[htmx]
```

Or install HTMX separately later:
```bash
pip install django-htmx
```

Add nexui to the list of installed apps in `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'nexui',
]
```

---

## 🎨 Features

✅ Reusable UI components for Django  
🔥 Smooth integration with HTMX  
🎨 Based on Tailwind CSS for a modern design  
📦 Easy to install and use  

---

## 🚀 Usage

### Load NexUI tags in your Django templates
```django
{% load nexui_tags %}
```

---

## 📖 Documentation

Check the full documentation here: [Official Documentation](https://pypi.org/project/nexui/)

### 🔘 Button Component

The button component allows you to create customizable buttons with icons and HTMX interactions.

#### **Available Options:**
- `label`: Button text
- `type`: Button type (`button`, `submit`, `reset`)
- `button_class`: Custom CSS classes
- `icon`: Icon (supports `Emoji`, `Font Awesome`, and `Unicode`)
- `icon_type`: Icon type (`emoji`, `fa`, `unicode`)
- `icon_position`: Icon position (`left`, `right`)
- `icon_size`: Icon size
- `icon_color`: Icon color
- `disabled`: Disables the button (`true`)
- `url_name`: Django URL name
- `url_params`: Dynamic parameters for the Django URL
- `attrs`: Additional `HTML` and `HTMX` attributes (`_hx-*`, `id`, `style`, `data-*`, etc.)

### **Button Usage Examples:**

#### 1️⃣ Simple Button
```django
{% button label="Send" %}
```

#### 2️⃣ Customized Simple Button
```django
{% button label="Send" type="submit" button_class="bg-yellow-500 text-black" %}
```

#### 3️⃣ Button with HTMX
```django
{% button label="Send with HTMX" type="submit" button_class="bg-green-500" attrs="hx-post='/submit' hx-target='#result' hx-swap='innerHTML'" %}
```

#### 4️⃣ Button with Dynamic URL
```django
{% button label="Dynamic URL Params" type="submit" button_class="bg-blue-500 text-white" url_name="update-user" url_params="2, tomato" attrs="hx-confirm='Are you sure?' hx-target='#result' hx-swap='innerHTML'" %}
```

#### 5️⃣ Button with Emojis
```django
{% button label="Download" button_class="bg-green-500" icon="⬇️" icon_position="left" icon_size="lg" %}
```

### 📝 Input Component

The input component allows you to create customizable input fields with labels, icons, and HTMX integration.

#### **Available Options:**
- `type`: Input type (`text`, `password`, `email`, etc.)
- `name`: Field name
- `id`: Field ID (default is the same as `name`)
- `value`: Default value
- `placeholder`: Placeholder text
- `container_class`: CSS classes for the main container
- `wrapper_class`: CSS classes for the input wrapper
- `label_class`: CSS classes for the label
- `input_class`: CSS classes for the input
- `label`: Label text
- `required`: Required field (`true`/`false`)
- `disabled`: Disables the field (`true`/`false`)
- `readonly`: Read-only field (`true`/`false`)
- `icon`: Icon (supports `Emoji`, `Font Awesome`, and `Unicode`)
- `icon_type`: Icon type (`emoji`, `fa`, `unicode`)
- `icon_position`: Icon position (`left`, `right`)
- `icon_size`: Icon size
- `icon_color`: Icon color
- `url_name`: Django URL name for `HTMX`
- `method`: HTTP method for HTMX (`post` by default)
- `attrs`: Additional `HTML` and `HTMX` attributes

### **Input Usage Examples:**

#### 1️⃣ Simple Input with Label and Icon

##### Simple Input
```django
{% input_field %}
```

##### Simple Input with Label
```django
{% input_field name="email" label="Email" %}
```

##### Simple Input with Label, Icon, and Customization
```django
{% input_field name="email" label="Email" icon="fas fa-envelope" icon_type="fa" icon_position="left" placeholder="Email" %}
```

#### 2️⃣ Password Input with Emoji
```django
{% input_field type="password" icon="🔒" %}
```

#### 3️⃣ Input with HTMX and Confirmation
```django
{% input_field name="email" label="Email" icon="fas fa-envelope" icon_type="fa" url_name="submit-form" attrs='hx-confirm="Are you okay?"' %}
```

#### 4️⃣ Input with Real-Time Search
```django
{% input_field name="search" label="Search" icon="fas fa-search" icon_type="fa" icon_position="left" url_name="search_suggestions" attrs='hx-trigger="keyup changed delay:500ms" hx-target="#suggestions"' %}
```

#### 5️⃣ Custom Styled Input
```django
{% input_field container_class="py-2 flex items-center" name="email" label="Email" label_class="ml-2 text-gray-700 font-bold" input_class="w-44 pl-10 pr-3 py-2 rounded-md border border-gray-300" icon="fas fa-envelope" icon_type="fa" icon_position="left" %}
```

---
### 🔐 Authentication Components Example
NexUI provides pre-built authentication components that you can easily integrate into your Django applications. Below are examples of login and registration forms built with NexUI components.

#### 🔐 Register Form Example
Create a beautiful registration form with social authentication options:

![Register Image](https://dl.dropboxusercontent.com/scl/fi/ctzrg5q42qru5ema4jlo6/register.png?rlkey=hb7037n155t5jhw9rv4l87d0u&st=bdet46zf&dl=0)


```django
<div class="max-w-md w-full p-6 bg-white rounded-lg shadow-md">
    <h1 class="text-2xl font-bold mb-2">Create an account</h1>
    <p class="text-gray-600 mb-6">Enter your email below to create your account</p>

    <div class="space-y-4">
        {# OAuth Buttons #}
        <div class="flex gap-4 mb-4">
            {% button label="GitHub" button_class="w-full border border-gray-300 bg-white hover:bg-gray-50" 
                     icon="fa-brands fa-github fa-lg" icon_type="fa" icon_position="left" %}
            {% button label="Google" button_class="w-full border border-gray-300 bg-white hover:bg-gray-50" 
                     icon="fa-brands fa-google fa-lg" icon_type="fa" icon_position="left" %}
        </div>

        {# Separator #}
        <div class="relative my-6">
            <div class="absolute inset-0 flex items-center">
                <span class="w-full border-t"></span>
            </div>
            <div class="relative flex justify-center text-xs uppercase">
                <span class="bg-white px-2 text-gray-500">OR CONTINUE WITH</span>
            </div>
        </div>

        {# Email Field #}
        {% input_field type="email" name="register_email" label="Email" 
                      placeholder="nexui@example.com" container_class="mb-4" 
                      input_class="h-10" icon="fa-solid fa-envelope" 
                      icon_type="fa" required="true" %}

        {# Password Field #}
        {% input_field type="password" name="register_password" label="Password" 
                      container_class="mb-6" input_class="h-10" 
                      icon="fa-solid fa-lock" icon_type="fa" required="true" %}

        {# Submit Button #}
        {% button label="Create account" type="submit" 
                 button_class="w-full bg-gray-900 text-white hover:bg-gray-800" %}
    </div>
</div>
```

#### 🔐 Login Form Example
Create a matching login form with social authentication:

![Login Image](https://dl.dropboxusercontent.com/scl/fi/d5tjmyciv6eb1cy2xcibw/login.png?rlkey=fog7vyyv6hupi3c60uuq685os&e=1&st=gk5i7qiz&dl=0)

```django
<div class="max-w-md w-full p-6 bg-white rounded-lg shadow-md">
    <h1 class="text-2xl font-bold mb-2">Login</h1>
    <p class="text-gray-600 mb-6">Welcome back! Please enter your details</p>

    <div class="space-y-4">
        {# OAuth Buttons #}
        <div class="flex gap-4 mb-4">
            {% button label="GitHub" button_class="w-full border border-gray-300 bg-white hover:bg-gray-50" 
                     icon="fa-brands fa-github fa-lg" icon_type="fa" icon_position="left" %}
            {% button label="Google" button_class="w-full border border-gray-300 bg-white hover:bg-gray-50" 
                     icon="fa-brands fa-google fa-lg" icon_type="fa" icon_position="left" %}
        </div>

        {# Separator #}
        <div class="relative my-6">
            <div class="absolute inset-0 flex items-center">
                <span class="w-full border-t"></span>
            </div>
            <div class="relative flex justify-center text-xs uppercase">
                <span class="bg-white px-2 text-gray-500">OR CONTINUE WITH</span>
            </div>
        </div>

        {# Email Field #}
        {% input_field type="email" name="login_email" label="Email" 
                      placeholder="nexui@example.com" container_class="mb-4" 
                      input_class="h-10" icon="fa-solid fa-envelope" 
                      icon_type="fa" required="true" %}

        {# Password Field #}
        {% input_field type="password" name="login_password" label="Password" 
                      container_class="mb-2" input_class="h-10" 
                      icon="fa-solid fa-lock" icon_type="fa" required="true" %}

        {# Forgot Password Link #}
        <div class="flex justify-end mb-6">
            <a href="#" class="text-sm text-black hover:underline">Forgot password?</a>
        </div>

        {# Submit Button #}
        {% button label="Sign in" type="submit" 
                 button_class="w-full bg-gray-900 text-white hover:bg-gray-800" %}
    </div>
</div>
```
#### Features
Both forms include:

- 🔑 Social authentication options (GitHub and Google)
- 📧 Email and password fields with icons
- 🎨 Clean, modern design with Tailwind CSS
- 📱 Responsive layout

#### Customization
You can customize these forms by:

- `Modifying` the Tailwind CSS classes
- `Adding` or `removing` social authentication providers
- `Customizing` the icons using Font Awesome classes
- Adding `HTMX` attributes for enhanced interactivity
Adjusting the layout and spacing

---

## 💡 Contribute

The project is currently in its early testing phase. We encourage interested users to provide feedback on the library.

If you want to contribute to **NexUI** or have suggestions:

1. **`Fork` the project** 📌
2. **`Test` the components and provide feedback** 🛠️
3. **`Create` an issue** to share your suggestions or report problems ✅

We cannot accept direct contributions at the moment, but **your feedback is essential** for NexUI's evolution.

---

## 🔗 Useful Links

- [GitHub Repository](https://github.com/huguescodeur/nexui) 🖥️
- [Report a Bug](https://github.com/huguescodeur/nexui/issues) 🐞
- [Django-HTMX](https://django-htmx.readthedocs.io/en/latest/installation.html) ⚡
- [Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html) 🎨
- [HTMX](https://htmx.org/) ⚡
- [Tailwind CSS](https://tailwindcss.com/) 🎨

---

## ⚖️ License

This project is licensed under the **MIT** license. See the LICENSE file for more details.

![PyPI - Downloads](https://img.shields.io/pypi/dm/nexui)

