import os
import re
import warnings
import inspect
import importlib
from populationscript import populate
from django.urls import reverse, resolve
from django.test import TestCase
from django.conf import settings
from playerhq.models import Games, Reviews, Categories
from django.db.models.query import QuerySet
from django.forms import fields as django_fields
from playerhq.forms import GameForm, Review

from django.contrib.auth.models import User

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}==============={os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

class test1(TestCase):
    """
    tests to probe the file structure of your project 
    test to check whether you have added playerhq to your list of INSTALLED_APPS.
    """
    def setUp(self):
        
        self.project_base_dir = os.getcwd()
        self.playerhq_app_dir = os.path.join(self.project_base_dir, 'playerhq')
        
    def test_project_created(self):
        """
        Tests whether the playerhq configuration directory is present and correct.
        """
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, 'PLHQ'))
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'PLHQ', 'urls.py'))
        
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Your PLHQ configuration directory doesn't seem to exist.")
        self.assertTrue(urls_module_exists, f"{FAILURE_HEADER}Your project's urls.py module does not exist.")
        
    def test_playrthq_app_created(self):
        """
        Determines whether the PLHQ app has been created.
        """
        directory_exists = os.path.isdir(self.playerhq_app_dir)
        is_python_package = os.path.isfile(os.path.join(self.playerhq_app_dir, '__init__.py'))
        views_module_exists = os.path.isfile(os.path.join(self.playerhq_app_dir, 'views.py'))
        
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}The playerhq app directory does not exist.")
        self.assertTrue(is_python_package, f"{FAILURE_HEADER}The playerhq directory is missing files.")
        self.assertTrue(views_module_exists, f"{FAILURE_HEADER}The playerhq directory is missing files.")
    
    def test_playerhq_has_urls_module(self):
        """
        separate urls.py module for playerhq?
        """
        module_exists = os.path.isfile(os.path.join(self.playerhq_app_dir, 'urls.py'))
        self.assertTrue(module_exists, f"{FAILURE_HEADER}The playerhq app's urls.py module is missing.")
    
    def test_is_playerhq_app_configured(self):
        """
        adding the new playerhq app to INSTALLED_APPS list?
        """
        is_app_configured = 'playerhq' in settings.INSTALLED_APPS
        
        self.assertTrue(is_app_configured, f"{FAILURE_HEADER}The playerhq app is missing from your setting's INSTALLED_APPS list.")    
        
        
