const {PythonShell} = require("python-shell");

PythonShell.run('db.py', null).then(x=>{
    console.log(x);
    console.log('finished');
  });

  PythonShell.run('main.py', null).then(x=>{
    console.log(x);
    console.log('finished');
  });