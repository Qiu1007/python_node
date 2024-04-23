const { spawn } = require('child_process');

// 创建 Python 子进程
const pythonProcess = spawn('python', ['mytest.py']);

// 监听子进程的标准输出
pythonProcess.stdout.on('data', (data) => {
  console.log(`Python output:${data}`);
});

// 监听子进程的标准错误输出
pythonProcess.stderr.on('data', (data) => {
  console.error(`Python 错误：${data}`);
});

// 向子进程发送数据
pythonProcess.stdin.write('Hello from Node.js');
pythonProcess.stdin.end();