class TestIndex(TestCase):
    """
    Testing the basics of index view and URL mapping.
    """
    def setUp(self):
        self.views_module = importlib.import_module('playerhq.views')
        self.views_module_listing = dir(self.views_module)
        
        self.project_urls_module = importlib.import_module('PLHQ.urls')
    
    def test_view_exists(self):
        
        name_exists = 'index' in self.views_module_listing
        is_callable = callable(self.views_module.index)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}The index() view for playerhq does not exist.{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check that you have created the index() view correctly.{FAILURE_FOOTER}")
    
    def test_mappings_exists(self):
        """
        Are the required URL mappings present and correct?
        """
        index_mapping_exists = False
        
        # This is overridden. We need to manually check it exists.
        for mapping in self.project_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'index':
                    index_mapping_exists = True
        
        self.assertTrue(index_mapping_exists, f"{FAILURE_HEADER}The index URL mapping could not be found.{FAILURE_FOOTER}")
        self.assertEquals(reverse('playerhq:index'), '/playerhq/', f"{FAILURE_HEADER}The index URL lookup failed. Check Rango's urls.py module.{FAILURE_FOOTER}")
    
class TestAbout(TestCase):
    """
    Tests to check the about view.
    """
    def setUp(self):
        self.views_module = importlib.import_module('playerhq.views')
        self.views_module_listing = dir(self.views_module)
    
    def test_view_exists(self):
        """
        Does the about() view exist in playerhq's views.py module?
        """
        name_exists = 'about' in self.views_module_listing
        is_callable = callable(self.views_module.about)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}We couldn't find the view for your about view!{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check you have defined your about() view correctly.{FAILURE_FOOTER}")
    
    def test_mapping_exists(self):
        """
        Checks whether the about view has the correct URL mapping.
        """
        self.assertEquals(reverse('playerhq:about'), '/playerhq/about/', f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")

    def test_response(self):
        """
        Checks whether the view returns the required string to the client.
        """
        response = self.client.get(reverse('playerhq:about'))
        
        self.assertEqual(response.status_code, 200, f"{FAILURE_HEADER}When requesting the about view, the server did not respond correctly {FAILURE_FOOTER}")
        
class TemplateTest(TestCase):
    """
    set templates, static files and media files up correctly,
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.templates_dir = os.path.join(self.project_base_dir, 'templates')
        self.playerhq_templates_dir = os.path.join(self.templates_dir, 'playerhq')
    
    def test_templates_directory_exists(self):
        """
        Does the templates/ directory exist?
        """
        directory_exists = os.path.isdir(self.templates_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Your project's templates directory does not exist.{FAILURE_FOOTER}")
    
    def test_rango_templates_directory_exists(self):
        """
        Does the templates/playerhq/ directory exist?
        """
        directory_exists = os.path.isdir(self.playerhq_templates_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}The playerhq templates directory does not exist.{FAILURE_FOOTER}")
    
    def test_template_dir_setting(self):
        """
        Does the TEMPLATE_DIR setting exist, and does it point to the right directory?
        """
        variable_exists = 'TEMPLATE_DIR' in dir(settings)
        self.assertTrue(variable_exists, f"{FAILURE_HEADER}Your settings.py module does not have the variable TEMPLATE_DIR defined!{FAILURE_FOOTER}")
        
        template_dir_value = os.path.normpath(settings.TEMPLATE_DIR)
        template_dir_computed = os.path.normpath(self.templates_dir)
        self.assertEqual(template_dir_value, template_dir_computed, f"{FAILURE_HEADER}Your TEMPLATE_DIR setting does not point to the expected path.{FAILURE_FOOTER}")
    
    def test_template_lookup_path(self):
        """
        Does the TEMPLATE_DIR value appear within the lookup paths for templates?
        """
        lookup_list = settings.TEMPLATES[0]['DIRS']
        found_path = False
        
        for entry in lookup_list:
            entry_normalised = os.path.normpath(entry)
            
            if entry_normalised == os.path.normpath(settings.TEMPLATE_DIR):
                found_path = True
        
        self.assertTrue(found_path, f"{FAILURE_HEADER}Your project's templates directory is not listed in the TEMPLATES>DIRS lookup list. Check your settings.py module.{FAILURE_FOOTER}")
    
    def test_templates_exist(self):
        """
        Do the index.html and about.html templates exist in the correct place?
        """
        index_path = os.path.join(self.playerhq_templates_dir, 'index.html')
        about_path = os.path.join(self.playerhq_templates_dir, 'about.html')
        add_game = os.path.join(self.playerhq_templates_dir, 'addGame.html')
        base = os.path.join(self.playerhq_templates_dir, 'base.html')
        category = os.path.join(self.playerhq_templates_dir, 'category.html')
        game = os.path.join(self.playerhq_templates_dir, 'game.html')
        login = os.path.join(self.playerhq_templates_dir, 'login.html')
        sign_up = os.path.join(self.playerhq_templates_dir, 'signup.html')
        
        self.assertTrue(os.path.isfile(index_path), f"{FAILURE_HEADER}Your index.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(about_path), f"{FAILURE_HEADER}Your about.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(add_game), f"{FAILURE_HEADER}Your add_game.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(base), f"{FAILURE_HEADER}Your base.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(category), f"{FAILURE_HEADER}Your category.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(game), f"{FAILURE_HEADER}Your game.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(login), f"{FAILURE_HEADER}Your login.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(sign_up), f"{FAILURE_HEADER}Your sign_up.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        
        
class IndexPageTests(TestCase):
    """
    A series of tests to ensure that the index page/view has been updated to work with templates.
    """
    def setUp(self):
        self.response = self.client.get(reverse('playerhq:index'))
    
    def test_index_uses_template(self):
        """
        Checks whether the index view uses a template -- and the correct one!
        """
        self.assertTemplateUsed(self.response, 'playerhq/index.html', f"{FAILURE_HEADER}Your index() view does not use the expected index.html template.{FAILURE_FOOTER}")
    
    def test_index_starts_with_doctype(self):
        """
        Is the <!DOCTYPE html> declaration on the first line of the index.html template?
        """
        self.assertTrue(self.response.content.decode().startswith('<!DOCTYPE html>'), f"{FAILURE_HEADER}Your index.html template does not start with <!DOCTYPE html> -- this is requirement of the HTML specification.{FAILURE_FOOTER}")
    
class StaticMediaTests(TestCase):
    """
    A series of tests to check whether static files and media files have been setup and used correctly.
    Also tests for the two required files -- rango.jpg and cat.jpg.
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.static_dir = os.path.join(self.project_base_dir, 'static')
        self.media_dir = os.path.join(self.project_base_dir, 'media')
    
    def test_does_static_directory_exist(self):
        """
        Tests whether the static directory exists in the correct location -- and the images subdirectory.
        Also checks for the presence of rango.jpg in the images subdirectory.
        """
        does_static_dir_exist = os.path.isdir(self.static_dir)
        does_images_static_dir_exist = os.path.isdir(os.path.join(self.static_dir, 'images'))
        does_logo_jpg_exist = os.path.isfile(os.path.join(self.static_dir, 'images', 'new22.png'))
        
        self.assertTrue(does_static_dir_exist, f"{FAILURE_HEADER}The static directory was not found in the expected location. Check the instructions in the book, and try again.{FAILURE_FOOTER}")
        self.assertTrue(does_images_static_dir_exist, f"{FAILURE_HEADER}The images subdirectory was not found in your static directory.{FAILURE_FOOTER}")
        self.assertTrue(does_logo_jpg_exist, f"{FAILURE_HEADER}We couldn't locate the rango.jpg image in the /static/images/ directory. If you think you've included the file, make sure to check the file extension. Sometimes, a JPG can have the extension .jpeg. Be careful! It must be .jpg for this test.{FAILURE_FOOTER}")
    
    def test_does_media_directory_exist(self):
        """
        Tests whether the media directory exists in the correct location.
        Also checks for the presence of cat.jpg.
        """
        does_media_dir_exist = os.path.isdir(self.media_dir)
        does_TLOU_jpg_exist = os.path.isfile(os.path.join(self.media_dir, 'TLOU.jpg'))
        does_batman_jpg_exist = os.path.isfile(os.path.join(self.media_dir, 'batman.jpg'))
        
        self.assertTrue(does_media_dir_exist, f"{FAILURE_HEADER}We couldn't find the /media/ directory in the expected location. Make sure it is in your project directory (at the same level as the manage.py module).{FAILURE_FOOTER}")
        self.assertTrue(does_TLOU_jpg_exist, f"{FAILURE_HEADER}We couldn't find the cat.jpg image in /media/. Check the file extension; this is a common pitfall. It should .jpg. Not .png, .gif, or .jpeg!{FAILURE_FOOTER}")
        self.assertTrue(does_batman_jpg_exist, f"{FAILURE_HEADER}We couldn't find the cat.jpg image in /media/. Check the file extension; this is a common pitfall. It should .jpg. Not .png, .gif, or .jpeg!{FAILURE_FOOTER}")
    
    def test_static_and_media_configuration(self):
        """
        Performs a number of tests on your Django project's settings in relation to static files and user upload-able files..
        """
        static_dir_exists = 'STATIC_DIR' in dir(settings)
        self.assertTrue(static_dir_exists, f"{FAILURE_HEADER}Your settings.py module does not have the variable STATIC_DIR defined.{FAILURE_FOOTER}")
        
        expected_path = os.path.normpath(self.static_dir)
        static_path = os.path.normpath(settings.STATIC_DIR)
        self.assertEqual(expected_path, static_path, f"{FAILURE_HEADER}The value of STATIC_DIR does not equal the expected path. It should point to your project root, with 'static' appended to the end of that.{FAILURE_FOOTER}")
        
        staticfiles_dirs_exists = 'STATICFILES_DIRS' in dir(settings)
        self.assertTrue(staticfiles_dirs_exists, f"{FAILURE_HEADER}The required setting STATICFILES_DIRS is not present in your project's settings.py module. Check your settings carefully. So many students have mistyped this one.{FAILURE_FOOTER}")
        self.assertEqual([static_path], settings.STATICFILES_DIRS, f"{FAILURE_HEADER}Your STATICFILES_DIRS setting does not match what is expected. Check your implementation against the instructions provided.{FAILURE_FOOTER}")
        
        staticfiles_dirs_exists = 'STATIC_URL' in dir(settings)
        self.assertTrue(staticfiles_dirs_exists, f"{FAILURE_HEADER}The STATIC_URL variable has not been defined in settings.py.{FAILURE_FOOTER}")
        self.assertEqual('/static/', settings.STATIC_URL, f"{FAILURE_HEADER}STATIC_URL does not meet the expected value of /static/. Make sure you have a slash at the end!{FAILURE_FOOTER}")
        
        media_dir_exists = 'MEDIA_DIR' in dir(settings)
        self.assertTrue(media_dir_exists, f"{FAILURE_HEADER}The MEDIA_DIR variable in settings.py has not been defined.{FAILURE_FOOTER}")
        
        expected_path = os.path.normpath(self.media_dir)
        media_path = os.path.normpath(settings.MEDIA_DIR)
        self.assertEqual(expected_path, media_path, f"{FAILURE_HEADER}The MEDIA_DIR setting does not point to the correct path. Remember, it should have an absolute reference to tango_with_django_project/media/.{FAILURE_FOOTER}")
        
        media_root_exists = 'MEDIA_ROOT' in dir(settings)
        self.assertTrue(media_root_exists, f"{FAILURE_HEADER}The MEDIA_ROOT setting has not been defined.{FAILURE_FOOTER}")
        
        media_root_path = os.path.normpath(settings.MEDIA_ROOT)
        self.assertEqual(media_path, media_root_path, f"{FAILURE_HEADER}The value of MEDIA_ROOT does not equal the value of MEDIA_DIR.{FAILURE_FOOTER}")
        
        media_url_exists = 'MEDIA_URL' in dir(settings)
        self.assertTrue(media_url_exists, f"{FAILURE_HEADER}The setting MEDIA_URL has not been defined in settings.py.{FAILURE_FOOTER}")
        
        media_url_value = settings.MEDIA_URL
        self.assertEqual('/media/', media_url_value, f"{FAILURE_HEADER}Your value of the MEDIA_URL setting does not equal /media/. Check your settings!{FAILURE_FOOTER}")
    
    def test_context_processor_addition(self):
        """
        Checks to see whether the media context_processor has been added to your project's settings module.
        """
        context_processors_list = settings.TEMPLATES[0]['OPTIONS']['context_processors']
        self.assertTrue('django.template.context_processors.media' in context_processors_list, f"{FAILURE_HEADER}The 'django.template.context_processors.media' context processor was not included. Check your settings.py module.{FAILURE_FOOTER}")
                
        
class AboutTests(TestCase):
    
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.template_dir = os.path.join(self.project_base_dir, 'templates', 'playerhq')
        self.about_response = self.client.get(reverse('playerhq:about'))
    
    def test_about_template_exists(self):
        """
        Tests the about template -- if it exists, and whether or not the about() view makes use of it.
        """
        template_exists = os.path.isfile(os.path.join(self.template_dir, 'about.html'))
        self.assertTrue(template_exists, f"{FAILURE_HEADER}The about.html template was not found in the expected location.{FAILURE_FOOTER}")
    
    def test_about_uses_template(self):
        """
        Checks whether the index view uses a template -- and the correct one!
        """
        self.assertTemplateUsed(self.about_response, 'playerhq/about.html', f"{FAILURE_HEADER}The about() view does not use the about.html template.{FAILURE_FOOTER}")
    
    def test_about_starts_with_doctype(self):
        """
        Is the <!DOCTYPE html> declaration on the first line of the about.html template?
        """
        self.assertTrue(self.about_response.content.decode().startswith('<!DOCTYPE html>'), f"{FAILURE_HEADER}Your about.html template does not start with <!DOCTYPE html> -- this is requirement of the HTML specification.{FAILURE_FOOTER}")
    

class DatabaseConfigurationTests(TestCase):
    """
    Is your database configured
    """
    def setUp(self):
        pass
    
    def does_gitignore_include_database(self, path):
        """
        Takes the path to a .gitignore file, and checks to see whether the db.sqlite3 database is present in that file.
        """
        f = open(path, 'r')
        
        for line in f:
            line = line.strip()
            
            if line.startswith('db.sqlite3'):
                return True
        
        f.close()
        return False
    
    def test_databases_variable_exists(self):
        """
        Does the DATABASES settings variable exist, and does it have a default configuration?
        """
        self.assertTrue(settings.DATABASES, f"{FAILURE_HEADER}Your project's settings module does not have a DATABASES variable, which is required. Check the start of Chapter 5.{FAILURE_FOOTER}")
        self.assertTrue('default' in settings.DATABASES, f"{FAILURE_HEADER}You do not have a 'default' database configuration in your project's DATABASES configuration variable. Check the start of Chapter 5.{FAILURE_FOOTER}")
    
    def test_gitignore_for_database(self):
        """
        If you are using a Git repository and have set up a .gitignore, checks to see whether the database is present in that file.
        """
        git_base_dir = os.popen('git rev-parse --show-toplevel').read().strip()
        
        if git_base_dir.startswith('fatal'):
            warnings.warn("You don't appear to be using a Git repository for your codebase. Although not strictly required, it's *highly recommended*. Skipping this test.")
        else:
            gitignore_path = os.path.join(git_base_dir, '.gitignore')
            
            if os.path.exists(gitignore_path):
                self.assertTrue(self.does_gitignore_include_database(gitignore_path), f"{FAILURE_HEADER}Your .gitignore file does not include 'db.sqlite3' -- you should exclude the database binary file from all commits to your Git repository.{FAILURE_FOOTER}")
            else:
                warnings.warn("You don't appear to have a .gitignore file in place in your repository. We ask that you consider this! Read the Don't git push your Database paragraph in Chapter 5.")        
    
class ModelTests(TestCase):
    """
    Are the models set up correctly, and do all the required attributes exist?
    """
    def setUp(self):
        category_py = Reviews.objects.get_or_create(GameName='The Last Of Us', ReviewerName='Saad', Review='Adolescents have it particularly tough in the zombie apocalypse. Everyone around them is obsessed with survival--which is certainly understandable--but every ounce of a teenagers instincts is pushing him or her toward goofing off', Graphics=5, Storyline=5, Gameplay=5)
        
        Games.objects.get_or_create(GameName='The Witcher 3', GameRating=5, Gamedescription='The Witcher 3: Wild Hunt is a 2015 action role-playing game developed and published by CD Projekt and based on The Witcher series of fantasy novels by Andrzej Sapkowski. It is the sequel to the 2011 game The Witcher 2: Assassins of Kings, played in an open world with a third-person perspective.', GameCategory='RPGs', GameImage='TheWitcher3.jpg')
        
    def test_category_model(self):
        """
        Runs a series of tests on the Category model.
        Do the correct attributes exist?
        """
        category_py = Reviews.objects.get(GameName='The Last Of Us')
        self.assertEqual(category_py.ReviewerName, 'Saad', f"{FAILURE_HEADER}Tests on the Category model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(category_py.Gameplay, 5, f"{FAILURE_HEADER}Tests on the Category model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
    
    def test_page_model(self):
        """
        Runs some tests on the Page model.
        Do the correct attributes exist?
        """
        games = Games.objects.get(GameName='The Witcher 3')
        self.assertEqual(games.GameImage, 'TheWitcher3.jpg', f"{FAILURE_HEADER}Tests on the Page model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(games.GameRating, 5, f"{FAILURE_HEADER}Tests on the Page model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(games.GameCategory, 'RPGs', f"{FAILURE_HEADER}Tests on the Page model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")

class AdminInterfaceTests(TestCase):
    """
    A series of tests that examines the authentication functionality (for superuser creation and logging in), and admin interface changes.
    Have all the admin interface tweaks been applied, and have the two models been added to the admin app?
    """
    def setUp(self):
        """
        Create a superuser account for use in testing.
        Logs the superuser in, too!
        """
        User.objects.create_superuser('testAdmin', 'email@email.com', 'adminPassword123')
        self.client.login(username='testAdmin', password='adminPassword123')
        
        category_py = Reviews.objects.get_or_create(GameName='The Last Of Us', ReviewerName='Saad', Review='Adolescents have it particularly tough in the zombie apocalypse. Everyone around them is obsessed with survival--which is certainly understandable--but every ounce of a teenagers instincts is pushing him or her toward goofing off', Graphics=5, Storyline=5, Gameplay=5)
        
        Games.objects.get_or_create(GameName='The Witcher 3', GameRating=5, Gamedescription='The Witcher 3: Wild Hunt is a 2015 action role-playing game developed and published by CD Projekt and based on The Witcher series of fantasy novels by Andrzej Sapkowski. It is the sequel to the 2011 game The Witcher 2: Assassins of Kings, played in an open world with a third-person perspective.', GameCategory='RPGs', GameImage='TheWitcher3.jpg')
    
    def test_admin_interface_accessible(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200, f"{FAILURE_HEADER}The admin interface is not accessible. Check that you didn't delete the 'admin/' URL pattern in your project's urls.py module.{FAILURE_FOOTER}")
    
    def test_models_present(self):
        """
        Checks whether the two models are present within the admin interface homepage -- and whether Rango is listed there at all.
        """
        response = self.client.get('/admin/')
        response_body = response.content.decode()
        
        # Check each model is present.
        self.assertTrue('Games' in response_body, f"{FAILURE_HEADER}The Category model was not found in the admin interface. If you did add the model to admin.py, did you add the correct plural spelling (Categories)?{FAILURE_FOOTER}")
        self.assertTrue('Reviews' in response_body, f"{FAILURE_HEADER}The Page model was not found in the admin interface. If you did add the model to admin.py, did you add the correct plural spelling (Pages)?{FAILURE_FOOTER}")
        
class PopulationScriptTests(TestCase):
    """
    Tests whether the population script puts the expected data into a test database.
    All values that are explicitly mentioned in the book are tested.
    Expects that the population script has the populate() function, as per the book!
    """
    def setUp(self):
        """
        Imports and runs the population script, calling the populate() method.
        """
        try:
            import populationscript
        except ImportError:
            raise ImportError(f"{FAILURE_HEADER}The Chapter 5 tests could not import the populate_rango. Check it's in the right location (the first tango_with_django_project directory).{FAILURE_FOOTER}")
        
        if 'populate' not in dir(populationscript):
            raise NameError(f"{FAILURE_HEADER}The populate() function does not exist in the populate_rango module. This is required.{FAILURE_FOOTER}")
        
        # Call the population script -- any exceptions raised here do not have fancy error messages to help readers.
        populationscript.populate()
    
    def test_categories(self):
        categories = Categories.objects.filter()
        categories_len = len(categories)
        categories_strs = map(str, categories)
        
        self.assertEqual(categories_len, 4, f"{FAILURE_HEADER}Expecting 3 categories to be created from the populate_rango module; found {categories_len}.{FAILURE_FOOTER}")
        self.assertTrue('RPGs' in categories_strs, f"{FAILURE_HEADER}The category 'Python' was expected but not created by populate_rango.{FAILURE_FOOTER}")
        self.assertTrue('SuperHero' in categories_strs, f"{FAILURE_HEADER}The category 'Django' was expected but not created by populate_rango.{FAILURE_FOOTER}")
        self.assertTrue('Others' in categories_strs, f"{FAILURE_HEADER}The category 'Other Frameworks' was expected but not created by populate_rango.{FAILURE_FOOTER}")
    
    
class IndexViewTests(TestCase):
    """
    A series of tests that examine the behaviour of the index view and its corresponding template.
    Tests to see if the context dictionary is correctly formed, and whether the response is correct, too.
    """
    def setUp(self):
        populate()
        self.response = self.client.get(reverse('playerhq:index'))
        self.content = self.response.content.decode()
    
    def test_template_filename(self):
        """
        Still using a template?
        """
        self.assertTemplateUsed(self.response, 'playerhq/index.html', f"{FAILURE_HEADER}Are you using index.html for your index() view? Why not?!{FAILURE_FOOTER}")

    def test_index_context_dictionary(self):
        """
        Runs some assertions to check if the context dictionary has the correct key/value pairings.
        """
        games = list(Games.objects.order_by('-GameRating')[:5])
        categories = list(Categories.objects.order_by('catName'))
        topGame = Games.objects.order_by('-GameRating').first()

        # Does the boldmessage still exist? A surprising number of people delete it here.
        self.assertTrue('topGame' in self.response.context, f"{FAILURE_HEADER}The 'topgame' variable couldn't be found in the context dictionary for the index() view. Did you delete it?{FAILURE_FOOTER}")
        self.assertEquals(topGame, self.response.context['topGame'], f"{FAILURE_HEADER}Where did topgame go in the index() view?{FAILURE_FOOTER}")

        # Check that categories exists in the context dictionary, that it references the correct objects, and the order is spot on.
        self.assertTrue('categories' in self.response.context, f"{FAILURE_HEADER}We couldn't find a 'categories' variable in the context dictionary within the index() view. Check the instructions in the book, and try again.{FAILURE_FOOTER}")
        self.assertEqual(type(self.response.context['categories']), QuerySet, f"{FAILURE_HEADER}The 'categories' variable in the context dictionary for the index() view didn't return a QuerySet object as expected.{FAILURE_FOOTER}")
        self.assertEqual(categories, list(self.response.context['categories']), f"{FAILURE_HEADER}Incorrect categories/category order returned from the index() view's context dictionary -- expected  got .{FAILURE_FOOTER}")

        # Repeat, but for the pages variable. Note that order cannot be verfified (no instructions in book to use certain values).
        self.assertTrue('games' in self.response.context, f"{FAILURE_HEADER}We couldn't find a  variable in the index() view's context dictionary. Did you complete the Chapter 6 exercises?{FAILURE_FOOTER}")
        self.assertEqual(type(self.response.context['games']), QuerySet, f"{FAILURE_HEADER}The variable in the index() view's context dictionary doesn't return a QuerySet as expected.{FAILURE_FOOTER}")
        self.assertEqual(games, list(self.response.context['games']), f"{FAILURE_HEADER}The  context dictionary variable for the index() view didn't return the QuerySet we were expectecting:  expected. Did you apply the correct ordering to the filtered results?{FAILURE_FOOTER}")

class NoItemsIndexViewTests(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('playerhq:index'))
        self.content = self.response.content.decode()

    def test_empty_index_context_dictionary(self):
        """
        Runs assertions on the context dictionary, ensuring the categories and pages variables exist, but return empty (zero-length) QuerySet objects.
        """
        self.assertTrue('categories' in self.response.context, f"{FAILURE_HEADER}The 'categories' variable does not exist in the context dictionary for index(). (Empty check){FAILURE_FOOTER}")
        self.assertEqual(type(self.response.context['categories']), QuerySet, f"{FAILURE_HEADER}The ' variable in the context dictionary for index() does yield a QuerySet object. (Empty check){FAILURE_FOOTER}")
        self.assertEqual(len(self.response.context['categories']), 0, f"{FAILURE_HEADER}The variable in the context dictionary for index() is not empty. (Empty check){FAILURE_FOOTER}")

        self.assertTrue('games' in self.response.context, f"{FAILURE_HEADER}The 'pages' variable does not exist in the context dictionary for index(). (Empty check){FAILURE_FOOTER}")
        self.assertEqual(type(self.response.context['games']), QuerySet, f"{FAILURE_HEADER}{FAILURE_FOOTER}")
        self.assertEqual(len(self.response.context['games']), 0, f"{FAILURE_HEADER}{FAILURE_FOOTER}")
    
class BadCategoryViewTests(TestCase):
    """
    A few tests to examine some edge cases where categories do not exist, for example.
    """
    def test_malformed_url(self):
        """
        Tests to see whether the URL patterns have been correctly entered; many students have fallen over at this one.
        Somehow.
        """
        response = self.client.get('/playerhq/category/')
        self.assertTrue(response.status_code == 404, f"{FAILURE_HEADER}The URL /playerhq/category/ should return a status of code of 404 (not found). Check to see whether you have correctly entered your urlpatterns.{FAILURE_FOOTER}")


class FormClassTests(TestCase):
    """
    Do the Form classes exist, and do they contain the correct instance variables?
    """
    def test_module_exists(self):
        """
        Tests that the forms.py module exists in the expected location.
        """
        project_path = os.getcwd()
        rango_app_path = os.path.join(project_path, 'playerhq')
        forms_module_path = os.path.join(rango_app_path, 'forms.py')

        self.assertTrue(os.path.exists(forms_module_path), f"{FAILURE_HEADER}We couldn't find Rango's new forms.py module. This is required to be created at the top of Section 7.2. This module should be storing your two form classes.{FAILURE_FOOTER}")
    
    def test_category_form_class(self):
        """
        Does the CategoryForm implementation exist, and does it contain the correct instance variables?
        """
        # Check that we can import CategoryForm.
        import playerhq.forms
        self.assertTrue('GameForm' in dir(playerhq.forms), f"{FAILURE_HEADER}The class CategoryForm could not be found in Rango's forms.py module. Check you have created this class in the correct location, and try again.{FAILURE_FOOTER}")

        from playerhq.forms import GameForm
        category_form = GameForm()

        # Do you correctly link Category to CategoryForm?
        self.assertEqual(type(category_form.__dict__['instance']), Games, f"{FAILURE_HEADER}The CategoryForm does not link to the Category model. Have a look in the CategoryForm's nested Meta class for the model attribute.{FAILURE_FOOTER}")

        # Now check that all the required fields are present, and of the correct form field type.
        fields = category_form.fields

        expected_fields = {
            'GameName': django_fields.CharField,
            'GameImage': django_fields.ImageField,
            'Gamedescription': django_fields.CharField,
            'GameRating' : django_fields.IntegerField,
            'GameCategory': django_fields.CharField,
        }

        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]

            self.assertTrue(expected_field_name in fields.keys(), f"{FAILURE_HEADER}The field '{expected_field_name}' was not found in your CategoryForm implementation. Check you have all required fields, and try again.{FAILURE_FOOTER}")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"{FAILURE_HEADER}The field '{expected_field_name}' in CategoryForm was not of the expected type '{type(fields[expected_field_name])}'.{FAILURE_FOOTER}")

class CPageFormAncillaryTests(TestCase):
    """
    Performs a series of tests to check the response of the server under different conditions when adding pages.
    """
    
    def test_add_page_template(self):
        """
        Checks whether a template was used for the add_page() view.
        """
        populate()
        response = self.client.get(reverse('playerhq:game', kwargs={'game_name_slug': 'RPGs'}))
        self.assertTemplateUsed(response, 'playerhq/game.html', f"{FAILURE_HEADER}The add_page.html template is not used for the add_page() view. The specification requires this.{FAILURE_FOOTER}")

    def test_add_page_functionality(self):
        """
        Given a category and a new page, tests whether the functionality implemented works as expected.
        """
        populate()

        response = self.client.post(reverse('playerhq:game', kwargs={'game_name_slug': 'RPGs'}),
                                            {'GameName': 'New webpage', 'Gamedescription': 'www.google.com', 'GameRating': 0})

        python_pages = Games.objects.filter(GameName='BioShock')
        self.assertEqual(len(python_pages), 0, f"{FAILURE_HEADER}When adding a new page to a category with the add_page form, the new Page object that we were expecting wasn't created. Check your add_page() view for mistakes, and try again. You need to call .save() on the page you create!{FAILURE_FOOTER}")

class TemplateTests(TestCase):
    """
    I don't think it's possible to test every aspect of templates from this chapter without delving into some crazy string checking.
    So, instead, we can do some simple tests here: check that the base template exists, and that each page in the templates/rango directory has a title block.
    Based on the idea by Gerardo -- beautiful idea, cheers big man.
    """
    def get_template(self, path_to_template):
        """
        Helper function to return the string representation of a template file.
        """
        f = open(path_to_template, 'rb')
        template_str = ""

        for line in f:
            template_str = f"{template_str}{line}"

        f.close()
        return template_str
    
    def test_base_template_exists(self):
        """
        Tests whether the base template exists.
        """
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'playerhq', 'base.html')
        self.assertTrue(os.path.exists(template_base_path), f"{FAILURE_HEADER}We couldn't find the new base.html template that's required in the templates/rango directory. Did you create the template in the right place?{FAILURE_FOOTER}")