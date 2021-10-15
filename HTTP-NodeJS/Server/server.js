class Queue
{
    constructor()
    {
        this.items = [];
    }
    enqueue(element)
    {
        this.items.push(element);
    }
    dequeue()
    {
        this.items.shift();
    }
    printQueue()
    {
        let str = "";
        for(let i = 0; i < this.items.length; i++)
            str += this.items[i] +"\n";
        return str;
    }
    size () {
        return  this.items.length
    }

}
const queue = new Queue();
const http = require('http');
const hostname = '127.0.0.1';
const port = 8000;

const server = http.createServer(async (req, res) => {
    const buffers = [];
    for await (const chunk of req) {
        buffers.push(chunk);
    }
    const data = Buffer.concat(buffers).toString();
    console.log(`Body: ${data}`)
    if(req.method==='POST' && data!='' )
    {
        if(queue.size()<5)
        {
            queue.enqueue(data);
        }
        else
        {
            queue.dequeue();
            queue.enqueue(data);
        }
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end("Данные успешно записаны");
    }
    if(req.method==='GET' )
    {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end(queue.printQueue());
    }

});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
