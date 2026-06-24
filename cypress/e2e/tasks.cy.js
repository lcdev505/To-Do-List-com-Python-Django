describe('Tasks', () => {
    beforeEach(() => {
        cy.login()
    })
    
    it('criando tarefa com dados válidos e verificando se existe', () => {
        const task = `Tarefa_${Date.now()}`
        cy.visit('/core/adicionar/')
        cy.get('input[name="nome"]').type(task)
        cy.get('textarea[name="descricao"]').type(task)
        cy.get('button[type="submit"]').click()
        cy.contains(task).should('exist')
    })

    it('criando tarefa com campos vazios', () => {
        cy.visit('/core/adicionar/')
        cy.get('button[type="submit"]').click()
        cy.get('input[name="nome"]').then(($input) => {
            expect($input[0].validationMessage).to.not.be.empty
        })
    })

    it('atualizando uma tarefa existente', () => {
        const task = `Tarefa_${Date.now()}`
        cy.visit('/core/adicionar/')
        cy.get('input[name="nome"]').type(task)
        cy.get('textarea[name="descricao"]').type(task)
        cy.get('button[type="submit"]').click()
        cy.contains('tr', task).find('.btn-edit').click()
        cy.get('input[name="nome"]').clear().type('Tarefa Atualizada')
        cy.get('textarea[name="descricao"]').clear().type('Tarefa Atualizada')
        cy.get('button[type="submit"]').click()
        cy.contains('Tarefa Atualizada').should('exist')
    })

    it('deletando uma tarefa existente', () => {
        const task = `Tarefa_${Date.now()}`
        cy.visit('/core/adicionar/')
        cy.get('input[name="nome"]').type(task)
        cy.get('textarea[name="descricao"]').type(task)
        cy.get('button[type="submit"]').click()
        cy.contains('tr', task).find('.btn-delete').click()
        cy.contains(task).should('not.exist')
    })
})