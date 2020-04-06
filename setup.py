from setuptools import setup


with open('requirements.txt') as f:
    reqs = f.read()

reqs = reqs.strip().split('\n')

install = [req for req in reqs if not req.startswith("git+git://")]
depends = [req.replace("git+git://","git+http://") for req in reqs if req.startswith("git+git://")]
license =  "".join(open("LICENSE").readlines())

setup(
    name='fever-scorer',
    version='0.0.0',
    author='James Thorne',
    author_email='james@jamesthorne.co.uk',
    url='https://jamesthorne.co.uk',
    description='Fact Extraction and VERification scorer',
    long_description="See https://github.com/sheffieldnlp/fever-scorer",
    license=license,
    package_dir={'fever': 'src/fever'},
    packages=['fever'],
    install_requires=install,
    dependency_links=depends,
)
