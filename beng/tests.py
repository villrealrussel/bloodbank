from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from beng.views import Russex
from django.urls import resolve
# from beng.models import Item
from beng.models import Item, Usseerr
from django.urls import reverse

class IndexTest(TestCase):

	def html_index_root_mainpage_pwede_din_homepage_basta(self):
		found = resolve('/')
		self.assertEqual(found.func, Firstpage)

		#REFACTOR
	def test_index_returns_correct_view(self):
		request = HttpRequest()
		response = Russex(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'weh.html')
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'weh.html')


		self.assertIn('<title>ATTENDANCE NATIN TO!</title>', html)
		self.assertTemplateUsed(response, 'weh.html')
		self.assertIn('<h1 style="color:dodgerblue;">WELCOME TO ATTENDANCE FORM</h1>', html)
		self.assertIn('<p><i>"Attend Today, Achive Tomorrow"</p></i>', html)
		self.assertIn('<label id="names">Name:</label>', html)
		self.assertIn('<input type="text" name="name" id="name" placeholder="Enter Name">', html)
		self.assertIn('<br>', html)
		self.assertIn('<center>', html)
		self.assertIn('</center>', html)

		self.assertIn('<label id="subjects">Subject:</label>', html)
		self.assertIn('<input type="text" name="subject" id="subject" placeholder="Enter Subject">', html)
		self.assertIn('<label id="names">Name:</label>', html)
		self.assertIn('<label id=bodies>Section:</label>', html)
		self.assertIn('<input type="text" name="body" id="body" placeholder="Enter body text">', html)
		self.assertIn('<p>GENDER:</p>', html)
		self.assertIn('<h3 style="color:blue;">', html)
		self.assertIn('<h3 style="color:red;">', html)
		self.assertIn('<input type ="radio" id="female" name="gender" value="FEMALE" required>', html)
		self.assertIn('<label id=dates>Date</label>', html)
		self.assertIn('<input type="date" name="date" id="date">', html)
		self.assertIn('<input type="submit" id="ggg">', html)
		self.assertTrue(html.strip().endswith('</html>'))
		self.assertTrue(html.strip().endswith('</html>')) 


class ListViewTest(TestCase):

	def test_uses_list_template(self):
		# student = User.objects.create()
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'weh.html')
	def test_uses_home_template(self):
		response = self.client.get('/next/')
		# self.assertTemplateUsed(response, 'dada.html')
	def test_displays_all_list_items(self):
		# student = Usseerr.objects.create()
		name = Item.objects.create(name='name')
		subject = Item.objects.create(subject='subject')
		body = Item.objects.create(body='body')
		# file = Details.objects.create(file='file.docx')
		gender = Item.objects.create(gender='gender')
		# select = Details.objects.create(select='select')
		response = self.client.get('/')
		self.assertIn('name', response.content.decode())
		self.assertIn('subject', response.content.decode())
		self.assertIn('body', response.content.decode())
		# self.assertIn('file', response.content.decode())
		self.assertIn('gender', response.content.decode())
		# self.assertIn('select', response.content.decode())
		name = Item.objects.get(name="name")
		subject = Item.objects.get(subject="subject")
		body = Item.objects.get(body="body")
		# file = Details.objects.get(file="file.docx")
		gender = Item.objects.get(gender="gender")
		# select = Details.objects.get(select="select")
		self.assertEqual(Item.objects.count(), 4)

class ORM(TestCase):
	def test_saving_koto(self):
		Item1 = Item()
		Item1.name = 'Russel'
		Item1.save()
		Item2 = Item()
		Item2.subject = 'Math'
		Item2.save()
		Item3 = Item()
		Item3.body = 'BSIE-ICT-3A'
		Item3.save()
		Item4 = Item()
		Item4.gender = 'female'
		Item4.save()
		# Item5 = Item()
		# Item5.date = '2012-11-02'
		# Item5.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 4)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		# save5 = saveall[4]
		self.assertEqual(Item1.name, 'Russel')
		self.assertEqual(Item2.subject, 'Math')
		self.assertEqual(Item3.body, 'BSIE-ICT-3A')
		self.assertEqual(Item4.gender, 'female')
		# self.assertEqual(Item5.date, '2012-11-02')

