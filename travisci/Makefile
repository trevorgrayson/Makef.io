TRAVIS_SKEL?=travisci/.travis.skel.yml
TRAVIS_YML=.travis.yml
MAKEFILE?=Makefile

travisci: .travis.yml
.travis.yml: $(MAKEFILE)
	@cat $(TRAVIS_SKEL) > $(TRAVIS_YML)
	@echo "script:" >> $(TRAVIS_YML)
	@grep "[a-z]*:.*#cicd" Makefile  | cut -d: -f1 | sed -e "s/^/- make /" >> $(TRAVIS_YML)
	echo "updated $(TRAVIS_YML)"
