from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Course, Step


class CourseModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Regular Expressions",
            description="Learn to write regex in Python")

    def test_course_creation(self):
        self.assertLess(self.course.created_at, timezone.now())


class StepModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Learn to write tests in Python")

        self.step = Step.objects.create(
            title="Introduction to Doctests",
            description="Learn to write tests in your docstrings",
            course=self.course)

    def test_step_creation(self):
        self.assertEqual(self.step.order, 0)
        self.assertEqual(self.step.content, "")

    def test_step_link(self):
        self.assertEqual(self.step.course, self.course)


class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Learn to write tests in Python")
        self.course2 = Course.objects.create(
            title="New Course",
            description="A  new course")
        self.step = Step.objects.create(
            title="Introduction to Doctests",
            description="Learn to write tests in your docstrings",
            course=self.course)

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertContains(resp, self.course.title)

    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:detail', kwargs={'pk': self.course.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.course, resp.context['course'])
        self.assertNotEqual(self.course2, resp.context['course'])
        self.assertTemplateUsed(resp, 'courses/course_detail.html')
        self.assertContains(resp, self.step.title)


class StepViewsTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Django Forms",
            description="learn about forms in Django")
        self.step = Step.objects.create(
            title="Intro to forms",
            description="Learn the basics about forms in Django",
            course=self.course)
        self.step2 = Step.objects.create(
            title="Make a form",
            description="Make a basic form",
            course=self.course)

    def test_step_detail_view(self):
        resp = self.client.get(reverse('courses:step', kwargs={
            'course_pk': self.step.course.pk,
            'step_pk': self.step.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.step, resp.context['step'])
        self.assertNotEqual(self.step2, resp.context['step'])
        self.assertTemplateUsed(resp, 'courses/step_detail.html')
        self.assertContains(resp, self.step.title)