class ORM2(TestCase):
	def test_saving_koto(self):
		Item1 = Item()
		Item1.name = 'Adrianne'
		Item1.save()
		Item2 = Item()
		Item2.subject = 'English'
		Item2.save()
		Item3 = Item()
		Item3.body = 'BSIE-ICT-3B'
		Item3.save()
		Item4 = Item()
		Item4.gender = 'female'
		Item4.save()
		# Item5 = Item()
		# Item5.date = '2001-12-15'
		# Item5.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 4)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		# save5 = saveall[4]
		self.assertEqual(Item1.name, 'Adrianne')
		self.assertEqual(Item2.subject, 'English')
		self.assertEqual(Item3.body, 'BSIE-ICT-3B')
		self.assertEqual(Item4.gender, 'female')
		# self.assertEqual(Item5.date, '2001-12-15')

class Views(TestCase):
	def setUp(self):
		name = Item.objects.create()
		subject = Item.objects.create()
		body = Item.objects.create()
		# file = Details.objects.create()
		gender = Item.objects.create()
		# select = Details.objects.create()
		
		Item.objects.create(
			name = 'Russel',
			subject = 'Math', 
			body = 'BSIE-ICT-3A',
			gender = 'female',
			date = 'date',
			)
		self.client.post('/next/', name='Russel')
		response = self.client.post('/next/')
		
		self.assertEqual(Item.objects.count(), 5)

	def test_redirect_view(self):
			name = Item.objects.get(name="Russel")
			subject = Item.objects.get(subject="Math")
			body = Item.objects.get(body="BSIE-ICT-3A")
			gender = Item.objects.get(gender="female")
			# date = Item.objects.get(date="date") 
			response = self.client.post('/next/')
			# self.assertRedirects(response, '/next/')
		
class URL(TestCase):

	def urls(self):
		found = resolve()
		self.assertEqual(found.func, weh)
		self.assertEqual(found.func, NextPage)

		url = reverse('weh')
		self.assertEqual(resolve(url).func, weh)

		url = reverse('goods')
		self.assertEqual(resolve(url).func, NextPage) 

class Models(TestCase):

	def modelo(self, 
		students="test1", 
		select="test2", 
		gender="test3", 
		subject="test4", 
		file="test5", 
		date="test6", 
		grade="test7"):
		
		return Usseerr.objects.create()
		return Item.objects.create(
			students="students", 
			select="select", 
			gender="gender", 
			subject="subject", 
			file="file", 
			date="date", 
			grade="grade", )

	def test_whatever_creation(self):
		w = self.modelo()
		self.assertTrue(isinstance(w, Usseerr))
		self.assertFalse(isinstance(w, Item))


		# admit = Info.objects.get(admit="3")

# class Views(TestCase):
# 	def test_mo_lang(self):
#  		Item.objects.create(gender='gender', 
#  			subject='subject', name='name',
#  			body='body', date='2001-12-15')
#  		response = self.client.get('/app/views.Russex/')















# class RussexTest(TestCase):

# 	def managemanagemanage (self):
# 		found = resolve('/')
# 		self.assertEqual(found.func, Russex)

		
# 	def test_index_returns_correct_view(self):
# 		request = HttpRequest()
# 		response = Russex(request)
# 		response = self.client.get('/')
# 		self.assertTemplateUsed(response, 'weh.html')
# 		self.assertTrue(html.strip().startswith('<html>'))
# 		self.assertTemplateUsed(response, 'weh.html')
# 		self.assertIn('<title>ATTENDANCE NATIN TO!</title>', html)