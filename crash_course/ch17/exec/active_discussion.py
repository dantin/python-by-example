
import pygal
import requests

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter


def load_hn_data():
    """Load data from hacker-news."""
    # Make an API call and store the response.
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)
    print('Status code:', r.status_code)

    # Process information about each submission.
    submission_ids = r.json()
    submission_dicts = []
    for submission_id in submission_ids[:30]:
        # Make a separate API call for each submission.
        url = ('https://hacker-news.firebaseio.com/v0/item/' +
               str(submission_id) + '.json')
        submission_r = requests.get(url)
        print(submission_r.status_code)
        response_dict = submission_r.json()

        submission_dict = {
            'title': response_dict['title'],
            'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
            'comments': response_dict.get('descendants', 0)
        }
        submission_dicts.append(submission_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)
    return submission_dicts


def render_svg(data_dicts):
    """Render data to svg."""
    names, plot_dicts = [], []
    for data_dict in data_dicts:
        names.append(data_dict['title'])

        plot_dict = {
            'value': data_dict['comments'],
            'label': data_dict['title'],
            'xlink': data_dict['link'],
        }
        plot_dicts.append(plot_dict)

    # Make visualization.
    my_style = LS('#333366', base_style=LCS)
    my_style.title_font_size = 24
    my_style.label_font_size = 14
    my_style.major_label_font_size = 18

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.tuncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Active discussion on Hacker News.'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('discussion.svg')


datas = load_hn_data()
render_svg(datas)
