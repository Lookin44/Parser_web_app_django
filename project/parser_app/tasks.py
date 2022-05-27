import requests
import re
import json

from lxml import etree
from .models import BaseTask, InformationFromDomain
from .celery import app


# URL адрес API содержащий базу данных по доменам
URL_DOMAINSDB = "https://api.domainsdb.info/v1/domains/search?domain="

# Константа очищающая с помощью регулярного выражения от префиксов
# "http://", "https://", "http://www.", "https://www."
CLEAR_D = re.compile(r"https?://(www\.)?")

# Константа отсеивающая только тег <a> с атрибутом href
A_HREF = "//a/@href"


def parse_data(celery_task_id: str, find_domain: str):
    new_task = BaseTask.objects.create(
        name_from_celery=celery_task_id,
        domain_from=find_domain
    )
    new_task.save()
    try:
        response = requests.get(find_domain)
        if response.status_code == 200:
            tree = etree.HTML(response.content)
            result = tree.xpath(A_HREF)
            all_domains = [
                f"{URL_DOMAINSDB}{(CLEAR_D.sub('', domain).strip().strip('/'))}"
                for domain in [
                    link for link in result if link.startswith('htt')
                ]
            ]
            for cur in all_domains:
                open_api = requests.get(cur)
                for item in open_api.json()['domains']:
                    cur_parsing_res = InformationFromDomain.objects.create(
                        task_name=new_task,
                        domain=item['domain'],
                        create_date=item['create_date'],
                        update_date=item['update_date'],
                        country=item['country'],
                        is_dead=item['isDead'],
                        a=item['A'],
                        ns=item['NS'],
                        cname=item['CNAME'],
                        mx=item['MX'],
                        txt=item['TXT']
                    )
                    cur_parsing_res.save()
    except Exception as e:
        print("Error: ", e)
    else:
        new_task.is_success = True
        new_task.save()


@app.task(name='create_task', bind=True)
def create_task(self, domain):
    parse_data(self.request.id, domain)
    return True
