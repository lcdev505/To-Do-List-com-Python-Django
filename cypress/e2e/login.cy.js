describe('Login', () => {

  beforeEach(() => {
    cy.visit('/core/accounts/login/')
  })

  it('login com credenciais válidas', () => {
  cy.get('input[name="username"]').type('Lucas')
  cy.get('input[name="password"]').type('#Lucas2025*20')
  cy.get('button[type="submit"]').click()
  cy.url().should('include', '/core/home/')
  })

  it('login com senha incorreta', () => {
    cy.get('input[name="username"]').type('Lucas')
    cy.get('input[name="password"]').type('errada123')
    cy.get('button[type="submit"]').click()
    cy.contains('Suas tarefas').should('not.exist')
  })

  it('login com usuario inexistente', () => {
    cy.get('input[name="username"]').type('Errado')
    cy.get('input[name="password"').type('#Lucas2025*20')
    cy.get('button[type="submit"]').click()
    cy.contains('Nome de usuário ou senha inválidos').should('exist')
  })

  it('login com campos vazios', () => {
    cy.get('button[type="submit"]').click()
    cy.contains('Nome de usuário ou senha inválidos').should('exist')
  })

})