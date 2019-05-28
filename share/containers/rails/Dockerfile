FROM ruby:2.5
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client tor ruby-nokogiri

# Add user

RUN useradd -ms /bin/bash peer
RUN mkdir -p 700 /home/peer
RUN mkdir -p 700 /home/peer/web
COPY tor/torrc /etc/tor
RUN ln -s /home/peer/web /srv/web.myonion
RUN chown -R peer /home/peer

RUN mkdir /home/peer/myapp
WORKDIR /home/peer/myapp
COPY app/Gemfile /home/peer/myapp/Gemfile
COPY app/Gemfile.lock /home/peer/myapp/Gemfile.lock
COPY app /home/peer/myapp

WORKDIR /home/peer/myapp
RUN gem install nokogiri
RUN bundle update nokogiri
RUN bundle install --full-index

# Add a script to be executed every time the container starts.
COPY app/entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
RUN ln -s /home/peer/web /srv/web.myonion
RUN chown -R peer /home/peer

USER peer

ENTRYPOINT ["entrypoint.sh"]
EXPOSE 80

# Start the main process.
CMD ["rails", "server", "-b", "0.0.0.0"]
