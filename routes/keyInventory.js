const express = require('express');
const router = express.Router();

router.post('/keyInventory', (req, res) => {
    console.log(req.body)
    // // Your code to handle the POST request (e.g., save the post to a database)
    res.status(201).json({ message: 'Post created successfully', output: req.body });
});

module.exports = router;
