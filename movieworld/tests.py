from django.test import TestCase
import os
from django.urls import reverse
from django.test import TestCase
from django.conf import settings

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

class Chapter4TemplatesStructureTests(TestCase):
    """
    Have you set templates, static files and media files up correctly, as per the book?
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.templates_dir = os.path.join(self.project_base_dir, 'templates')
        self.movieworld_templates_dir = os.path.join(self.templates_dir, 'movieworld')
    
    def test_templates_directory_exists(self):
        """
        Does the templates/ directory exist?
        """
        directory_exists = os.path.isdir(self.templates_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Your project's templates directory does not exist.{FAILURE_FOOTER}")
    
    def test_movieworld_templates_directory_exists(self):
        """
        Does the templates/movieworld/ directory exist?
        """
        directory_exists = os.path.isdir(self.movieworld_templates_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}The movieworld templates directory does not exist.{FAILURE_FOOTER}")
    
    def test_template_dir_setting(self):
        """
        Does the TEMPLATE_DIR setting exist, and does it point to the right directory?
        """
        variable_exists = 'TEMPLATE_DIR' in dir(settings)
        self.assertTrue(variable_exists, f"{FAILURE_HEADER}Your settings.py module does not have the variable TEMPLATE_DIR defined!{FAILURE_FOOTER}")
        
        template_dir_value = os.path.normpath(settings.TEMPLATE_DIR)
        template_dir_computed = os.path.normpath(self.templates_dir)
        self.assertEqual(template_dir_value, template_dir_computed, f"{FAILURE_HEADER}Your TEMPLATE_DIR setting does not point to the expected path. Check your configuration, and try again.{FAILURE_FOOTER}")
    
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
        index_path = os.path.join(self.movieworld_templates_dir, 'index.html')
        about_path = os.path.join(self.movieworld_templates_dir, 'about.html')
        
        self.assertTrue(os.path.isfile(index_path), f"{FAILURE_HEADER}Your index.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(about_path), f"{FAILURE_HEADER}Your about.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")


class Chapter4IndexPageTests(TestCase):
    """
    A series of tests to ensure that the index page/view has been updated to work with templates.
    Image tests are in the Chapter4StaticMediaTests suite.
    """
    def setUp(self):
        self.response = self.client.get(reverse('movieworld:index'))
    
    def test_index_uses_template(self):
        """
        Checks whether the index view uses a template -- and the correct one!
        """
        self.assertTemplateUsed(self.response, 'movieworld/index.html', f"{FAILURE_HEADER}Your index() view does not use the expected index.html template.{FAILURE_FOOTER}")
    
    
        

class Chapter4StaticMediaTests(TestCase):
    """
    A series of tests to check whether static files and media files have been setup and used correctly.
    Also tests for the two required files -- movieworld.jpg and cat.jpg.
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.static_dir = os.path.join(self.project_base_dir, 'static')
    
    def test_does_static_directory_exist(self):
        """
        Tests whether the static directory exists in the correct location -- and the img subdirectory.
        Also checks for the presence of movieworld.jpg in the img subdirectory.
        """
        does_static_dir_exist = os.path.isdir(self.static_dir)
        does_img_static_dir_exist = os.path.isdir(os.path.join(self.static_dir, 'img'))
        does_logo_jpg_exist = os.path.isfile(os.path.join(self.static_dir, 'img', 'logo.jpg'))
        
        self.assertTrue(does_static_dir_exist, f"{FAILURE_HEADER}The static directory was not found in the expected location. Check the instructions in the book, and try again.{FAILURE_FOOTER}")
        self.assertTrue(does_img_static_dir_exist, f"{FAILURE_HEADER}The img subdirectory was not found in your static directory.{FAILURE_FOOTER}")
        self.assertTrue(does_logo_jpg_exist, f"{FAILURE_HEADER}We couldn't locate the logo.jpg image in the /static/img/ directory. If you think you've included the file, make sure to check the file extension. Sometimes, a JPG can have the extension .jpeg. Be careful! It must be .jpg for this test.{FAILURE_FOOTER}")
    
    
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
        
        

class Chapter4ExerciseTests(TestCase):
    """
    A series of tests to ensure that the exercise listing at the end of Chapter 4 has been completed.
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.template_dir = os.path.join(self.project_base_dir, 'templates', 'movieworld')
        self.about_response = self.client.get(reverse('movieworld:about'))
    
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
        self.assertTemplateUsed(self.about_response, 'movieworld/about.html', f"{FAILURE_HEADER}The about() view does not use the about.html template.{FAILURE_FOOTER}")
  
    
    def test_about_contains_required_text(self):
        """
        Checks to see whether the required text is on the rendered about page.
        """
        required = [
            "Here is the about page.",
            "This website is a movie-rating platform."
        ]
        
        for required_str in required:
            self.assertTrue(required_str in self.about_response.content.decode(), f"{FAILURE_HEADER}The expected string '{required_str}' was not found in the rendered /movieworld/about/ response.{FAILURE_FOOTER}")
    
    def test_about_contains_logo(self):
        """
        Checks whether the rendered about view has the picture of movieworld.
        """
        required_str = f"<img src=\"{settings.STATIC_URL}img/logo.jpg\" alt=\"Movie World logo\" />"
        self.assertTrue(required_str in self.about_response.content.decode(), f"{FAILURE_HEADER}The HTML markup to include the image of movieworld in the about template was not found. It needs to match exactly what we are looking for. Check the book.{FAILURE_FOOTER}")
        
class Chapter8TemplateTests(TestCase):
    """
    I don't think it's possible to test every aspect of templates from this chapter without delving into some crazy string checking.
    So, instead, we can do some simple tests here: check that the base template exists, and that each page in the templates/movieworld directory has a title block.
    Based on the idea by Gerardo -- beautiful idea, cheers big man.
    """
    def get_template(self, path_to_template):
        """
        Helper function to return the string representation of a template file.
        """
        f = open(path_to_template, 'r')
        template_str = ""

        for line in f:
            template_str = f"{template_str}{line}"

        f.close()
        return template_str
    
    def test_base_template_exists(self):
        """
        Tests whether the base template exists.
        """
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'movieworld', 'base.html')
        self.assertTrue(os.path.exists(template_base_path), f"{FAILURE_HEADER}We couldn't find the new base.html template that's required in the templates/movieworld directory. Did you create the template in the right place?{FAILURE_FOOTER}")
    


 
    def test_for_links_in_base(self):
        """
        There should be three hyperlinks in base.html, as per the specification of the book.
        Check for their presence, along with correct use of URL lookups.
        """
        template_str = self.get_template(os.path.join(settings.TEMPLATE_DIR, 'movieworld', 'base.html'))

        look_for = [
            '<a href="{% url \'movieworld:about\' %}">About</a >',
            '<a href="{% url \'movieworld:index\' %}">Index</a>',
        ]
        
        for lookup in look_for:
            self.assertTrue(lookup in template_str, f"{FAILURE_HEADER}In base.html, we couldn't find the hyperlink '{lookup}'. Check your markup in base.html is correct and as written in the book.{FAILURE_FOOTER}")
