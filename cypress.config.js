const { defineConfig } = require("cypress");

module.exports = defineConfig({
  allowCypressEnv: false,

  e2e: {
    baseUrl: "https://to-do-list-com-python-django-production.up.railway.app",
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
