import json
import pytest
from app import db, JobsModel


def test_JobsModel(app):
    app.testing = True
    jobs = JobsModel.query.all()
    assert len(jobs) == 15
    assert jobs[0].title == 'Graphic Designer'
    assert jobs[0].icon_url == 'https://www.flaticon.com/svg/static/icons/svg/2192/2192721.svg'
    assert jobs[0].image_url == 'https://www.freepik.com/blog/app/uploads/2018/07/PIN-BLOG-1270x720-What-is-the-difference-between-an-illustrator-and-a-graphic-designer-1.jpg'
    assert jobs[0].video_url == "https://www.youtube.com/watch?v=kqwgs7vBMkU"
    assert jobs[0].min_salary == '35,000'
    assert jobs[0].max_salary == '60,000'
    assert jobs[0].avg_salary == '47,500'
    assert jobs[0].education == "Bachelor's degree in graphic design"
    assert jobs[0].short_description == "Graphic designers develop graphics and layouts for product illustrations, company logos, websites and more."
    assert jobs[0].long_description == "Graphic designers are visual communicators, who create visual concepts by hand or by using computer software. They communicate ideas to inspire, inform, or captivate consumers through both physical and virtual art forms that include images, words, or graphics. The end goal of graphic designers is to make the organizations that hire them more well known by their designs. By using a variety of media they communicate a particular idea to be used in advertising and promotions. These media include fonts, shapes, colors, images, print design, photography, animation, logos, and billboards. Graphic designers often work on projects with artists, multimedia animators and other creative professionals."

    # assert jobs[0].title == 'Graphic Designer'
    # client = app.test_client()
    # response = client.get('/api/v1/jobs/')
    # print(response)
    # data = json.loads(response.data.decode())
    # assert response.status_code == 200

# def func(x):
#     return x + 1
#
#
# def test_answer():
    # assert func(4) == 5
