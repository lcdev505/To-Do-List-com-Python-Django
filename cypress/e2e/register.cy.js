describe('Register', () => {
    
    beforeEach(() => {
        cy.visit('/core/accounts/register/')
    })
    
    it('cadastro com dados válidos', () => {
        const username = `teste_${Date.now()}`
        cy.get('input[name="username"]').type(username)
        cy.get('input[name="email"]').type('teste@email.com')
        cy.get('input[name="password"]').type('testesenha')
        cy.get('input[name="password_confirm"]').type('testesenha')
        cy.get('button[type="submit"]').click()
        cy.contains('Conecte-se a sua conta').should('exist')
    })

    it('cadastro com senhas diferentes', () => {
        cy.get('input[name="username"]').type('teste')
        cy.get('input[name="email"]').type('teste@email.com')
        cy.get('input[name="password"]').type('testesenha')
        cy.get('input[name="password_confirm"]').type('senha')
        cy.get('button[type="submit"]').click()
        cy.contains('As senhas não coincidem').should('exist')
    })

    it('cadastro com usuario já cadastrado', () => {
        cy.get('input[name="username"]').type('teste')
        cy.get('input[name="email"]').type('teste@email.com')
        cy.get('input[name="password"]').type('teste')
        cy.get('input[name="password_confirm"]').type('teste')
        cy.get('button[type="submit"]').click()
        cy.contains('Este nome de usuário já está em uso').should('exist')
    })

    it('cadastro com campos vazios', () => {
        cy.get('button[type="submit"]').click()
        cy.get('input[name="username"]').then(($input) => {
            expect($input[0].validationMessage).to.not.be.empty
        })
    })
})