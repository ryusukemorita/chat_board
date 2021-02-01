<h1>"Chat Board" について</h1>

<p>"Chat Board"は SNSのチャット機能のコアの部分を SPA(Single Page Application) で実装した簡易版チャットWebアプリケーションです。</p>

<# Site clip for your Coffee Time ☕

You can check out the app on [Heroku](https://coffeee-time.herokuapp.com/)!

![image](https://github.com/nouvelle/coffee-time/blob/master/images/desktop.png?raw=true)
![image](https://github.com/nouvelle/coffee-time/blob/master/images/smartphone.png?raw=true)

1. [About](#About)
1. [Development](#Development)
1. [Other command](#Other%20command)
1. [Technology used](#Technology%20used)
1. [Future features](#Future%20features)
1. [Contributing](#Contributing)
1. [License](#License)

# About

If you use this app, you can save the URLs you want to read later and read them together later.  
You can save what you have read, so you can read it immediately if you want to read it again.

# Development

Follow this guide to set up your environment etc.

## Database

This project assumes a Postgres database, naturally, this is not included in the package.json file, so must be installed separately.

If you are on Windows using WSL, [this blogpost](https://medium.com/@harshityadav95/postgresql-in-windows-subsystem-for-linux-wsl-6dc751ac1ff3) is very helpful.

Create a database called `coffeetime`.

Create a `.config.js` file in the project root with this format:

```
module.exports = {
  db: {
    client: "postgresql",
    connection: process.env.DATABASE_URL || {
      host: process.env.DB_HOST || "127.0.0.1",
      port: process.env.DB_PORT || 5432,
      database: process.env.DB_NAME || "coffeetime",
      user: "exampleUsername", // <= Your command line username
      password: "examplePassword", // <= Your command line
    }
  },
};

```

To clone and run this application, you'll need Git and Node.js (which comes with yarn) installed on your computer.  
From your command line:

**Downloading and installing steps**

1. Clone this repository

```bash
$ git clone https://github.com/nouvelle/coffee-time.git
```

2. Go into the repository

```bash
$ cd coffee-time
```

3. Install dependencies

```bash
$ yarn
```

4. Create database, Run migrations and set up the database

```bash
$ yarn migrate
```

5. Run the app

```bash
$ yarn start
```

# Other command

- To roll back migrations

```bash
$ yarn rollback
```

- To insert test data

```bash
$ yarn seed
```

# Technology used

This software uses the following open source packages:
![image](https://github.com/nouvelle/coffee-time/blob/master/images/technology.png?raw=true)

# Future features

For now, you can see the site clip data.  
I will be adding more function.

- [x] Save added data and read information into database.
- [ ] Show the history of your reading.
- [ ] Login function.
- [ ] Interactive animations.

# Contributing

Pull requests are welcome!! 😊
