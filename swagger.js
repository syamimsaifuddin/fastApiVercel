const swaggerJsdoc = require('swagger-jsdoc')
const swaggerUi = require('swagger-ui-express')
const YAML = require('yamljs');
const swaggerDoc = YAML.load('./swagger.yaml')

const options = {
  swaggerDefinition: {
    restapi: '3.0.0',
    info: {
      title: 'My API',
      version: '1.0.0',
      description: 'My REST API',
    },
    servers: [
      {
        url: 'http://localhost:3000',
      },
    ],
  },
  apis: ['./routes/*.js'],
}

const specs = swaggerJsdoc(options)

module.exports = (app) => {
    app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDoc))
}