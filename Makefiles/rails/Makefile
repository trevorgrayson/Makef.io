GEMDIR?=.gems

export GEM_HOME=$(GEMDIR)
export GEM_PATH=$(GEMDIR):.

test:
#	.gems/bin/rspec install
	bundle exec rspec $(TEST)
	touch .gems

compile:
	ruby --version
	bundle --path $(GEMDIR)

configure:
	# cp config/secrets.yml.example config/secrets.yml
	# bundle install
	rails db:create
	rails db:fetch_and_reload_main_db
	rails db:fetch_and_reload[152]

clean:
	rm -rf $(GEMDIR)

server:
	rails s

reloadDb:
	# rails db:destroy
	rails db:create

mysql:
	docker run --name rsapi-mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -p 3306:3306 -d mysql:5.6.46

.PHONY: test
