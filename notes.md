# General Notes 
1. You can make git leave out certain files and folders and you can put all these files in a folder named assets.
2. The configs are typically placed in .env like project name or an api secret key. and typically all capital and _ between the word. and the configs is either string or number only.
but this only can make errors because there's no file .env tracked in git. To solve this you should make an exact copy of it and name it .env.example without any secrets of course like api key.
3. You can make a collection in postman and even set variables to easily change it like the pain localhost:8000 and that by variables tab in the program.
4. If you want the server to automaticaly save every change in the app you can add --reload to the normal run 'uvicorn main:app' and if you want to expose this api to different users in the same network you can add --host (and the ip of that user without parnthses ) if you want all users just use --host 0.0.0.0 and if you want to change the port use --port.
5. Remember FastAPI came with swagger docs you can access it using 127.0.0.1/docs.
6. If you want to use and APIRouter in the app you can write it like this `app.include_router(router)` 
7. Some interesting note is that you can use the dot . to access something inside a file in module like this `file.something`.
8. It's recommended to make the route functions async.
9. It's recommended to use boilerplate for any framework. you can search it using something like this `fastapi boilerplate github`
10. It's recommended to make a folder called helpers that has some files that several other files use it like config.
11. You can validate various things like settings if there are str or int or something using pydantic_settings and its methods BaseSettings, SettingsConfigDict
12. What happens when for any reason when i call settings it didn't return ? error. You can use `Depends` from fastapi when making the route like this def welcome(app_settings=Depends(get_settings)).
13. It good practice to specify the paramater types when create function or routes.
14. To upload file in fastapi you can import it from fastapi like this `UploadFile`.
15. An important pro for pydantic_settings is that it can allow some composite variable types in .env like list.
16. DON'T FORGET TO FUCKING COPY ANY NEW ENV VARS TO .env.example.
17. DON'T FORGET TO FUCKING COPY ANY NEW ENV VARS INTO CONFIG HELPER IF YOU USED IT.
18. It's the best to separate different logic into its respective file like the validation logic in controller.
19. If there's something appears in multiple controllers it's best to make base controller which all other controllers to inherit from it.
20. Some pretty good advice is to use `__init__.py` in a directory to help import it like this. in the `__init__.py` write like this 'from .DataController import DataController' and in where to import it write it like this 'from controllers import DataController'
21. When using post man to upload file you can upload using body > form-data and enter your file.
22. When 404 error happens when making controllers or routers or staff don't forget to check if you added the router in the main.py
23. FUCK THIS ERROR. SINCE Pydantic v2 THE FUCKING CONFIG IS LIKE THIS NOT LIKE THE VIDEO
''' class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")
'''
24. Remember there's no list in .env
25. For better coordanation and understanding you should return signal ( not true or false only ) what is true ? what is false ? and a neat trick is python can return multilple things not only one.
26. Make sure if there's some constant in the code make it a variable and store it to retrieve it every time you need it. the best way to store it is enums.
27. Remember this status from fastapi and this JSONResponse.
28. It's far more effient for file uploading to split it chunk by chunk and to do this. you should use.
29. Don't forget to specify the mode of read in file.
30. Do logging do logging do logging. do it like this. 
31. Remember it's try except not try catch.
32. We can validate and force certain schemes in the request using pydantic. the same idea of settings.
33. LangChain is like a pipeline that some chains can take a document and split it and even answer a question but in production this not effient and moreover not customizable. We can take some compononts only in this chain like document loader
34. Remember any constants it's better to store it in enum to better control and call it.
35. After loading documents we should split the content into chunks 
36. Recursively split by character is good as it don't split in the middle of a word or important sentence
37. chunk_size is the size as obvious and chunk_overlap is that it gets back a number of chars as the splitter can split in the middle of an important information
38. Remember the loader returns document and the splitter works on text. remember this.
39. Remember in the text splitter it's called chunk_overlap not overlap_size.
40. When beginning a new docker compose file (That take multiple services and make them work together) we begin with services:
41. Important note how to write ports in docker to actually communicate with what inside the container from my machine is like this `- "the_port_in_my_machine:the_port_inside_container"` like for example if I'm create mongodb container and I want it on my machine with port 7415 i can do it like this `- "7415:27017"`
42. And like the ports like the volumes ( or where the data is) in the right what path inside the container in the left what path outside on my machine like this 
`- "./mongodb:/data/db"`
43. Don't forget to gitignore this data folder.
44. You should declare a network for the service you create
45. If you want to auto restart the service if it fails.
46. You can up the service by simply right click the docker-compose file and in the bottom there are compose options.
47. You can fucking simply use vs code to compose the container up.
48. Motor is recommended as it has good async capabilities.
49. A neat trick is that you can attach something in app and all that use app can see and interact with this thing like this `app.mongo_conn = bla`
50. Fast api events are awesome search about them.
51. You can make scheme like when we created settings. and you can make your own validator inside the scheme class.
52. A very important note is that pydantic is not allowing different types by default You should put it in the config from the beginning.
53. I don't know why specifily he created project and chunk schemes before create baseDataModel and collections
54. A neat trick that when we store into the database we take an object of the scheme to make sure all fields existed.
55. Remember when inserting the data should be dict in insert_one func
56. Remeber if it's async then we should await
57. in pydantic `.dict()` is depricated use `model_dump()` instead.
58. Every document create in Mongo if success will return inserted_id
59. In motor find_one() we pass dict as for what to search like this `{ "id" : id }`
60. Very Important note. to convert from dict to any model for example Project we can do it this way `Project(**data)`.
61. Be careful when creating get all. You should make Pagination.
62. Cursor is like someone who knows where the data will stop in the page and you just should follow him.
63. If you put request in the parameters of the router function this mean you want every detail of the request INCLUDING app
64. The fucking on_event is deprecated you can use lifespan instead.
65. Like in get all data remember also to make something to batch insert or create because it's ineffient to do otherwise. We can do so using bulk_write but this function takes a list of operations definations like InsertOne from pymongo which define the function but not run it.
66. Very important in pydantic if the variable name begins with _ like `_id`. it treats it as private so you can access it from the outside. You can solve this problem by using alias in Field. so you rename it without _ and then set alias to it with _ like this `id : Optional[ObjectId] = Field(None, alias="_id")` But this can lead to some problems as now id is always setted with None so motor (mongo) will not return id for the operation and object we can solve this using parameters from where the CRUD functions are ( which is models in MVC arch )
67. Things you always forget to access mongo from the terminal you can use `mongosh --port port_of_container` and to show all databases names you can write it like this `show dbs` and to show collections inside a specfic databse you should switch your work to this database first using `use database_name` and then you can show all collections by `show collections` and to get all documents in a collection you can write `db.collection_name.find()`.
68. It's prefered to name detete function (and i think find too) by the factor of deletion like this `delete_chunk_by_project_id.
69. To add credentials for mongodb in docker you can use 
```
    environment:
      - MONGO_INITDB_ROOT_USERNAME = username
      - MONGO_INITDB_ROOT_PASSWORD = password

```
70. But you defiently can't put secrets like username and password directly in docker file and moreover every user has different credintials so it should be put in `.env` (in the folder of docker a new `.env`) and don't forget to add the new thing to `.env.example`. 
71. and when putting the secrets in the docker compose we put it like this `MONGO_INITDB_ROOT_PASSWORD = ${name_of_env_varible}`.
72. In most cases there are some changes that we do in docker and sometimes we want to start over from the beginning. to do this we can run the following commands
```bash
$ sudo docker stop $(sudo docker ps -aq)
$ sudo docker rm $(sudo docker ps -aq)
$ sudo docker rmi $(sudo docker images -aq)
$ sudo docker volume rm $(sudo docker volume ls -q)
$ sudo docker system prune --all
```
and be careful this happens only in development not production
73. WHAT THE FUCK ? okay calm down. in docker compose file you should either key-value mapping without - or fuck leave it but with = between key, value instead of :. so either this `mongo_username : shit` or `-mongo_username = shit`
74. To avoid any future problem in the connection to mongodb you can use the following url `mongosh "mongodb://gemy:123@localhost:7412/?authSource=admin"` where gemy:123 is username : password and authSource is where to authenticate these credantials agains which database. 
75. Storing and retriving data from the database is like a book with million page if we have million record in the tradetional way it loop in each record and check you with me ? yes append him and next no ? don't append next. indexing solves this issue. by like exactly in the indexing of book. each topic begins with page number and next topic with another page number. so when requiring some topic then go the page number of it. It's exactly the same idea.
76. Static function ( inside class ) we can access without defining object from the class and doing that by add a decorator `@classmethod`.
77. You can use two indexes in one if two conditions always happens together this make it more effient and to use two indexes in one is creating a list of dictionaries with the number of indexes and conditions.
78. Remember indexing is either ascending ( 1 ) or descending ( -1 ).
79. Every index should have three important things which are key,name,unique like this 
    {
        "key": [
            ("project_id", 1)
        ],
        "name": "project_id_index_1",
        "unique": True
    }
