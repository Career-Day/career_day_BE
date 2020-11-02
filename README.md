# career_day_BE
Stack: Python3, Flask, Postgres, Heroku

1. set up virtualenv or pipenv, activate the virtual environment
2. pip install -r requirements.txt
3. create a postgresql database:
    ```
    $ psql
    # create database career_day;
    ```
4. set up the project database:
    ```
    flask db init
    flask db migrate
    flask db upgrade
    flask db_seed
    ```
5. run the server
    ```
    flask run
    ```
6. run model tests with coverage:
    ```
    $ pytest --cov=app tests/
    ```
7. run integration tests
    * First, click the button below to download the Career Day Postman collections to your local client:
    [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/c226a3ff3a643f0456f7)
    * Next, ensure the app is running with `flask run` in the command line
    * Finally, to run the tests, in Postman:
      1. Click `Runner` at the top left
      2. In the new window that opens up, click on the Career Day collection on the left
      3. Then click the blue Run Career Day button to run all the tests
    * To examine or run just one test, in the main Postman app click on the `Tests` tab of one of the requests and click the blue `Send` button

## Endpoints
### Jobs Index Endpoint
Example response for this request: ```GET ‘https://.herokuapp.com/api/v1/jobs’```

```json

{
    "jobs": [
        {
            "avg_salary": "47,500",
            "education": "Bachelor's degree in graphic design",
            "icon_url": "https://www.flaticon.com/svg/static/icons/svg/2192/2192721.svg",
            "id": 1,
            "short_description": "Graphic designers develop graphics and layouts for product illustrations, company logos, websites and more.",
            "title": "Graphic Designer"
        }, 
    ]
}
```
### Job Show Endpoint
```GET ‘https://.herokuapp.com/api/v1/jobs/(id)’```


```json
{
    "job": {
        "education": "Bachelor's degree in graphic design",
        "id": 1,
        "image_url": "https://www.freepik.com/blog/app/uploads/2018/07/PIN-BLOG-1270x720-What-is-the-difference-between-an-illustrator-and-a-graphic-designer-1.jpg",
        "long_description": "Graphic designers are visual communicators, who create visual concepts by hand or by using computer software. They communicate ideas to inspire, inform, or captivate consumers through both physical and virtual art forms that include images, words, or graphics. The end goal of graphic designers is to make the organizations that hire them more well known by their designs. By using a variety of media they communicate a particular idea to be used in advertising and promotions. These media include fonts, shapes, colors, images, print design, photography, animation, logos, and billboards. Graphic designers often work on projects with artists, multimedia animators and other creative professionals.",
        "max_salary": "60,000",
        "min_salary": "35,000",
        "title": "Graphic Designer",
        "video_url": "https://www.youtube.com/watch?v=kqwgs7vBMkU"
    }
}
```

### Team
[Phillip Strom](https://www.linkedin.com/in/phillipstrom/)

[Jane Greene](https://www.linkedin.com/in/jane-greene-mba/)

[Dan Sehl](https://linkedin.com/in/danielsehl)
