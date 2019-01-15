FROM debian

MAINTAINER hiro <hiro@torproject.org>

RUN \
    apt-get update && \
    apt-get install -y nginx tor && \
    rm -rf /var/lib/apt/lists/* && \
    echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
    chown -R www-data:www-data /var/lib/nginx

COPY default /etc/nginx/sites-available/

# Define mountable directories.
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]

# Define working directory.
WORKDIR /etc/nginx

# Define default command.
CMD ["nginx"]

# Add user

RUN useradd -ms /bin/bash peer
RUN mkdir -p 700 /home/peer
RUN mkdir -p 700 /home/peer/web
COPY tor/torrc /etc/tor
RUN ln -s /home/peer/web /srv/web.myonion
RUN chown -R peer /home/peer

USER peer

WORKDIR /home/peer

CMD ["tor"]

VOLUME peer

EXPOSE 80
