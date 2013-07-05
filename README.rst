.. warning::
    I don't have a subscription for MUBI at the moment, so **development is on hold** until I
    subscribe again. You are welcome to send me pull requests, though!


======
MUBIPy
======
:Author:    Johannes Baiter (jbaiter)
:License:   Simplified BSD License

About
-----
A small Python module to access MUBI.com functionality. As MUBI currently does
not offer an API for 3rd party developers, nor is planning to do so in the
foreseeable future,[1]_ this module relies on screenscraping using the
BeautifulSoup package.[2]_

.. [1] http://support.mubi.com/mubi/topics/mubi_api_for_xbmc_other_integration 
.. [2] This was chosen over lxml for portability reasons, as it is written in
       pure Python, which makes it easier to port for a variety of platforms
       (XBMC on ARM, Android, etc)

Currently supported features:
-----------------------------
- Browse films, filter by genre, country or language
- Browse MUBI cinemas/programs
- Search for films or persons
- See all available movies for a person
- For users with a subscription, obtain URL to play a movie with any player that supports HTTP streaming

Not yet implemented:
--------------------
- Support for purchases of single films

Example usage:
--------------
>>> from mubi import Mubi
>>> from pprint import pprint
>>> mubi = Mubi()
>>> mubi.login("username", "password")
>>> pprint(mubi.get_all_programs())
[(u'10 Years of Venice Film Critics Week',
  u'10-years-of-venice-film-critics-week',
  u'http://s3.amazonaws.com/auteurs_production/program_images/494/critics_week.png'),
[...]
 (u'Films by Peter Tscherkassky',
  u'films-by-peter-tscherkassky--2',
  u'http://s3.amazonaws.com/auteurs_production/program_images/305/films-by-peter-tscherkassky.jpg')]
>>> pprint(mubi.get_program_films("films-by-peter-tscherkassky--2"))
[(u'Peter Tscherkassky: Outer Space (Austria 1999)',
  u'21392',
  u'http://s3.amazonaws.com/auteurs_production/images/film/outer-space/w448/outer-space.jpg?1308427210'),
 (u'Peter Tscherkassky: Manufraktur (Austria 1985)',
  u'27802',
  u'http://s3.amazonaws.com/auteurs_production/images/film/manufraktur/w448/manufraktur.jpg?1289464710'),
 (u"Peter Tscherkassky: L'arriv\xe9e (Austria 1998)",
  u'31014',
  u'http://s3.amazonaws.com/auteurs_production/images/film/larrivee/w448/larrivee.jpg?1289473234'),
 (u'Peter Tscherkassky: Dream Work (Austria 2002)',
  u'33002',
  u'http://s3.amazonaws.com/auteurs_production/images/film/dream-work/w448/dream-work.jpg'),
 (u"Peter Tscherkassky: Motion Picture (La sortie des ouvriers de l'usine Lumi\xe8re \xe0 Lyon) (Canada 1984)",
  u'33206',
  u'http://s3.amazonaws.com/auteurs_production/images/film/motion-picture-la-sortie-des-ouvriers-de-lusine-lumiere-a-lyon/w448/motion-picture-la-sortie-des-ouvriers-de-lusine-lumiere-a-lyon.jpg?1289478246'),
 (u'Peter Tscherkassky: Miniatures \u2013 Many Berlin Artists in Hoisdorf (Austria 1983)',
  u'33209',
  u'http://s3.amazonaws.com/auteurs_production/images/film/miniatures-many-berlin-artists-in-hoisdorf/w448/miniatures-many-berlin-artists-in-hoisdorf.jpg?1289478253'),
 (u'Peter Tscherkassky: Get Ready (Austria 1999)',
  u'33210',
  u'http://s3.amazonaws.com/auteurs_production/images/film/get-ready/w448/get-ready.jpg?1289478256')]
>>> mubi.get_play_url(33002)
'http://video.mubi.com/theauteurs/Nativ/dream-work_xx_xx_1024_720x304_174_33002.m4v?e=XXXXXXXXXX&a=A1,A2,AD,AE,AF,AG,AI,AL,AM,AN,AO,AP,AQ,AR,AS,AT,AU,AW,AX,AZ,BA,BB,BD,BE,BF,BG,BH,BI,BJ,BM,BN,BO,BR,BS,BT,BV,BW,BY,BZ,CA,CC,CD,CF,CG,CH,CI,CK,CL,CM,CN,CO,CR,CU,CV,CX,CY,CZ,DE,DJ,DK,DM,DO,DZ,EC,EE,EG,EH,ER,ES,ET,EU,FI,FJ,FK,FM,FO,FR,GA,GB,GD,GE,GF,GG,GH,GI,GL,GM,GN,GP,GQ,GR,GS,GT,GU,GW,GY,HK,HM,HN,HR,HT,HU,ID,IE,IL,IM,IN,IO,IQ,IR,IS,IT,JE,JM,JO,JP,KE,KG,KH,KI,KM,KN,KP,KR,KW,KY,KZ,LA,LB,LC,LI,LK,LR,LS,LT,LU,LV,LY,MA,MC,MD,ME,MG,MH,MK,ML,MM,MN,MO,MP,MQ,MR,MS,MT,MU,MV,MW,MX,MY,MZ,NA,NC,NE,NF,NG,NI,NL,NO,NP,NR,NU,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PM,PN,PR,PS,PT,PW,PY,QA,RE,RO,RS,RU,RW,SA,SB,SC,SD,SE,SG,SH,SI,SJ,SK,SL,SM,SN,SO,SR,ST,SV,SY,SZ,TC,TD,TF,TG,TH,TJ,TK,TL,TM,TN,TO,TT,TV,TW,TZ,UA,UG,UM,US,UY,UZ,VA,VC,VE,VG,VI,VN,VU,WF,WS,YE,YT,ZA,ZM,ZW&h=XXXXXXXXXXXXXXXXXXXXXXXXX&bghttp_Pragma=no-cache&bghttp_Cache-Control=no-store'
