from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsportal_project.settings')
setup()

from news.models import Article

article = Article.objects.get(title='Thousands march to Knesset in Jerusalem to protest draft equality')
article.title = 'Thousands march in Jerusalem to protest haredi draft exemption'
article.content = '''Thousands march in Jerusalem for equal military service burden, demanding government action for widespread recruitment. "We bear the burden, but we demand immediate change," protesters say.

Over 5,000 people from Sholder to Shoulder, an organization that advocates for equal service for all, hundreds of reservists, and others marched in Jerusalem on Wednesday, calling for equality in sharing the burden of military service.

Thousands more participants are expected to join the demonstration in front of the Knesset on Wednesday evening.

"In the past year, we fought shoulder to shoulder, we protected one another, but unfortunately - like that generation, we lost close and beloved friends," Shoulder to Shoulder said in a statement.

"In the army, mutual responsibility and camaraderie are supreme values, and throughout the past year, we learned to put disagreements aside when fighting against a common enemy. Today, we demand that leadership come down to the people's level, look us in the eyes, and bring about widespread recruitment. We bear the burden and will continue to bear it, but we demand immediate change."

In addition to the Shoulder to Shoulder organization's march, a "Marching for Recruitment" demonstration was also held, with hundreds of young people, parents, discharged soldiers, and public figures participating, under a clear message: the duty of service belongs to all of us.

Mutual responsibility in all sectors

The march came as a public and moral response to voices of draft dodging and incitement against the IDF, and it reinforced the importance of integration, equality, and mutual responsibility in all sectors of Israeli society.

During the march, former Knesset member Shirly Pinto Kadosh met with Lali Deri - the mother of Saadia Deri, an IDF soldier who fell in Gaza. In conversation with her, Pinto said, "Not just me and him - but every person who receives an exemption from service and can enlist, should do so. Whether they are ultra-Orthodox, a person with disabilities, or any other person."

Finally, Deri added, "When we choose to contribute despite the difficulty - we truly strengthen our country."'''
article.save()
print("Article updated successfully")