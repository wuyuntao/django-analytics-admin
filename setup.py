# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages
from setuptools.command.test import test

class TestRunner(test):
    def run(self, *args, **kwargs):
        if self.distribution.install_requires:
            self.distribution.fetch_build_eggs(self.distribution.install_requires)
        if self.distribution.tests_require:
            self.distribution.fetch_build_eggs(self.distribution.tests_require)
        from runtests import runtests
        runtests()

setup(
    name='django-analytics-admin',
    version='0.1',
    description='An analytics service for Django admin.',
    long_description=open('README.rst', 'rt').read(),
    author='Wu Yuntao',
    author_email='wyt.brandon@gmail.com',
    license='MIT',
    url='https://github.com/wuyuntao/django-analytics-admin',
    packages=find_packages(),
    install_requires=[
    ],
    tests_require=[
        'django',
    ],
    include_package_data=True,
    test_suite = "analyticsadmin.tests",
    cmdclass={"test": TestRunner},
    classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
)