80. Something self studied. Asyncio motor will be deprecated in 2026 so it's better to migrate to PyMongo Async API. and here's how to migrate : https://www.mongodb.com/docs/languages/python/pymongo-driver/current/reference/migration/
81. Be careful that `__init__()` cannot be async. if you want to call async function inside it you can simply escape calling the async function inside `__init__()` and make a third static function to call both of them the `__init__()` and the async function and for sure the third function will be async
82. Don't forget to await any async.
83. The on_event is deprecated like i mentioned above and the current way is using lifespan. We pass to the FastAPI object lifespan parameter which can be a function of the decorator `asynccontextmanager` and we name the function for example `async def lifespan(app: FastAPI). and we put yield in the function every thing BEFORE yield will be executed BEFORE the app start reciving requests and everything AFTER yield will be executed AFTER the app ends. 
84. `datetime.utcnow()` is now deprecated and the replacment is `datetime.now(timezone.utc)`
85. To get all documents from pymongo with find. we write `find(bla bla bla).toList(length = None)` length is the how many documents do you want to return.
86. A funny bug. Remeber in pydantic we don't initilize the class just putting the fields.
87. Some advanced bug i think. pydantic can't understand enum with it's default settings. we should pass mode = "json" and make the enum inherit from both str AND Enum.
88. Be careful when creating indexes make sure to start over because the collection may have some records violating the index.
89

# In requirements notes 
1. Leave a line in the end of the file. (If you didn't do this and when anyone add another package he will make a new line (\n) so the previous line go updated as well )
2. Don't ever leave the package without version ( you can find any package version when searching like this 'fastapi pypi')


# Structure notes
1. You should make routes folder to make the main.py minimal and the project itself scalable. and if you want to call any file from this folder inside the code this is called module and happens when the file `__init__.py` is created inside a folder.
2. You can use APIRouter to make routes outside the `main.py`.
3. When you use dotenv and to call it one time from main.py you should import `load_dotenv` before any other imports like routes for example