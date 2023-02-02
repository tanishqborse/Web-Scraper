WEB SCRAPER PROJECT

WHAT APPLICATION DOES?
- This python program is a client side HTTP application that takes urls from command line and creates a IPV4 socket connection depending upon wether the url supplied was http or https, 
after the connection is established, it scrapes the http response to find and print all the external refernces in the given website. An external reference, is one that 
does not reside on the host (to the best of my knowledge) being accessed in the HTTP request.

-I developed the client side program in Python3 version 3.10.8 which makes HTTP requests and parses HTTP responses without using pre-made libraries for the given task. 

-The program is tested on Linux operating system and should work on ubuntu as well

CHALLENGES FACED
-I was not able to make the http requests without pre existing libraries, I got errors for using different user agents, tls versions, as well as for encoding methods.
-The external references on the website gave a lot of errors, and error handling was the most time consuming out of all.

HOW TO EXECUTE
-Download webscraper.py 
-On a command line enter
  Python3 webscraper.py "URL" 

For example-



Input
─(kali㉿kali)-[~/Desktop/webappsec/csec731-webscraper-tb7223]
└─$ python3 project.py https://www.rit.edu/  
www.rit.edu
/home/kali/Desktop/webappsec/csec731-webscraper-tb7223/project.py:27: DeprecationWarning: ssl.PROTOCOL_TLSv1_2 is deprecated
  context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

