from django.test import TestCase, Client,TransactionTestCase
from SWE573_Project.models import ArticleModel,ReportModel,TagModel
from django.db.utils import IntegrityError

class ArticleTestCase(TestCase):
    def setUp(self):
        ArticleModel.objects.create(title='article title', body="article body", authors='author', pmid='1234', keywords='keyword1', slug='testslug')
        ArticleModel.objects.create(title='article 1', body='body 1', authors='author1', pmid='5678', keywords='keyword1', slug='testslug1')

    def test_article_is_created_properly(self):
        article = ArticleModel.objects.get(slug='testslug')
        self.assertEqual(article.title, 'article title')
        self.assertEqual(article.body, 'article body')
        self.assertEqual(article.authors, 'author')
        self.assertEqual(article.pmid, '1234')
        self.assertEqual(article.keywords, 'keyword1')
    
    def test_same_article(self):
        with self.assertRaises(IntegrityError):
            ArticleModel.objects.create(title="article title", body="article body", authors='author', pmid='1234', keywords='keyword1', slug='testslug')

    def test_unique_field_pmid(self):
        with self.assertRaises(IntegrityError):
            ArticleModel.objects.create(title='article 2', body='body 2', authors='author2', pmid='5678', keywords='keyword2', slug='testslug')

class TagTestCase(TestCase):

    def setUp(self):
        TagModel.objects.create(name='testtag', url='testurl.com')

    def test_tag_is_created_properly(self):
        tag = TagModel.objects.get(name='testtag')
        self.assertEqual(tag.name, 'testtag')
        self.assertEqual(tag.url, 'testurl.com')

class ReportTestCase(TestCase):

    def setUp(self):
        ReportModel.objects.create(message='report test message')

    def test_report_created_properly(self):
        report = ReportModel.objects.get(message='report test message')
        self.assertEqual(report.message, 'report test message')
