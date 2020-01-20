start: server
server: compile
	npm start

install: compile
compile: node_modules
node_modules: package.json
	npm install
	@touch node_modules

test: compile
	npm test

package:
	npm run build

clean:
	npm clean
	rm -rf node_modules
