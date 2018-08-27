# -*- coding: utf-8 -*-

import pygal
import requests

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def render_lang_repo(lang):
    """Render language repo to svg."""
    # Make an API call and store the response.
    url = 'https://api.github.com/search/repositories?q=language:%s&sort=stars' % lang
    r = requests.get(url)
    print('Status code:', r.status_code)

    # Store API response in a variable.
    response_dict = r.json()
    print('Total repositories:', response_dict['total_count'])

    # Explore information about the repositories.
    repo_dicts = response_dict['items']

    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])

        # Get the project description, if one is available.
        description = repo_dict['description']
        if not description:
            description = 'No description provided.'

        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': str(description),
            'xlink': repo_dict['html_url'],
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
    chart.title = 'Most-Starred %s Projects on GitHub' % lang.title()
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('%s_repos.svg' % lang)


for lang in ('java', 'go', 'c', 'python', 'rust'):
    render_lang_repo(lang)
