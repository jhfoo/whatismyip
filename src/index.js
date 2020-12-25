const restify = require('restify'),
  server = restify.createServer(),
  PORT = 8080

function respond(req, res, next) {
  console.log(req.connection.remoteAddress)
  res.send(req.connection.remoteAddress);
  next();
}
  
server.get('/', respond);
server.head('/hello/:name', respond);

server.listen(PORT, () => {
  console.log('%s listening at %s', server.name, server.url);
})