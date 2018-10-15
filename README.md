# GitVanity

A command line tool for generating vanity leaderboards of Git stats.

Find out exciting stats like:

* Who wrote the most lines in the current head of your repo
* Who wrote the most commits
* Who has fixed the most bugs
* Who swears the most in commit messages
* Who has made the largest commit in the history of your repo

And a ton more!

`git-vanity` gives you multiple output options as well for easy viewing and sharing:

* pretty print results to the command line
* generate markdown tables of results
* or output html leaderboards

## Shameless Plug

`git-vanity` was built by [Intuition](https://intuition.app). We run analysis for git repos
that is a lot more meaningful than just vanity metrics. We help you automate your standups, run your
sprint retrospectives and get real-time personalized code change notifications.

If you and your dev team want to spend less time on meetings and administrative work and more time coding,
[sign up for Intuition](https://intuition.app).

## Leaderboards

* **The Real Product Owner** - Most Lines In HEAD Ref
* **Git Master** - Most Commits
* **Keyboard Wizard** - Most Insertions/Deletions
* **Mythical Man Month** - Most Commits In A Single Month, One Entry Per Author
* **It's A Marathon, Not A Sprint** - Most Commits In A Single Day, One Entry Per Author
* **Too Big To Fail** - Largest Commit (Non-Merge)
* **Branch Cutter** - Most Merge Commits
* **Exterminator** - Most Commits With Bug Fixes
* **Talk Like A Pirate** - Most Commit Messages That Contain Profanity
* **Night Owl** - Most Commits Late At Night
* **It's Been A Long Time** - Longest Gap Between Commits

## Examples

HTML output for the "Most Commits" leaderboard for the [facebook/react](https://github.com/facebook/react) repo.

![alt text](https://github.com/intuition-app/git-vanity/raw/master/imgs/screenshot.png "Facebook React Screenshot")

### [facebook/react](https://github.com/facebook/react)

* [HTML Output](https://intuition-app.github.io/git-vanity/react/index.html)
* [Markdown Output](https://github.com/intuition-app/git-vanity/blob/master/examples/react/README.md)

### [koajs/koa](https://github.com/koajs/koa)

* [HTML Output](https://intuition-app.github.io/git-vanity/koa/index.html)
* [Markdown Output](https://github.com/intuition-app/git-vanity/blob/master/examples/koa/README.md)

## Installation

`git-vanity` works with python 2 or 3 and can be installed via `pip`.

```bash
pip install git-vanity
```

## Usage

From the command line, navigate to any directory that is part of a git repository.

To print leaderboards directly to the command line:

```bash
git vanity
```

There is a default limit of 100 entries per leaderboard. To change this limit, use the `--limit` option:

```bash
git vanity --limit 1000
```

To generate markdown files that contain leaderboard information:

```bash
git vanity --output-type markdown
```

Generating markdown files allows you to commit them to your repo for viewing in your Git hosting service (e.g.
GitHub, Gitlab, Bitbucket, etc).

To generate html files that contain leaderboard information:

```bash
git vanity --output-type html
```

By default, markdown and html files are written to the directory `./vanity`. This can be changed
via the `--output-dir` option:

```bash
git vanity --output-type html --output-dir ./vanity-html
```

## Hosting HTML Via GitHub Pages

**Hosting your pages this way for a private repository will make them public. They will include a list
of authors, shortened hexshas and truncated commit messages. If this is something that you are not
comfortable with, DO NOT publish your vanity metrics in this way.**

Generate your vanity html and output it to the directory `docs` in the root folder of your repo:

```bash
git vanity -output-type html -output-dir ./docs
```

Commit the vanity html files to your master branch and push to github.

```bash
git add ./docs
git commit -m "Added git vanity leaderboards"
git push
```

Finally, follow the
[instructions on GitHub](https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/#publishing-your-github-pages-site-from-a-docs-folder-on-your-master-branch)
for setting up GitHub pages with a docs folder.

## Contributing

1. Fork this repository
2. Create your feature branch (git checkout -b feature/description)
3. Commit your changes (git commit -am 'Added some feature')
4. Push your new commit to the branch (git push origin feature/description)
5. Create a new Pull Request

## License

GitVanity is released under the MIT license.
