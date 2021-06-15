from django.test import TestCase
from SWE573_Project.models import ArticleModel,ReportModel,TagModel
from django.utils import timezone
from django.db.utils import IntegrityError

class ArticleTestCase(TestCase):
    def setUp(self):
        ArticleModel.objects.create(title="article title", body="article body", authors='author', pmid='1234', keywords='keyword1', slug='testslug')

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








