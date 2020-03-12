####### Q32: 

The answer belowed are removed stopwords and fulfill the specific scenerio.
#######a list of the top ten most frequent tokens:

```
#ArtificialIntelligence : 15
@alison_iot : 7
Awesome : 7
Benefits : 7
#CloudComputing : 7
Services : 7
@ravikikan : 7
#robotics : 7
#datascience : 7
#MachineLear : 7
```


#######a list of the top ten most frequent hashtags

```
#ArtificialIntelligence : 15
#CloudComputing : 7
#robotics : 7
#datascience : 7
#MachineLear : 7
# : 3
#AI : 3
#computervision : 2
#IoT : 2
#stem : 1
```

#######a list of the top ten most frequent terms, skipping mentions and hashtags.

```
Awesome : 7
Benefits : 7
Services : 7
Some : 2
examples : 2
science : 2
behind : 2
well : 2
achievements : 2
MARK : 2
```



## Task 3.4: Student proposal 
(1)We were thinking use 'Amazon Prime' and 'Netflix' to see which one is more popular, however among all the tweet we collected (409), there's more discusstion about Netflix.
Suprisingly, without specific the language, we got a lot of spanish written tweet, so we also delete some spanish stopword(or words that don't have special meaning)to got following words and tag. However, we realized not so many people discuss about Amazon prime, so that we know still Netflix own bigger market as the online-media provider.

```
Netflix : 200
Coronavirus : 52
casa : 49
cuarentena : 47
piénsalo : 46
@oscarpgarcia : 40
@netflix : 39
que : 32
documentary : 28
🚨 : 28
```

From the keywords above we trace back to the person who post this, 
and the original tweet is as follow and had 24.3k repost:
Tú 
Yo
Coronavirus 
Netflix 
En cuarentena
En mi casa
No se, piénsalo






(2)
Trying to use SpaceX as filter without knowing there's a news today. Tag and the content are correspond to the news that
SpaceX's Dragon cargo capsule arrived at the International Space Station on March 9.
NASA astronaut Jessica Meir used the station's huge Canadarm robotic arm to capture Dragon at 6:25 a.m. EDT (1025 GMT), while the two spacecraft were 262 miles (422 kilometers) above the Pacific Ocean near Vancouver, British Columbia, NASA officials said.
However, we took some time to collect the data than we expect, from here we can know that people put their focus on another topic instead of SpaceX.

```
@SpaceX : 212
@Space_Station : 173
#Dragon : 103
SpaceX : 99
@Astro_Jessica : 98
Dragon : 86
@AstroDrewMorgan : 71
@NASA : 64
station : 53
@elonmusk : 45
```




Q35: How long have you been working on this session? What have been the main difficulties you have faced and how have you solved them?
We spent around 3.5 hr to finish it

When using 'Coronavirus' as filter to collect the data, we both encountered some key error problem, we check the internet, modify the JSON file for the possible problem and change the python version to compile, but the problem still can't be solved. However, we also tried so many other keywords to filter, and they all worked perfectly. 



