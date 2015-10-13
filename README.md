# python-intro-course-cern
Code snippets and notes from the Hands-on introduction course to Python by Jacek Generowicz, held at CERN.

http://jacek.web.cern.ch/jacek/courses/python-intro/course.html

## cloning & pushing from the course computer(s)
(Hello future self!)

(Thanks, past self!)

set the `user.name` and `user.email` config variables for the repository:

* `git config --file .git/config user.name "otron"`
* `git config --file .git/config user.email EMAILS_YO`

### Cloning
`git clone https://otron@github.com/otron/python-intro-course.git`

### Pushing
if you cloned it with the https read-only url (`https://github.com/...`) do:
`git remote set-url origin https://otron@github.com/otron/python-intro-course.git`
to fix it.

