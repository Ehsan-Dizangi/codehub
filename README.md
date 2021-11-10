<p align="center">
  <img src="git_components/gitbanner.png" width="550px">
  <br>
  <br>
  <b>CodeHub</b>
  <br>
  <span>Persian Pastebin Service</span>
  <br>
  <a href="README_fa.md">پارسی</a> ◆
  <a href="README.md">English</a>
  </p>

> :heavy_check_mark:: This project is being developed externally on [lnxpy/codehub](https://github.com/lnxpy/codehub), once all tests are passed and the project stabilized, all changes will be pushed to the current repository.

> :hibiscus:: Special thanks to those who tested the project and give me responses and ideas.

## CodeHub
CodeHub is a platform for archiving the errors, bugs, and scripts you intend to share with others. You may have seen the other samples anywhere but this platform is completely Persian, free and also accessible to all friends.
Not only you can share your programming problems in CodeHub, but also you can easily write handy scripts and modules and send them to your friends on social networks.

### API
CodeHub API services have been provided to make this service more flexible and accessible on any platform and devices you use. There are several ways to make a snippet or open up any of. You can use API services to have a tiny CodeHub on your local system with no dependencies.

#### 1. GET
Get all information about a snippet. You need to know the SnippetIdentification (SID) so you can read all data from the database.
```json
POINT: http://codehub.pythonanywhere.com/api/vX/snippet/<SID>

RESULT
{
    "SID": "##########",
    "title": "TITLE",
    "detail": "DETAILS",
    "script": "SCRIPT",
    "error": "ERROR",
    "language": "python",
    "pub_date": "۶ فروردین ۱۳۹۹",
    "link": "http://codehub.pythonanywhere.com/api/vX/snippet/############"
}
```
You may use all information about the CodeHub providers. You just need to change the end-point to `http://codehub.pythonanywhere.com/api/vX/team` and the result will be..
```json
[
    {
        "name": "علیرضا یحیی پور",
        "position": "برنامه نویس و توسعه دهنده ارشد",
        "passion": "علاقه زیادی به ساخت چیزای جدید دارم. قطعا کد هاب یکی از اون بهتریناس.",
        "github": "https://github.com/lnxpy",
        "linkedin": "https://www.linkedin.com/in/ali-reza-yahyapour-18b896164/",
        "twitter": "",
        "gmail": "lnxpylnxpy@gmail.com"
    },
    ...
]
```

#### 2. POST
Now you can post an object to the server and let it returns the link. Try this one.
```json
POINT: http://codehub.pythonanywhere.com/api/vX/snippet

DATA-STRUCTURE:
{
    "title": "TITLE",
    "detail": "DETAILS",
    "script": "SCRIPT",
    "error": "ERROR",
    "language": "python",
}

RETURNED DATA:
{
    "SID": "###########",
    "title": "TITLE",
    "detail": "DETAILS",
    "script": "SCRIPT",
    "error": "ERROR",
    "language": "python",
    "pub_date": "۶ فروردین ۱۳۹۹",
    "link": "http://codehub.pythonanywhere.com/api/vX/snippet/############"
}

```

Tip: `vX` means the API version you use. The first version (`v1`) is available now.

#### 3. Optionals (According to [CodeHub-CLI](https://github.com/CodeHub-Contributors/CodeHub-cli))
There are some fields you are able to leave them empty. `detail`and `error` fields are the optional parameters you may not want to fill them up, so you use the exact keywords to give other parameters the values you want.
```python
from components import GetSnippet, PushSnippet, Language

configs = {
    'title': 'TITLE',
    # 'details': 'DETAILS',  OPTIONAL PARAMETER
    'script': 'SCRIPT',
    # 'error': 'ERROR',      OPTIONAL PARAMETER
    'language': 'go',
}

snippet = PushSnippet(**configs).push()
print(snippet)
```
For more information click [here](https://github.com/CodeHub-Contributors/CodeHub-cli).

### Admin API
You may need to transfer data from the client side to the server using APIs, so there are no concerns. 
#### 1. Authentication
CodeHub is a Token-based website that allows admins to transfer data using Application/JSON style. After the migration you can access to `../api/vX/admin/login` or `../api/vX/admin/logout` to both logging in or logging out from the website.

#### 3. See Snippets
Use `../api/vX/admin/snippet` to show all saved snippets from all users. You can also use `../api/vX/admin/snippet/<SID>` for CRUD access.

#### 4. See Teammates
To see teammates and add how much you want, you can locate in `../api/vX/admin/team`. Use `../api/vX/admin/team/<ID>` to modify any teammate you want.

#### 5. See Suggestions
To change, create, and show any suggestion use the following addresses. (You have to be logged in as the superuser if you want the CRUD access)
```
../api/vX/admin/suggest/
../api/vX/admin/suggest/<ID>
```

### Find More
Find more details about the CodeHub in the main documentation which is [here](http://codehub.pythonanywhere.com/docs).

### Fork
Never mind, fork it. XD
