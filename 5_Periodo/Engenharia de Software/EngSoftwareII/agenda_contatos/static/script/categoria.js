const modalcadastro = new bootstrap.Modal(document.getElementById('modalcadastro'));
let idcategoriaatual = 0;

// Função para mostrar loading nos botões
const setButtonLoading = (button, isLoading) => {
    if (isLoading) {
        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        button.disabled = true;
    } else {
        const action = button.classList.contains('btn-edit') ? 'Alterar' : 'Excluir';
        const icon = button.classList.contains('btn-edit') ? 'fa-edit' : 'fa-trash';
        button.innerHTML = `<i class="fas ${icon}"></i> ${action}`;
        button.disabled = false;
    }
};

// Função para mostrar mensagem flutuante
const showToast = (message, isSuccess = true) => {
    const toast = document.createElement('div');
    toast.className = `custom-toast ${isSuccess ? 'success' : 'error'}`;
    toast.innerHTML = `
        <i class="fas ${isSuccess ? 'fa-check-circle' : 'fa-exclamation-circle'}"></i>
        <span>${message}</span>
    `;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => {
                document.body.removeChild(toast);
            }, 300);
        }, 3000);
    }, 100);
};

async function alterarcategoria(categoria) {
    const button = document.querySelector(`.btn-edit[onclick="alterarcategoria(${categoria})"]`);
    if (button) setButtonLoading(button, true);

    try {
        const response = await fetch(`http://127.0.0.1:5000/categoria/${categoria}`);
        if (!response.ok) throw new Error('Erro ao carregar categoria');
        
        const dados = await response.json();
        idcategoriaatual = categoria;
        document.getElementById("categoria").value = dados.categoria;
        modalcadastro.show();
        showToast('Categoria carregada com sucesso');
    } catch (error) {
        console.error("Erro:", error);
        showToast(error.message, false);
    } finally {
        if (button) setButtonLoading(button, false);
    }
}

async function excluircategoria(categoria) {
    // Modal customizado no estilo do sistema
    const modalHtml = `
        <div class="custom-modal">
            <div class="modal-confirm">
                <div class="modal-icon warning">
                    <i class="fas fa-exclamation-triangle"></i>
                </div>
                <h3>Confirmar Exclusão</h3>
                <p>Tem certeza que deseja excluir esta categoria?</p>
                <div class="modal-buttons">
                    <button class="btn-cancel">
                        <i class="fas fa-times"></i> Cancelar
                    </button>
                    <button class="btn-confirm">
                        <i class="fas fa-trash"></i> Excluir
                    </button>
                </div>
            </div>
        </div>
    `;

    const modal = document.createElement('div');
    modal.innerHTML = modalHtml;
    document.body.appendChild(modal);

    return new Promise((resolve) => {
        modal.querySelector('.btn-cancel').addEventListener('click', () => {
            document.body.removeChild(modal);
            resolve(false);
        });

        modal.querySelector('.btn-confirm').addEventListener('click', async () => {
            const button = modal.querySelector('.btn-confirm');
            button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            button.disabled = true;

            try {
                const response = await fetch(`http://127.0.0.1:5000/categoria/${categoria}`, {
                    method: "DELETE"
                });

                if (!response.ok) throw new Error('Erro ao excluir categoria');

                showToast('Categoria excluída com sucesso');
                listarcategoria();
                resolve(true);
            } catch (error) {
                console.error("Erro:", error);
                showToast(error.message, false);
                resolve(false);
            } finally {
                document.body.removeChild(modal);
            }
        });
    });
}

function novocategoria() {
    idcategoriaatual = 0;
    document.getElementById("categoria").value = "";
    
    // Efeito visual no botão
    const btn = document.querySelector('button[onclick="novocategoria()"]');
    if (btn) {
        btn.classList.add('btn-pulse');
        setTimeout(() => {
            btn.classList.remove('btn-pulse');
            modalcadastro.show();
        }, 300);
    } else {
        modalcadastro.show();
    }
}

async function salvarcategoria() {
    const vcategoria = document.getElementById("categoria").value.trim();
    if (!vcategoria) {
        showToast('Por favor, preencha o nome da categoria', false);
        return;
    }

    const button = document.querySelector('#modalcadastro .btn-primary');
    const originalText = button.innerHTML;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
    button.disabled = true;

    const categoria = { categoria: vcategoria };
    const url = idcategoriaatual > 0 
        ? `http://127.0.0.1:5000/categoria/${idcategoriaatual}`
        : 'http://127.0.0.1:5000/categoria';
    const method = idcategoriaatual > 0 ? 'PUT' : 'POST';

    try {
        const response = await fetch(url, {
            method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(categoria)
        });

        if (!response.ok) throw new Error(idcategoriaatual > 0 
            ? 'Erro ao atualizar categoria' 
            : 'Erro ao criar categoria');

        showToast(idcategoriaatual > 0 
            ? 'Categoria atualizada com sucesso!' 
            : 'Categoria criada com sucesso!');
        
        listarcategoria();
        modalcadastro.hide();
    } catch (error) {
        console.error("Erro:", error);
        showToast(error.message, false);
    } finally {
        button.innerHTML = originalText;
        button.disabled = false;
    }
}

async function listarcategoria() {
    const lista = document.getElementById("lista");
    lista.innerHTML = `
        <tr>
            <td colspan="3" class="loading-row">
                <i class="fas fa-spinner fa-spin"></i> Carregando categorias...
            </td>
        </tr>
    `;

    try {
        const response = await fetch("http://127.0.0.1:5000/categorias");
        if (!response.ok) throw new Error('Erro ao carregar categorias');
        
        const dados = await response.json();
        mostrarcategoria(dados);
    } catch (error) {
        console.error("Erro:", error);
        lista.innerHTML = `
            <tr>
                <td colspan="3" class="error-row">
                    <i class="fas fa-exclamation-triangle"></i> ${error.message}
                </td>
            </tr>
        `;
    }
}

function mostrarcategoria(dados) {
    const lista = document.getElementById("lista");
    
    if (!dados || dados.length === 0) {
        lista.innerHTML = `
            <tr>
                <td colspan="3" class="empty-row">
                    <i class="fas fa-inbox"></i> Nenhuma categoria encontrada
                </td>
            </tr>
        `;
        return;
    }

    lista.innerHTML = dados.map(item => `
        <tr>
            <td>${item.id_categoria}</td>
            <td>${item.categoria}</td>
            <td class="action-buttons">
                <button class="btn-edit" onclick="alterarcategoria(${item.id_categoria})">
                    <i class="fas fa-edit"></i> Alterar
                </button>
                <button class="btn-delete" onclick="excluircategoria(${item.id_categoria})">
                    <i class="fas fa-trash"></i> Excluir
                </button>
            </td>
        </tr>
    `).join('');
}