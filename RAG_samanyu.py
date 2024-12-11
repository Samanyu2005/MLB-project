from openai import OpenAI
import numpy as np

client = OpenAI(api_key="<Key>")

#===== Creating an embedding with the openai api =======
# https://platform.openai.com/docs/guides/embeddings
response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small"
)
# print(response.data[0].embedding)
# ======================================================



# ==== Use case example ======
query = "At which team was Messi the all time leading goalscorer?"

resource1 = "Messi was born on 24 June 1987 in Rosario, Santa Fe Province,[21] the third of four children of Jorge Messi, a steel factory manager, and his wife Celia Cuccittini, who worked in a magnet manufacturing workshop. On his father's side, he is of Italian and Spanish descent, the great-grandson of immigrants from the north-central Adriatic Marche region of Italy, and on his mother's side, he has primarily Italian ancestry.[3] Growing up in a tight-knit, football-loving family, Leo developed a passion for the sport from an early age, playing constantly with his older brothers, Rodrigo and Matías, and his cousins, Maximiliano and Emanuel Biancucchi, both of whom became professional footballers.[22] At the age of four he joined local club Grandoli, where he was coached by his father, though his earliest influence as a player came from his maternal grandmother, Celia, who accompanied him to training and matches.[23] He was greatly affected by her death, shortly before his eleventh birthday; since then, as a devout Catholic, he has celebrated his goals by looking up and pointing to the sky in tribute to his grandmother.[24][25]"
resource2 = "Messi has endorsed sportswear company Adidas since 2006. According to France Football, he was the world's highest-paid footballer for five years out of six between 2009 and 2014, and was ranked the world's highest-paid athlete by Forbes in 2019 and 2022. Messi was among Time's 100 most influential people in the world in 2011, 2012, and 2023. In 2020 and 2023, he was named the Laureus World Sportsman of the Year, the first team-sport athlete to win it. In 2020, Messi was named to the Ballon d'Or Dream Team and became the second footballer and second team-sport athlete to surpass $1 billion in career earnings."
resource3 = """
Lionel Andrés Messi[note 1] (Spanish pronunciation: [ljoˈnel anˈdɾes ˈmesi] ⓘ; born 24 June 1987), also known as Leo Messi, is an Argentine professional footballer who plays as a forward for and captains both Major League Soccer club Inter Miami and the Argentina national team. Widely regarded as one of the greatest players of all time, Messi set numerous records for individual accolades won throughout his professional footballing career such as eight Ballon d'Or awards and eight times being named the world's best player by FIFA.[note 2] He is the most decorated player in the history of professional football having won 45 team trophies,[note 3] including twelve league titles, four UEFA Champions Leagues, two Copa Américas, and one FIFA World Cup. Messi holds the records for most European Golden Shoes (6), most goals for a single club (672, with Barcelona), most goals (474), hat-tricks (36) and assists (192) in La Liga, most matches played (39), assists (18) and goal contributions (34) in the Copa América, most matches played (26) and goal contributions (21) in the World Cup, most international appearances (189) and international goals (112) by a South American male, and the second-most in the latter category outright. A prolific goalscorer and creative playmaker, Messi has scored over 850 senior career goals for club and country.

Born in Rosario, Argentina, Messi relocated to Spain to join Barcelona at age 13, and made his competitive debut at age 17 in October 2004. He established himself as an integral player for the club within the next three years, and in his first uninterrupted season in 2008–09 helped Barcelona achieve the first treble in Spanish football; that year, aged 22, Messi won the first of his four consecutive Ballons d'Or, the first player to win it four times. During the 2011–12 season, he set La Liga and European records for most goals in a season, while establishing himself as Barcelona's all-time top scorer. The following two seasons, he finished second for the Ballon d'Or behind Cristiano Ronaldo, his perceived career rival, before regaining his best form during the 2014–15 campaign, where he became the all-time top scorer in La Liga, led Barcelona to a historic second treble, and won a fifth Ballon d'Or in 2015. Messi assumed captaincy of Barcelona in 2018, and won a record sixth Ballon d'Or in 2019. During his overall tenure at Barcelona, Messi won a club-record 34 trophies, including ten La Liga titles and four UEFA Champions Leagues, among others. He signed for French club Paris Saint-Germain in August 2021, where he would win the Ligue 1 title during both of his seasons there. Messi joined American club Inter Miami in July 2023, and set a new mark for most goals scored for the club by his second season.

An Argentine international, Messi is the national team's all-time leading goalscorer and most-capped player. His style of play as a diminutive, left-footed dribbler drew career-long comparisons with compatriot Diego Maradona, who described Messi as his successor. At the youth level, he won the 2005 FIFA World Youth Championship and gold medal at the 2008 Summer Olympics. After his senior debut in 2005, Messi became the youngest Argentine to play and score in a World Cup in 2006. He assumed the national team's captaincy in 2011, and then led Argentina to three consecutive finals: the 2014 FIFA World Cup, the 2015 Copa América and the Copa América Centenario, all of which they would lose. After initially announcing his international retirement in 2016, he returned to help his country narrowly qualify for the 2018 FIFA World Cup, which they would again exit early. Messi and the national team finally broke Argentina's 28-year trophy drought with a victory in the 2021 Copa América, where he was named the tournament's best player and which later helped him win his seventh Ballon d'Or that year. He then led Argentina to win the 2022 FIFA World Cup, his country's third overall world championship and first in 36 years. This followed with a record-extending eighth Ballon d'Or in 2023. A second Copa América victory with Messi as captain came in 2024.

"""

query_embedding = client.embeddings.create(
        input=query,
        model="text-embedding-3-small"
    ).data[0].embedding

resource_responses = client.embeddings.create(
            input=[resource1, resource2, resource3],
            model="text-embedding-3-small"
    ).data

resource1_embedding = resource_responses[0].embedding
resource2_embedding = resource_responses[1].embedding
resource3_embedding = resource_responses[2].embedding

query = np.array(query_embedding)

resource1_embedding = np.array(resource1_embedding)
resource2_embedding = np.array(resource2_embedding)
resource3_embedding = np.array(resource3_embedding)

def cosine_simularity(A, B):
    return np.dot(A,B) / ( np.linalg.norm(A) * np.linalg.norm(B) )

simularity1 = cosine_simularity(query_embedding, resource1_embedding)
simularity2 = cosine_simularity(query_embedding, resource2_embedding)
simularity3 = cosine_simularity(query_embedding, resource3_embedding)

print(f"Simularity of query and resource1: {simularity1}")
print(f"Simularity of query and resource2: {simularity2}")
print(f"Simularity of query and resource3: {simularity3}")