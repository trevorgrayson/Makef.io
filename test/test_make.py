from make import Makefile

MAKEFILE = """
test: deps1 deps2
	./test

clean: 
	rm -rf garbage

""".split("\n")

MAKEFILE2 = """
boom:
	punch
""".split("\n")

class TestMakefile:
    def test_parse(self):
        mk = Makefile.parse(MAKEFILE)

        assert isinstance(mk, Makefile)
        assert list(mk.targets.keys()) == ['test', 'clean']
        assert mk.deps['test'] == ' deps1 deps2'
        assert mk.targets['test'] == ['	./test', '']

    def test_merge(self):
        a = Makefile.parse(MAKEFILE) 
        b = Makefile.parse(MAKEFILE2)

        mk = a + b

        assert isinstance(mk, Makefile)
        assert list(mk.targets.keys()) == ['test', 'clean', 'boom']
        assert mk.deps['test'] == ' deps1 deps2'
        assert mk.targets['test'] == ['	./test', '']
        assert mk.targets['boom'] == ['	punch', '']
