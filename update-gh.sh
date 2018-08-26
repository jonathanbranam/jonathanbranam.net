#! env bash

pipenv run pelican content
pipenv run ghp-import output
git push origin gh-pages
