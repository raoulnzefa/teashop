<div align="center">
  <img src="https://user-images.githubusercontent.com/93079515/178122213-77afd716-d0c2-4db3-9751-16f7a4b43fe6.png" width="30%"></img> 
</div>
<h1 align="center">TeaShop</h1>

<h3>An online store created in a minimalistic and clear style. The idea was to create a website for a tea producer with its own blends.
</h3>

<div align="center">
<img src="https://user-images.githubusercontent.com/93079515/178141316-70d799bf-137f-4c72-ba20-a703afde2076.gif" width="80%"></img>
</div>

<h2 align="center"> Build with </h2>

<div align="center">
<img src="https://user-images.githubusercontent.com/93079515/178142153-e6aabb2a-70ae-460f-9a3e-be567bb25c28.svg" width="90%"></img> 
</div>

<br>

<!-- GETTING STARTED -->
<h1 align="center">
  Getting Started
</h1>
<h4 align="center">Here you can find instruction step by step how to run TeaShop project locally.</h4>


<h2 align="center"> The software you need </h2>

<h4>Install python 3.9 or newer from <a href="https://www.python.org/">Python.org</a></h4>
<h4>Install nodejs from <a href="https://nodejs.org/en/">nodejs.org</a></h4>
<h4>If u don't have code editor install <a href="https://www.jetbrains.com/pycharm/">PyCharm</a> or <a href="https://code.visualstudio.com">Visual Studio Code</a></h4>

<h2 align="center"> Installation </h2>
<h4>Clone repository to your folder</h4>

```ps
git clone https://github.com/kacperkrasnal/teashop.git
```

<h3>Backend</h3>

<h4>1. Install virtualenv in terminal</h4>

```ps
pip install virtualenv
```

<h4>2. Create virtual environment in terminal</h4>
Inside teashop folder which include folders like 'backend' and 'frontend'

```ps
virtualenv venv
```

<h4>3. Activate venv</h4>

<img src="https://user-images.githubusercontent.com/93079515/178146913-0e4cd308-a7bb-48d8-8934-660c86ff6117.jpeg" width="90%"></img>

Windows
```ps
.\venv\Scripts\activate
```

Unix or MacOS using the bash shell
```bs
source /venv/Scripts/bin/activate
```

<h4>4. Install required packages using command</h4>

```ps
pip install -r requirements.txt
```


<h4>5. Prepare .env:</h4> 
Inside 'backend' folder prepare .env-example by removing from file name '-example'  <br>  File should have name '.env' and contain

```py
SECRET_KEY = example_name
DEBUG = True
```

<h4>6. Migrate</h4>
Inside 'backend' folder put in terminal

```ps
python manage.py migrate
```

<h4>7. Create two separate terminals 'frontend' and 'backend'</h4>
Go into backend terminal and navigate inside folder named 'backend'

<img src="https://user-images.githubusercontent.com/93079515/178148165-ccd27426-c57b-4104-bd20-2f5bc354208e.jpeg" width="90%"></img>

<h4>8. Run backend server</h4>

```ps
python manage.py runserver 
```

<h3>Frontend</h3>

<h4>1. Go into frontend terminal and navigate inside folder named 'frontend'</h4>

<img src="https://user-images.githubusercontent.com/93079515/178148164-bd04306a-54b6-4859-992b-765cf1a49d0b.jpeg" width="90%"></img>

<h4>2. Install npm packages with following command</h4>

```ps
npm install
```

<h4>3. Run frontend server</h4>

```ps
npm run serve
```

<h3 align="center">Everything done just open <a href="http://localhost:8080/">localhost</a> page</h3>

<h1 align="center">
  Usage
</h1>









