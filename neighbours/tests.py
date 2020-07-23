from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Profile, Post,Comments,Neighbourhood,Business


class ProfileTestClass(TestCase):
  """  
  Test class that tests profile
  """
  def setUp(self):
    self.prof =Profile(profpic='test.jpg', bio='test bio', contact='j.yayah@gmail.com',user=1)

  def test_instance(self):
      self.assertTrue(isinstance(self.prof, Profile))

  def test_save_method(self):
      """
      Function to test that profile is being saved
      """
      self.prof.save_profile()
      profiles = Profile.objects.all()
      self.assertTrue(len(profiles) > 0)

  def test_delete_method(self):
      """
      Function to test that a profile can be deleted
      """
      self.prof.save_profile()
      self.prof.delete_profile()
      profiles = Profile.objects.all()
      self.assertTrue(len(profiles) == 0)

class PostTestClass(TestCase):
  """  
  Tests Post class and its functions
  """

  def test_instance(self):
      self.assertTrue(isinstance(self.post, Post))

  def test_save_method(self):
      """
      Testing whether a new post is being saved
      """
      self.project.save_post()
      posts = Post.objects.all()
      self.assertTrue(len(posts) > 0)

  def test_delete_method(self):
      """
      Function to test that a post can be deleted
      """
      self.post.save_post()
      self.post.delete_post()
      posts = Post.objects.all()
      self.assertTrue(len(posts) == 0)

class NeighbourhoodTestClass(TestCase):

        def setUp(self):
            self.new_neighbourhood=Neighbourhood(name='kampala',population=20101000)
        def tearDown(self):
            Neighbourhood.objects.all().delete()


        # test for instance
        def test_instance(self):
            self.assertTrue(isinstance(self.new_neighbourhood,Neighbourhood))
        # test for save method
        def test_save_neighbourhood(self):
            self.new_neighbourhood.create_neighbourhood()
            neighbourhood=Neighbourhood.objects.all()
            self.assertTrue(len(neighborhood)>0)
        def test_delete_neighbourhood(self):
            self.new_neighbourhood.create_neighbourhood()
            self.new_neighbourhood.delete_neighbourhood()
            neighbourhood=Neighbourhood.objects.all()
            self.assertEqual(len(neighbourhood),0)