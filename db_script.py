"""
keys            = sorted(set(key for data in datas for key in data))
names           = (data["name"] for data in datas)
results_keys    = sorted(set(key for data in datas for result in data["results"] for key in result))
sectors         = sorted(set(data["sector"] for data in datas))

print(keys)         # ['name', 'results', 'sector', 'siren']
print(results_keys) # ['ca', 'ebitda', 'loss', 'margin', 'year']
print(sectors)      # ['Electronic', 'Energy', 'Luxury', 'Retail', 'Services']

longest_name = max(names, key=len)
print(len(longest_name), longest_name)

Model.objects.all().delete()  # clean table
Result will be delete on cascade
"""
import django
import json
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tkt.settings')
django.setup()

from result.models import Company, Result  # noqa: E402


# get choices from model
SECTOR_CHOICE = {label: value for value, label in Company.Sector.choices}


def db_add_companies(datas):
    companies = []

    for data in datas:

        companies.append(
            Company(
                name=data["name"],
                siren=data["siren"],
                sector=SECTOR_CHOICE[data["sector"]]
            )
        )

    Company.objects.bulk_create(companies)


def db_add_results(datas):
    results = []

    for data in datas:
        company = Company.objects.get(siren=data["siren"])

        for result in data["results"]:

            results.append(
                Result(
                    ca=result["ca"],
                    ebitda=result["ebitda"],
                    loss=result["loss"],
                    margin=result["margin"],
                    year=result["year"],

                    company=company
                )
            )

    Result.objects.bulk_create(results)


def db_init():
    with open("data.json") as json_file:
        datas = json.load(json_file)

    db_add_companies(datas)  # first, add companies to set pk
    db_add_results(datas)    # then, add results


if __name__ == '__main__':
    db_init()
