# [Django File Manager](https://github.com/app-generator/sample-django-file-manager/)

Open-source **Django** project crafted on top of **[Corporate Dashboard](https://appseed.us/product/corporate-dashboard/django/)**, an open-source `Bootstrap 5` design from [Creative-Tim](https://www.creative-tim.com/product/corporate-ui-dashboard?AFFILIATE=128200).
Designed for those who like bold elements and beautiful websites. Made of hundred of elements, designed blocks and fully coded pages, `Corporate Dashboard` is ready to help you create stunning websites and web apps.

> 👉 `VIDEO Presentation`: [Django File Manager](https://www.youtube.com/watch?v=dBWGf-ZNUDI) (published on `YouTube`)
  
<br />

## Features

> `Have questions?` Contact **[Support](https://appseed.us/support/)** (Email & Discord) provided by **AppSeed**

| Free Version                          | [PRO Version](https://appseed.us/product/datta-able-pro/django/)    | [Custom Development](https://appseed.us/custom-development/) |  
| --------------------------------------| --------------------------------------| --------------------------------------|
| ✓ **Media Files Manager**             | **Everything in Free**, plus:                                                          | **Everything in PRO**, plus:         |
| ✓ Best Practices                      | ✅ **Premium Bootstrap 5 Design**                                                      | ✅ **1mo Custom Development**       | 
| ✓ Bootstrap 4, `Datta Able` Design    | ✅ `OAuth` Google, GitHub                                                              | ✅ **Team**: PM, Developer, Tester  |
| ✓ API Generator                       | ✅ `API`, **[Charts](https://django-datta-pro.onrender.com/charts/)**                  | ✅ Weekly Sprints                   |
| ✓ DataTables                          | ✅ **[Enhanced DataTables](https://django-datta-pro.onrender.com/tables/)**            | ✅ Technical SPECS                  |
| ✓ `Docker`                            | ✅ **Celery**                                                                          | ✅ Documentation                    |
| ✓ `CI/CD` Flow via Render             | ✅ **Media Files Manager**                                                             | ✅ **30 days Delivery Warranty**    |
| -                                     | ✅ **Extended User Profiles**                                                          |  -                                   |
| -                                     | ✅ **Automated e2e Tests**                                                             |  -                                   |
| -                                     | ✅ `Private REPO Access`                                                               |  -                                   |
| -                                     | ✅ **PRO Support** - [Email & Discord](https://appseed.us/support/)                    |  -                                   |
| -                                     | ✅ Deployment Assistance                                                               |  -                                   |
| -                                     | -                                                                                       |  -                                   |
| ------------------------------------  | ------------------------------------                                                    | ------------------------------------|
| ✓ [VIDEO](https://www.youtube.com/watch?v=dBWGf-ZNUDI)  | 🚀 [LIVE Demo](https://django-datta-pro.onrender.com/) | 🛒 `Order`: **[$3,999](https://appseed.gumroad.com/l/rocket-package)** (GUMROAD) |   

![Django File Manager - Open-Source Sample crafted by AppSeed.](https://github.com/app-generator/sample-django-file-manager/assets/51070104/0d40c31f-d109-4ed8-b4f5-6a9be585e5e6)

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/sample-django-file-manager.git
$ cd sample-django-file-manager
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py   # Project Configuration  
   |    |-- urls.py       # Project Routing
   |
   |-- home/
   |    |-- views.py      # APP Views 
   |    |-- urls.py       # APP Routing
   |    |-- models.py     # APP Models 
   |    |-- tests.py      # Tests  
   |     
   |-- templates/
   |    |-- includes/     # UI components 
   |    |-- layouts/      # Masterpages
   |    |-- pages/        # Kit pages 
   |
   |-- static/   
   |    |-- css/                                   # CSS Files 
   |    |-- scss/                                  # SCSS Files 
   |         |-- corporate-ui-dashboard/_variables.scss # File Used for Theme Styling
   |
   |-- requirements.txt   # Project Dependencies
   |
   |-- env.sample         # ENV Configuration (default values)
   |-- manage.py          # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## Recompile SCSS  

The SCSS/CSS files used to style the Ui are saved in the `static` directory. 
In order to update the Ui colors (primary, secondary) this procedure needs to be followed. 

```bash
$ yarn                                                  # install modules
$ vi static/scss/corporate-ui-dashboard/_variables.scss # edit variables 
$ gulp                                                  # SCSS to CSS translation
```

The `_variables.scss` content defines the `primary` and `secondary` colors: 

```scss
$primary:       #774dd3 !default; // EDIT for customization
$secondary:     #64748b !default; // EDIT for customization
$info:          #55a6f8 !default; // EDIT for customization
$success:       #67c23a !default; // EDIT for customization
$warning:       #f19937 !default; // EDIT for customization 
$danger:        #ea4e3d !default; // EDIT for customization
```

<br />

## Deploy on [Render](https://render.com/)

- Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
- Click `New Blueprint Instance` button.
- Connect your `repo` which you want to deploy.
- Fill the `Service Group Name` and click on `Update Existing Resources` button.
- After that your deployment will start automatically.

At this point, the product should be LIVE.

<br />

---
[Django File Manager ](https://github.com/app-generator/sample-django-file-manager/) - **Django** starter provided by **[AppSeed](https://appseed.us/)**
