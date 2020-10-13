from codustry.codustry import Codustry
from codustry.models.craftsman import AllCraftsmanTypes
from codustry.models.craftsman import AuthorizeLevel
from codustry.protocals.inactive import make_inactive


@situation(who=AllCraftsmanTypes, when=Month.day(1), where=AllPlaces, overwrite_by=AuthorizeLevel.CLevel)
def pay_salary(craftsman: AllCraftsmanTypes, company: Codustry, time: Time):
    rate = craftsman.salary_rate

    total = 0
    for c in craftsman.contribution:
        rate = c.project.rate or rate
        total += rate * c.amount

    company.money_accounts.pay(craftsman, total, "Salary for {craftsman}, {Time.month.prev}")
