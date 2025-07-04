const modalcadastro = new bootstrap.Modal(document.getElementById('modalcadastro'));
let idcontatoatual = 0;

// Função para mostrar feedback visual
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

// Função para mostrar loading nos botões
const setButtonLoading = (button, isLoading, action = '') => {
    if (isLoading) {
        button.innerHTML = `<i class="fas fa-spinner fa-spin"></i>`;
        button.disabled = true;
    } else {
        const icon = action === 'edit' ? 'fa-edit' : 'fa-trash';
        const text = action === 'edit' ? 'Alterar' : 'Excluir';
        button.innerHTML = `<i class="fas ${icon}"></i> ${text}`;
        button.disabled = false;
    }
};

// Função para carregar categorias no select
async function carregarCategorias() {
    try {
        const response = await fetch("http://127.0.0.1:5000/categorias");
        if (!response.ok) throw new Error('Erro ao carregar categorias');
        
        const categorias = await response.json();
        const select = document.getElementById("id_categoria");
        
        // Salva a seleção atual
        const selectedValue = select.value;
        
        // Limpa e adiciona as novas opções
        select.innerHTML = '<option value="">Selecione uma categoria</option>';
        
        categorias.forEach(cat => {
            const option = document.createElement("option");
            option.value = cat.id_categoria;
            option.textContent = `${cat.id_categoria} - ${cat.categoria}`;
            select.appendChild(option);
        });
        
        // Restaura a seleção anterior, se existir
        if (selectedValue) {
            select.value = selectedValue;
        }
        
        return categorias;
    } catch (error) {
        console.error("Erro ao carregar categorias:", error);
        showToast('Erro ao carregar categorias', false);
        return [];
    }
}

async function alterar(id_contato) {
    const buttons = document.querySelectorAll(`button[onclick="alterar(${id_contato})"]`);
    buttons.forEach(btn => setButtonLoading(btn, true, 'edit'));

    try {
        // Carrega as categorias primeiro
        await carregarCategorias();
        
        const response = await fetch(`http://127.0.0.1:5000/contato/${id_contato}`);
        if (!response.ok) throw new Error('Erro ao carregar contato');
        
        const dados = await response.json();
        idcontatoatual = id_contato;
        document.getElementById("nome").value = dados.nome;
        document.getElementById("telefone").value = dados.telefone;
        document.getElementById("email").value = dados.email;
        
        // Define a categoria selecionada pelo ID
        if (dados.id_categoria) {
            document.getElementById("id_categoria").value = dados.id_categoria;
        } else {
            document.getElementById("id_categoria").value = "";
        }
        
        modalcadastro.show();
        showToast('Contato carregado com sucesso');
    } catch (error) {
        console.error("Erro:", error);
        showToast(error.message, false);
    } finally {
        buttons.forEach(btn => setButtonLoading(btn, false, 'edit'));
    }
}

async function excluir(id_contato) {
    const modalHtml = `
        <div class="custom-modal">
            <div class="modal-confirm">
                <div class="modal-icon warning">
                    <i class="fas fa-exclamation-triangle"></i>
                </div>
                <h3>Confirmar Exclusão</h3>
                <p>Tem certeza que deseja excluir este contato?</p>
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
                const response = await fetch(`http://127.0.0.1:5000/contato/${id_contato}`, {
                    method: "DELETE"
                });

                if (!response.ok) throw new Error('Erro ao excluir contato');

                showToast('Contato excluído com sucesso');
                listar();
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

function novo() {
    idcontatoatual = 0;
    document.getElementById("nome").value = "";
    document.getElementById("telefone").value = "";
    document.getElementById("email").value = "";
    
    // Carrega as categorias e depois mostra o modal
    carregarCategorias().then(() => {
        document.getElementById("id_categoria").value = "";
        
        // Efeito visual no botão
        const btn = document.querySelector('button[onclick="novo()"]');
        if (btn) {
            btn.classList.add('btn-pulse');
            setTimeout(() => {
                btn.classList.remove('btn-pulse');
                modalcadastro.show();
            }, 300);
        } else {
            modalcadastro.show();
        }
    });
}

async function salvar() {
    const vnome = document.getElementById("nome").value.trim();
    const vtelefone = document.getElementById("telefone").value.trim();
    const vemail = document.getElementById("email").value.trim();
    const vid_categoria = document.getElementById("id_categoria").value;

    // Validação básica
    if (!vnome || !vtelefone) {
        showToast('Preencha pelo menos nome e telefone', false);
        return;
    }

    const button = document.querySelector('#modalcadastro .btn-save');
    const originalText = button.innerHTML;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
    button.disabled = true;

    const contato = {
        nome: vnome,
        telefone: vtelefone,
        email: vemail,
        categoria: vid_categoria || null
    };

    const url = idcontatoatual > 0 
        ? `http://127.0.0.1:5000/contato/${idcontatoatual}`
        : 'http://127.0.0.1:5000/contato';
    const method = idcontatoatual > 0 ? 'PUT' : 'POST';

    try {
        const response = await fetch(url, {
            method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(contato)
        });

        if (!response.ok) throw new Error(idcontatoatual > 0 
            ? 'Erro ao atualizar contato' 
            : 'Erro ao criar contato');

        showToast(idcontatoatual > 0 
            ? 'Contato atualizado com sucesso!' 
            : 'Contato criado com sucesso!');
        
        listar();
        modalcadastro.hide();
    } catch (error) {
        console.error("Erro:", error);
        showToast(error.message, false);
    } finally {
        button.innerHTML = originalText;
        button.disabled = false;
    }
}

async function listar() {
    const lista = document.getElementById("lista");
    lista.innerHTML = `
        <tr>
            <td colspan="6" class="loading-row">
                <i class="fas fa-spinner fa-spin"></i> Carregando contatos...
            </td>
        </tr>
    `;

    try {
        const response = await fetch("http://127.0.0.1:5000/contatos");
        if (!response.ok) throw new Error('Erro ao carregar contatos');
        
        const dados = await response.json();
        mostrar(dados);
    } catch (error) {
        console.error("Erro:", error);
        lista.innerHTML = `
            <tr>
                <td colspan="6" class="error-row">
                    <i class="fas fa-exclamation-triangle"></i> ${error.message}
                </td>
            </tr>
        `;
    }
}

function mostrar(dados) {
    const lista = document.getElementById("lista");
    
    if (!dados || dados.length === 0) {
        lista.innerHTML = `
            <tr>
                <td colspan="6" class="empty-row">
                    <i class="fas fa-inbox"></i> Nenhum contato encontrado
                </td>
            </tr>
        `;
        return;
    }

    lista.innerHTML = dados.map(item => `
        <tr>
            <td>${item.id_contato}</td>
            <td>${item.nome}</td>
            <td>${item.telefone}</td>
            <td>${item.email}</td>
            <td>${item.categoria || '-'}</td>
            <td class="action-buttons">
                <button class="btn-edit" onclick="alterar(${item.id_contato})">
                    <i class="fas fa-edit"></i> Alterar
                </button>
                <button class="btn-delete" onclick="excluir(${item.id_contato})">
                    <i class="fas fa-trash"></i> Excluir
                </button>
            </td>
        </tr>
    `).join('');
}