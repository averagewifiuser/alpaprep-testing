from alphaprep import app
import random


@app.template_filter('filter_shuffle')  # this function is to shuffle possible answers. It as a custom jinja template
def filter_shuffle(q):
        h = random.sample(q, len(q))   
        return h

