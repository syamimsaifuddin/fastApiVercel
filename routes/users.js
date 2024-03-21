/**
 * @swagger
 * /users:
 *   get:
 *     description: Get all users
 *     responses:
 *       200:
 *         description: Success
 */
const express = require('express');
const router = express.Router();

router.get('/users', (req, res) => {
    res.send('Hello');
});

module.exports = router;
