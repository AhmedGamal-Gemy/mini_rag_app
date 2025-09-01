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


# In requirements notes 
1. Leave a line in the end of the file. (If you didn't do this and when anyone add another package he will make a new line (\n) so the previous line go updated as well )
2. Don't ever leave the package without version ( you can find any package version when searching like this 'fastapi pypi')


# Structure notes
1. You should make routes folder to make the main.py minimal and the project itself scalable. and if you want to call any file from this folder inside the code this is called module and happens when the file `__init__.py` is created inside a folder.
2. You can use APIRouter to make routes outside the `main.py`.
3. When you use dotenv and to call it one time from main.py you should import `load_dotenv` before any other imports like routes for example