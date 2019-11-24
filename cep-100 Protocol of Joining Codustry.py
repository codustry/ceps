# Title: Protocol of Joining Codustry
# Author: Nutchanon Ninyawee
# Status: Draft
# Type: None
# Created: 24 Nov 2019

from typing import Literal, NewType
from datetime import timezone

address = "work.codustry.com"
address_onion = None

CityOnEarth = NewType("CityOnEarth", str)

class Applicant:
    address_submit = address
    language_programing_major: str
    name: str
    basedIn: CityOnEarth
    timezone: timezone


    def __init__(self, language_major):
        super().__init__()
        self.language_programing_major = language_major

    def sign_up_with(self, channel: Literal["github", "google", "microsoft", "amazon", "linkedin"]):
        pass
    
    def choose_tradtional_or_exotic(self):
        pass
    
    def apply_via_api(self):
        pass

    def fill_form(self):
        pass

    def add_profile(self, url):
        sources_known = ["github", "gitlab", "bitbucket", "stackoverflow", "dev.to", "kaggle", "medium", "behance", ]
        pass
    
    def upload_cv(self, pdf):
        pass

    def improve_and_create_a_pull_request(self):
        pass

    def choose_team_topic(self):
        pass

    def verify_skill(self):
        sources_known = ["pluralsight"]
        pass


class AnonymousApplicant(Applicant):
    address_submit = address_onion

    def sign_up_with(self, channel: Literal["keybase", "signal", "email", "telegram"]):
        pass

def main():
    primary_programing_language = chooseFromLanguages()
    need_anonymous, prefer_channel = show_sign_up_options()

    if need_anonymous:
        an_applicant = AnonymousApplicant(primary_programing_language)
    else:
        an_applicant = Applicant(primary_programing_language)
    
    an_applicant.sign_up_with(prefer_channel)

    fun_or_boring = red_pill_or_blue_pill = an_applicant.choose_tradtional_or_exotic()

    if fun_or_boring == "boring":
        an_applicant.fill_form()
        an_applicant.upload_cv()
    else:
        an_applicant.apply_via_api()
        an_applicant.improve_and_create_a_pull_request()

    accept, doubt_in_skill = an_applicant.waitForResonse()

    if doubt_in_skill: 
        an_applicant.verify_skill()

    teams_and_topics = an_applicant.choose_team_topic()

    an_applicant.get_interview(by=teams_and_topics)


