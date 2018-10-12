import os
import re
import sys
import webbrowser
from collections import defaultdict, Counter
from datetime import datetime, timedelta

import git
from jinja2 import Environment, FileSystemLoader
from tabulate import tabulate


class ProgressBar():
    def __init__(self, endvalue, title='Percent', startvalue=0, bar_length=40):
        self.startvalue = startvalue
        self.endvalue = endvalue
        self.bar_length = bar_length
        self.title = title

    def __enter__(self):
        self.update(self.startvalue)
        return lambda value: self.update(value)

    def __exit__(self, type, value, traceback):
        self.update(self.endvalue)
        print('')

    def update(self, value):
        percent = float(value) / self.endvalue
        arrow = '#' * int(round(percent * self.bar_length))
        spaces = ' ' * (self.bar_length - len(arrow))
        sys.stdout.write("\r{0}: [{1}] {2}%".format(self.title, arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()


badwords_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bad-words-en.csv')
with open(badwords_filepath) as badwords:
    BAD_WORDS = set([line.strip() for line in badwords.readlines()])


FIX_WORDS = {'fix','bug','bugfix','fixes','fixed','bug'}


class Vanity():

    def __init__(self, output_type='print', output_dir='./vanity', limit=100):
        if output_type not in {"print", "html", "markdown"}:
            raise NotImplementedError("Output type must be one of print/html/markdown")
        self.output_dir = os.path.abspath(output_dir)
        self.output_type = output_type
        os.makedirs(output_dir, exist_ok=True)
        self.metrics_list = []
        self.limit = limit

    def load_template(self, name):
        template_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')
        template_file = os.path.join(template_dir, name)
        with open(template_file) as f:
            return Environment(loader=FileSystemLoader(template_dir)).from_string(f.read())

    def render_template(self, template_name, output_file, context={}):
        output_file_abs = os.path.abspath(output_file)
        output_dir = os.path.dirname(output_file_abs)
        try:
            os.makedirs(output_dir)
        except FileExistsError:
            pass
        template = self.load_template(template_name)
        context['repo_name'] = self.repo_name
        with open(output_file_abs, 'wb') as f:
            f.write(template.render(**context).encode('utf-16'))

    def output_metric(self, title, description, data, columns, reverse=True, headers=None):
        if not headers:
            headers = columns
        processed_data = self.process_data(data, columns, reverse=reverse)
        if self.output_type == 'markdown':
            self.write_markdown_table(title, description, processed_data, headers)
        elif self.output_type == 'html':
            self.write_html_table(title, description, processed_data, headers)
        else:
            self.print_section(title, description)
            self.print_as_table(processed_data, headers)
        self.metrics_list.append([title, description])

    def output_index(self):
        if self.output_type == 'markdown':
            filename = 'README.md'
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, 'w') as f:
                f.write("# %s - Git Vanity\n\n" % self.repo_name)
                f.write("Vanity leaderboards for your git repository, last updated at %s\n\n" % datetime.now())
                f.write("Name | Description | Report\n")
                f.write("--- | --- | ---\n")
                for metric in self.metrics_list:
                    f.write("%s | %s | [View](%s.md)\n" % (metric[0], metric[1], self.format_title(metric[0])))
                f.write('\n')
                self.write_md_tag(f)
            print("Markdown files containing vanity leaderboards saved to %s" % self.output_dir)
        elif self.output_type == 'html':
            filename = 'index.html'
            filepath = os.path.join(self.output_dir, filename)
            metrics_rich = [{
                'name': metric[0],
                'description': metric[1],
                'link': self.format_title(metric[0])
            } for metric in self.metrics_list]
            self.render_template('index.html', filepath, {
                'metrics': metrics_rich,
                'repo_name': self.repo_name,
                'updated_at': datetime.now(),
                'limit': self.limit
            })
            print("HTML files containing vanity leaderboards saved to %s" % self.output_dir)
            response = input('Would you like to view your metrics now? [y/n]: ')
            if response.lower()[0] == 'y':
                webbrowser.open('file://%s' % filepath)

    def process_data(self, data, columns, reverse=True, headers=None, truncate=True):
        rows = [[row[key] for key in columns] for row in data]
        sorted_rows = sorted(rows, key=lambda row: row[-1], reverse=reverse)
        processed_rows = []
        for row in sorted_rows:
            processed_row = []
            for item in row:
                if isinstance(item, str) and truncate:
                    processed_row.append(item[:50])
                else:
                    processed_row.append(str(item))
            processed_rows.append(processed_row)
        return processed_rows

    def print_section(self, title, description):
        print("##################################################")
        print("# %s" % title)
        print("# (%s)" % description)
        print("##################################################")
        print("")

    def print_as_table(self, data, headers):
        print(tabulate(data[:self.limit], headers=headers))
        if len(data) > self.limit:
            num_hidden = len(data) - self.limit
            print("(Hiding %s result%s)" % (num_hidden, "s" if num_hidden != 1 else ""))
        print('')

    def format_title(self, title):
        return re.sub('[^A-Za-z0-9_]', '', title.lower().replace(' ', '_'))

    def write_markdown_table(self, title, description, data, headers):
        filename = '%s.md' % self.format_title(title)
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w') as f:
            f.write("# %s - %s\n\n" % (title, self.repo_name))
            f.write("%s\n\n" % description)
            f.write("%s\n" % " | ".join(headers))
            f.write("%s\n" % " | ".join(["---" for header in headers]))
            for row in data[:self.limit]:
                f.write("%s\n" % " | ".join([str(item) for item in row]))
            f.write("\n")
            if len(data) > self.limit:
                num_hidden = len(data) - self.limit
                f.write("(Hiding %s result%s)" % (num_hidden, "s" if num_hidden != 1 else ""))
                f.write("\n\n")
            self.write_md_tag(f)

    def write_html_table(self, title, description, data, headers):
        filename = '%s/index.html' % self.format_title(title)
        filepath = os.path.join(self.output_dir, filename)
        self.render_template('metric.html', filepath, {
            'title': title,
            'description': description,
            'data': data,
            'headers': headers,
            'limit': self.limit,
            'show_back': True
        })

    def write_md_tag(self, f):
        f.write("Produced with [Git Vanity](https://github.com/intuition-app/git-vanity)\n\n")
        f.write("For meaningful analytics and reporting for Git, use [Intuition](https://intuition.app)\n\n")

    def is_fix(self, commit):
        words = re.findall(r'\w+|\W+', commit.message.lower())
        for word in words:
            if word in FIX_WORDS:
                return True
        return False

    def is_badwords(self, commit):
        words = re.findall(r'\w+|\W+', commit.message.lower())
        for word in words:
            if word in BAD_WORDS:
                return True
        return False

    def run(self):

        repo = git.Repo(search_parent_directories=True)
        repo_dir = os.path.dirname(repo.common_dir)
        self.repo_name = os.path.basename(repo_dir)
        raw_git = git.Git()
        git_files = raw_git.ls_files().split('\n')
        num_files = len(git_files)

        authors = defaultdict(lambda: {
            # Current Branch Stats
            'num_lines_total': 0,
            'num_chars_total': 0,

            # Commit Stats
            'num_commits_total': 0,
            'insertions': 0,
            'deletions': 0,
            'total_changes': 0,
            'commits_by_month': Counter(),
            'commits_by_day': Counter(),
            'merges': 0,
            'fixes': 0,
            'badwords': 0,
            'nightowl': 0,

            # Largest Change Stats
            'largest_change': 0,
            'largest_change_message': '',
            'largest_change_sha': '',

            # Longest Message
            'longest_message_length': 0,
            'longest_message': '',
            'longest_message_sha': '',

            # Longest Gap
            'last_commit_date': None,
            'gap_start': None,
            'gap_end': None,
            'gap_length': timedelta()
        })

        print("Analyzing all historical commits. This may take a while...")
        for index, commit in enumerate(repo.iter_commits()):
            short_sha = commit.hexsha[:7]
            sys.stdout.write("Analyzing commit %s. Processed %s commits so far.\r" % (short_sha, index))

            is_merge = len(commit.parents) > 1
            is_bugfix = self.is_fix(commit)
            contains_badwords = self.is_badwords(commit)
            commit_month = commit.authored_datetime.strftime("%m/%Y")
            commit_day = commit.authored_datetime.strftime("%d %b, %Y")
            commit_hour = commit.authored_datetime.hour

            author_name = commit.author.name
            author_info = authors[author_name]
            author_info['num_commits_total'] += 1
            insertions = commit.stats.total['insertions']
            deletions = commit.stats.total['deletions']
            total_change = insertions + deletions
            author_info['insertions'] += insertions
            author_info['deletions'] += deletions
            author_info['total_changes'] += total_change
            author_info['commits_by_month'][commit_month] += 1
            author_info['commits_by_day'][commit_day] += 1
            if is_merge:
                author_info['merges'] += 1
            if is_bugfix:
                author_info['fixes'] += 1
            if contains_badwords:
                author_info['badwords'] += 1
            if commit_hour < 5 or commit_hour > 22:
                author_info['nightowl'] += 1
            
            if not is_merge and total_change > author_info['largest_change']:
                author_info['largest_change'] = total_change
                author_info['largest_change_message'] = commit.message.replace('\n','')
                author_info['largest_change_sha'] = short_sha

            message_length = len(commit.message)
            if message_length > author_info['longest_message_length']:
                author_info['longest_message_length'] = message_length
                author_info['longest_message'] = commit.message
                author_info['longest_message_sha'] = short_sha
            
            current_datetime = commit.authored_datetime
            if author_info['last_commit_date']:
                current_gap_length = author_info['last_commit_date'] - current_datetime
                if author_info['gap_length'] is None or author_info['gap_length'] < current_gap_length:
                    author_info['gap_length'] = current_gap_length
                    author_info['gap_start'] = current_datetime
                    author_info['gap_end'] = author_info['last_commit_date']

            author_info['last_commit_date'] = current_datetime

        print("Finished analyzing commits...")
        print('Analyzing %s files of current HEAD ref for blame info...' % num_files)

        with ProgressBar(num_files) as update:
            for index, filepath in enumerate(git_files):
                update(index)
                for commit, lines in repo.blame('HEAD', filepath):
                    author_name = commit.author.name
                    authors[author_name]['num_lines_total'] += len(lines)
                    for line in lines:
                        authors[author_name]['num_chars_total'] += len(line.strip())

        authors_list = []
        for name, info in authors.items():
            if info['num_commits_total'] == 0:
                continue
            info['name'] = name
            top_month = info['commits_by_month'].most_common()[0]
            info['best_month'] = top_month[0]
            info['best_month_count'] = top_month[1]
            top_day = info['commits_by_day'].most_common()[0]
            info['best_day'] = top_day[0]
            info['best_day_count'] = top_day[1]
            authors_list.append(info)

        print("Done collecting metrics")
        if self.output_type == 'print':
            print('')

        self.output_metric("The Real Product Owner", "Most Lines In HEAD Ref", authors_list,
                           columns=['name', 'num_lines_total'], headers=['Author', 'Lines'])

        self.output_metric("Git Master", "Most Commits", authors_list, columns=['name', 'num_commits_total'],
                           headers=['Author', 'Commits'])

        self.output_metric("Keyboard Wizard", "Most Insertions/Deletions", authors_list, 
                           columns=['name', 'insertions', 'deletions', 'total_changes'],
                           headers=['Author', 'Insertions', 'Deletions', 'Total Lines Changed'])

        self.output_metric("Mythical Man Month", "Most Commits In A Single Month, One Entry Per Author",
                           authors_list, columns=['name', 'best_month', 'best_month_count'],
                           headers=['Author', 'Best Month', 'Commits'])

        self.output_metric("It's A Marathon, Not A Sprint", "Most Commits In A Single Day, One Entry Per Author",
                           authors_list, columns=['name', 'best_day', 'best_day_count'],
                           headers=['Author', 'Best Day', 'Commits'])

        self.output_metric("Too Big To Fail", "Largest Commit (Non-Merge)", authors_list,
                           columns=['name', 'largest_change_sha', 'largest_change_message', 'largest_change'],
                           headers=['Author', 'SHA', 'Message', 'Total Lines Changed'])

        self.output_metric("Branch Cutter", "Most Merge Commits", authors_list,
                           columns=['name', 'merges'], headers=['Author', 'Total Merges'])

        self.output_metric("Exterminator", "Most Commits With Bug Fixes",
                           authors_list, columns=['name', 'fixes'], headers=['Author', 'Total Fixes'])

        self.output_metric("Talk Like A Pirate", "Most Commit Messages That Contain Profanity",
                           authors_list, columns=['name', 'badwords'], headers=['Author', 'Total Profane Commits'])

        self.output_metric("Night Owl", "Most Commits Late At Night", authors_list,
                           columns=['name', 'nightowl'], headers=['Author', 'Total Late Night Commits'])

        self.output_metric("It's Been A Long Time", "Longest Gap Between Commits", authors_list,
                           columns=['name', 'gap_start', 'gap_end', 'gap_length'],
                           headers=['Author', 'Start', 'End', 'Gap Length'])

        self.output_index()