Output
External links:
https://www.drupal.org)
http://purl.org/rss/1.0/modules/content/
http://purl.org/dc/terms/
http://xmlns.com/foaf/0.1/
http://ogp.me/ns#
http://www.w3.org/2000/01/rdf-schema#
http://schema.org/
http://rdfs.org/sioc/ns#
http://rdfs.org/sioc/types#
http://www.w3.org/2004/02/skos/core#
http://www.w3.org/2001/XMLSchema#
https://www.drupal.org)"
https://66356383.global.siteimproveanalytics.io">
https://secure-ds.serving-sys.com">
https://bs.serving-sys.com">
https://connect.facebook.net">
https://www.facebook.com">
https://cdn.rit.edu">
https://www.googletagmanager.com">
https://www.google.com">
https://www.google-analytics.com">
https://s.ytimg.com">
https://kit.fontawesome.com">
https://kit-free.fontawesome.com">
http://www.w3.org/2000/svg">
https://www.googletagmanager.com/ns.html?id=GTM-TKNM7FX"
https://certified.rit.edu"
https://library.rit.edu/"
https://youtu.be/kCTyHAepE6Q"
https://certified.rit.edu"
https://library.rit.edu/"
https://youtu.be/kCTyHAepE6Q"
https://join.rit.edu/portal/ugrd_campusvisit">info
https://cdn.rit.edu/images/faces-of-rit/Nicole_Pannullo.jpg"
https://www.youtube.com/embed/6lwh3_ZDrIU?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1"
https://cdn.rit.edu/images/faces-of-rit/Faces-of-RIT---Aaron-Gordon-0-3-screenshot.jpg"
https://www.youtube.com/embed/t7lCIQXDC9g?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Rydrea_Walker.jpg"
https://www.youtube.com/embed/M9YN-4M_gvI?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1"
https://cdn.rit.edu/images/faces-of-rit/Shannon_McHale.jpg"
https://www.youtube.com/embed/Bd40IdvBxdA?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/4-1_0.png"
https://www.youtube.com/embed/afIOD3a9wpM?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/andow-nana-yaw.jpg"
https://www.youtube.com/embed/5RJkC4XcWEs?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Jess_Sudol.jpg"
https://www.youtube.com/embed/Zp-p82SPGb4?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/poornima-padmanabhan.jpg"
https://www.youtube.com/embed/3Rsl9SNf5aA?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/andrew-sevigny.jpg"
https://www.youtube.com/embed/3eieYDku1i8?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/zayneb-jaff.jpg"
https://www.youtube.com/embed/hQMml0N3Nr4?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/3.jpg"
https://www.youtube.com/embed/SUbPPATL9AA?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/John_Meyer.jpg"
https://www.youtube.com/embed/1DgvWGn3wVQ?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/claire-wilcox.jpg"
https://www.youtube.com/embed/lI0Pe6L6HIE?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Jonathan_Kruger.jpg"
https://www.youtube.com/embed/BmC5pxG_pbU?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/David_Even.jpg"
https://www.youtube.com/embed/0UpUKXc3YR0?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Ted-Canning.jpg"
https://www.youtube.com/embed/_j3y4SeqlHM?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Amelia_Hamilton_0.jpg"
https://www.youtube.com/embed/-kvsJCNk47c?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1"
https://cdn.rit.edu/images/faces-of-rit/Elizabeth_Ruder.jpg"
https://www.youtube.com/embed/dzrSTgNQXqg?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/elizabeth-moore.jpg"
https://www.youtube.com/embed/y4xFavk5OiE?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/shal-khazanchi.jpg"
https://www.youtube.com/embed/2w6QyVkiNdk?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Jessica_Wegman.jpg"
https://www.youtube.com/embed/cyykV9AhJ4g?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/sherwyn-millette.jpg"
https://www.youtube.com/embed/kCAvc66WzCY?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Tina_Goudreau_Collison.jpg"
https://www.youtube.com/embed/g3iz5JJxqmA?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/berta-rivera.jpg"
https://www.youtube.com/embed/NVknW1hYgY8?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Humza-Syed.jpg"
https://www.youtube.com/embed/clrFpldc5Wo?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Amanda_DeVito.jpg"
https://www.youtube.com/embed/99Gk2uqz0Yg?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/faces_of_rit_1.jpg"
https://www.youtube.com/embed/JdcrQ6aJXZk?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/2.jpg"
https://www.youtube.com/embed/vgt8N2p_0WI?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Michael_Oshetski.jpg"
https://www.youtube.com/embed/WhwHQi4OEuA?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Landyn_Hatch.jpg"
https://www.youtube.com/embed/9oj9z9jDcyc?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Fred_Beam.jpg"
https://www.youtube.com/embed/Iq6aLNOggLw?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1"
https://cdn.rit.edu/images/faces-of-rit/Corinne_Mendieta.jpg"
https://www.youtube.com/embed/voVl_-KwaFo?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Diamond_Guy.jpg"
https://www.youtube.com/embed/TUCSslGF-Z8?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/kate-ferguson.jpg"
https://www.youtube.com/embed/hZ5yXjCahYQ?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Jennifer-Wheeler-MD.jpg"
https://www.youtube.com/embed/ZGHS7rfOrHQ?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/harrison-canning.jpg"
https://www.youtube.com/embed/F2FXwdgvpFo?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Ashley_Kosak.jpg"
https://www.youtube.com/embed/qNSxXfrF6Pg?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Carlos_Diaz_Acosta.jpg"
https://www.youtube.com/embed/3IJ8YA-mgkc?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Evan_Hirsh.jpg"
https://www.youtube.com/embed/0uHoDQe_nG8?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/rachael-aho.jpg"
https://www.youtube.com/embed/AqRTv_ikklM?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Kimberley_Hedger.jpg"
https://www.youtube.com/embed/6VexwhdKsCA?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Kevin_Kha.jpg"
https://www.youtube.com/embed/av0sGUOiYO8?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/mari-jaye-blanchard.jpg"
https://www.youtube.com/embed/mTOHbiMAmMU?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Matt_Huenerfauth.jpg"
https://www.youtube.com/embed/ttzaDOuYPTc?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/solt-diana.jpg"
https://www.youtube.com/embed/fWMQkxsqJbc?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Lily_Lautenschlager.jpg"
https://www.youtube.com/embed/7nYiIFJVXJg?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Blair-Benson.jpg"
https://www.youtube.com/embed/ejDM1bKoYoQ?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/katherine-duffy.jpg"
https://www.youtube.com/embed/sktm3GaFAcY?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Barrington_Campbell.jpg"
https://www.youtube.com/embed/PedeabTZ9v8?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Becky_Jasen.jpg"
https://www.youtube.com/embed/vCkRTbLqLiY?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/Devin_Klibanow.jpg"
https://www.youtube.com/embed/1qqaWjTEUOw?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://cdn.rit.edu/images/faces-of-rit/remy-decausemaker.jpg"
https://www.youtube.com/embed/DWL7UWoTbNE?autoplay=1&autohide=1&showinfo=0&rel=0&enablejsapi=1&amp;cc_load_policy=1"
https://claws.rit.edu/photos/getphotoid.php?Client=Marketing&amp;UN=dcmpro&amp;HASH=30481cbf459cf736ae7263e6bb26ce9497c8cd72&amp;T=1674889298"
https://www.twitter.com/RITPresident"
https://walls.io/js/wallsio-widget-1.2.js';
https://walls.io/rit?nobackground=1&show_header=0';
http://www.facebook.com/RITfb"
http://instagram.com/RITTigers"
http://twitter.com/RITtigers"
https://www.tiktok.com/@rittigers"
http://www.youtube.com/user/RITUniversityNews"
https://www.linkedin.com/company/rochester-institute-of-technology"
Number of external links:  147


Libraries imported in python program - 

import socket 
import sys
import ssl
import re
 
