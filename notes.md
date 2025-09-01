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

# In requirements notes 
1. Leave a line in the end of the file. (If you didn't do this and when anyone add another package he will make a new line (\n) so the previous line go updated as well )
2. Don't ever leave the package without version ( you can find any package version when searching like this 'fastapi pypi')


# Structure notes
1. You should make routes folder to make the main.py minimal and the project itself scalable. and if you want to call any file from this folder inside the code this is called module and happens when the file `__init__.py` is created inside a folder.
2. You can use APIRouter to make routes outside the `main.py`.
3. When you use dotenv and to call it one time from main.py you should import `load_dotenv` before any other imports like routes for example