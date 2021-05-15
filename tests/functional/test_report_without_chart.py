# coding=utf-8
"""Pull request with the report but without the chart feature tests."""

import os
import subprocess
from dataclasses import dataclass

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

owners_file_content = """\
chart:
  name: psql-service
  shortDescription: Lorem ipsum
publicPgpKey: null
users:
  - githubUsername: openshift-helm-charts-bot
vendor:
  label: test-org1
  name: Balabit
"""

@pytest.fixture
def secrets():
    @dataclass
    class Secret:
        test_repo: str
        fork_repo: str
        cluster_token:  str
        bot_token: str
        pr_base_branch: str

    test_repo = os.environ.get("TEST_REPO")
    if not test_repo:
        raise Exception("TEST_REPO environment variable not defined")
    fork_repo = os.environ.get("FORK_REPO")
    if not fork_repo:
        raise Exception("FORK_REPO environment variable not defined")
    cluster_token = os.environ.get("CLUSTER_TOKEN")
    if not cluster_token:
        raise Exception("CLUSTER_TOKEN environment variable not defined")
    bot_token = os.environ.get("BOT_TOKEN")
    if not bot_token:
        raise Exception("BOT_TOKEN environment variable not defined")
    pr_number = os.environ.get("PR_NUMBER")
    if not pr_number:
        raise Exception("PR_NUMBER environment variable not defined")

    pr_base_branch = "test-pr-"+pr_number
    return Secret(test_repo, fork_repo, cluster_token, bot_token, pr_base_branch)

@scenario('features/report_without_chart.feature', 'Partner submits report without any errors')
def test_partner_submits_report_without_any_errors():
    """Partner submits report without any errors."""

@given('the partner has created a report without any errors')
def the_partner_has_created_a_report_without_any_errors(secrets):
    """the partner has created a report without any errors."""

    out = subprocess.run(["mkdir", "push", f"https://x-access-token:{secrets.bot_token}@github.com/{secrets.test_repo}", f"HEAD:{secrets.pr_base_branch}", "-f"], capture_output=True)
    print(out.stdout.decode("utf-8"))
    print(out.stderr.decode("utf-8"))
    out = subprocess.run(["git", "push", f"https://x-access-token:{secrets.bot_token}@github.com/{secrets.test_repo}", f"HEAD:{secrets.pr_base_branch}", "-f"], capture_output=True)
    print(out.stdout.decode("utf-8"))
    print(out.stderr.decode("utf-8"))

@when('the partner sends the pull request with the report')
def the_partner_sends_the_pull_request_with_the_report():
    """the partner sends the pull request with the report."""


@then('the index.yaml is updated with a new entry')
def the_indexyaml_is_updated_with_a_new_entry():
    """the index.yaml is updated with a new entry."""


@then('the partner should see the pull request getting merged')
def the_partner_should_see_the_pull_request_getting_merged():
    """the partner should see the pull request getting merged."""

