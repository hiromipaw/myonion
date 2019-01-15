MyOnion is a proof of concept to run onion services into docker container from
your command line, via cli, or more simply via gui.


This project explore the idea of running ephemeral onion services on the Tor
network. Someone that may want to run an onion service to share websites or simple web
applications can use the MyOnion wrapper app to start a .onion from your computer
and share a static website or a web application.


Tor is an important tool providing privacy and anonymity online. The property of
anonymity itself is more than just providing an encrypted connection between the
source and the destination of a given conversation. Encryption only prevents the
content of the communication between Alice and Bob from becoming known.  There is
in fact a lot of information that can still be learned by just observing encrypted
communications. For example, it is always possible to guess certain information
by learning some properties of the conversation beyond just the content, such as
the length of the conversation, or who was involved, or even guessing a group of
people that communicate with a certain frequency. These properties are called
metadata and can be used to describe information even when the full data is not available.


Anonymity is a broad concept, and it can mean different things to different groups.
The main advertised property of the Tor network is that it provides strong
anonymity given a variety of people using the network. For the Tor network to
function properly and to satisfy users' needs, we need a certain degree of
diversity. We need diversity in the relays comprising the network and in the user
population sending traffic through it.  We want Tor to be able to reach and serve
a diverse population of users and use cases. We believe everyone should be able
to browse the web and enjoy privacy, independently of where they live and who they are.


The Tor network itself is only a part of what Tor is. Tor provides privacy at the
application level through the Tor Browser, and with .onion service Tor allows
users to hide their locations while offering various kinds of services, such as
web publishing or an instant messaging server. Using Tor "rendezvous points,"
other Tor users can connect to these .onion services, formerly known as hidden
services, each without knowing the other's network identity.


An .onion service needs to advertise its existence in the Tor network before
clients will be able to contact it. Therefore, the service randomly picks some
relays, builds circuits to them, and asks them to act as introduction points by
telling them its public key. By using a full Tor circuit, it's hard for anyone
to associate an introduction point with the .onion server's IP address. While the
introduction points and others are told the onion service's identity (public key),
 we don't want them to learn about the onion server's location (IP address).    


Because .onion services live on the Tor network, you do not need hosting or a
public ip address to offer some service via .onion address. This means .onion
services are a gateway to a decentralised, peer-to-peer internet, where you regain
control on the content you create and who you are sharing it with. The .onion is
hosted on your computer for the time you desire, allowing the people visiting your
site to remain anonymous, and also you. We believe anonymity to be very important
since it can free people, allowing them to decide how to expose themselves or to
make themselves visible on their own terms.
