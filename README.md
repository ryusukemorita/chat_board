# Chat Board !!!

![image](https://github.com/ryusukemorita/chat_board/blob/master/image/demo.gif?raw=true)

1. [About](#About)
1. [Development](#Development)
1. [Other command](#Other%20command)
1. [Technology used](#Technology%20used)
1. [Future features](#Future%20features)
1. [Contributing](#Contributing)
1. [License](#License)

# About

"Chat Board" is a simplified chat web application that implements the core part of the chat function of SNS with SPA (Single Page Application).
If you use this app, you can post your message and read the other user's message.  

Please Access Here!!!!

🔽  🔽  🔽  🔽  🔽  🔽  🔽  🔽  🔽  🔽
https://chat--board.herokuapp.com/


# Development

Follow this guide to set up your environment etc.

To clone and run this application, you'll need Git and Node.js (which comes with yarn) installed on your computer.  
From your command line:

**Downloading and installing steps**

1. Clone this repository

```bash
$ git clone https://github.com/ryusukemorita/chat_board.git
```

2. Go into the repository

```bash
$ cd chat_board
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
![image](https://github.com/ryusukemorita/chat_board/blob/master/image/tec.gif)

# Future features

For now, you can see the site clip data.  
I will be adding more function.

- [x] Save added data and read information into database.
- [ ] Show the history of your reading.
- [ ] Login function.
- [ ] Interactive animations.

# Contributing

Pull requests are welcome!!
