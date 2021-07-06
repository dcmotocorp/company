=====
worker1
=====

worker1 is a Django worker1 to conduct Web-based worker1. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "worker1" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'worker1',
    ]

2. Include the worker1 URLconf in your project urls.py like this::

    path('worker1/', include('worker1.urls')),

3. Run ``python manage.py migrate`` to create the worker1 models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a worker1 (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/worker1/ to participate in the worker1. 


installation 
-----------------------------------
1) open your project

2)create your virtualenv 

3) install requirement dependancy 

4)open worker1 library 

5) Go to  dist folder and search for the tar file 

6) python pip install dist/<tar file>

7) run your env
