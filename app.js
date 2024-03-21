const express = require('express');
const swagger = require('./swagger');
const usersRouter = require('./routes/users');
const keyInventory = require('./routes/keyInventory')
const keyMarks = require('./routes/keyMarks')

const app = express();

app.use(express.json())
app.get('/users', usersRouter);
app.post('/keyInventory', keyInventory)
app.post('/keyMarks', keyMarks)

swagger(app); // Swagger documentation

export default app;
// const PORT = process.env.PORT || 3000;
// app.listen(PORT, () => {
//     console.log(`Server is running on port ${PORT}`);
// });
