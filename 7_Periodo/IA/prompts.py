"""Templates de prompt para extracao.

Este arquivo concentra a instrucao enviada ao modelo.
"""


PROMPT_BASE = """Voce e um analista de RH especializado em extracao estruturada de informacoes de vagas.

Sua tarefa e analisar o anuncio e extrair informacoes com alto rigor, garantindo maxima fidelidade ao texto.

IMPORTANTE:
- Pense passo a passo internamente antes de responder
- Verifique consistencia entre campos antes de gerar o JSON final
- Nao inclua qualquer explicacao, raciocinio ou texto adicional
- Retorne APENAS um JSON valido

Campos esperados:
- cargo (string): titulo da vaga
- empresa (string ou null): nome da empresa contratante
- localidade (string ou null): cidade ou estado
- modalidade (string): "remoto", "hibrido" ou "presencial"
- nivel (string ou null): "estagio", "junior", "pleno" ou "senior"
- salario (objeto ou null): com campos "min" e "max" (numeros ou null)
- requisitos (lista de strings): habilidades exigidas explicitamente no texto
- beneficios (lista de strings): beneficios oferecidos explicitamente no texto

REGRAS IMPORTANTES:
- Nao invente informacoes que nao estejam explicitamente no anuncio
- Use null para campos ausentes
- Salario "a combinar" ou nao mencionado = null
- Normalize para minusculas e sem acentos apenas os valores de nivel e modalidade
- Preserve o texto original dos demais campos sempre que possivel, sem inventar padronizacoes desnecessarias
- Se houver multiplas interpretacoes, escolha a mais conservadora
- Extraia apenas informacoes diretamente suportadas pelo texto
- O campo empresa deve capturar o nome da organizacao quando ela estiver explicitamente citada, mesmo que venha precedida por palavras como "startup", "empresa", "consultoria", "grupo" ou "instituto"
- Quando aparecer algo como "startup BlueLab", extraia empresa = "BlueLab", nao null
- Quando o anuncio seguir padroes como "TechHub abre vaga", "Empresa X contrata", "vaga na Y" ou "procurado pela Z", extraia o nome citado como empresa
- Quando houver formulacoes como "Oportunidade Junior na DataSolutions" ou "Vaga Pleno no Grupo X", interprete "na/no + nome" como empresa explicita
- Se a primeira frase trouxer nivel e empresa, mas o cargo aparecer depois em outra frase, use o cargo explicitamente citado depois
- O campo nivel so deve ser preenchido quando o nivel estiver explicitamente declarado no anuncio ou no proprio cargo, como "estagiario", "junior", "pleno" ou "senior"
- Nao infira nivel com base em contexto vago como portfolio, experiencia, inicio de carreira, responsabilidades ou stack; se nao estiver declarado, use null

REGRAS ESPECIFICAS PARA REQUISITOS E BENEFICIOS:
- Requisitos sao exigencias para candidatura, como formacao, curso, periodo, experiencia, habilidades, ferramentas, certificacoes ou idiomas
- Beneficios sao vantagens oferecidas pela vaga, como bolsa-auxilio, vale-transporte, vale-refeicao, plano de saude, bonus ou horarios flexiveis
- Nunca classifique pagamento, bolsa, auxilio ou beneficio como requisito
- Se o anuncio disser que a vaga e para estudantes de determinado curso ou a partir de certo periodo, isso deve entrar em requisitos
- Quando houver "bolsa-auxilio" com valor explicito, registre o valor em salario e inclua "bolsa-auxilio" em beneficios
- Preserve em requisitos o sentido da exigencia. Exemplo: "a partir do 4o periodo de engenharia" e requisito, nao beneficio

REGRAS ESPECIFICAS PARA SALARIO:
- Se o anuncio disser "ate R$ X", isso indica teto salarial: use salario = {"min": null, "max": X}
- Se o anuncio disser "a partir de R$ X", isso indica piso salarial: use salario = {"min": X, "max": null}
- Se o anuncio disser "entre R$ X e R$ Y" ou "de R$ X a R$ Y", use ambos os limites
- Nao troque min por max nem max por min; respeite exatamente o sentido textual da faixa

PROCESSO INTERNO (nao exibir):
1. Identificar cargo e empresa
2. Identificar localizacao e modalidade
3. Detectar nivel da vaga
4. Extrair salario se existir
5. Listar requisitos explicitos
6. Listar beneficios explicitos
7. Validar consistencia final

Exemplo:
Anuncio: "Desenvolvedor Python Pleno na DataCorp, Sao Paulo - hibrido. Salario R$ 8000 a R$ 12000. Requisitos: Python, SQL, Docker. Beneficios: VR, plano de saude."

JSON:
{"cargo": "Desenvolvedor Python", "empresa": "DataCorp", "localidade": "Sao Paulo", "modalidade": "hibrido", "nivel": "pleno", "salario": {"min": 8000, "max": 12000}, "requisitos": ["Python", "SQL", "Docker"], "beneficios": ["VR", "plano de saude"]}

Exemplo:
Anuncio: "TI Lopes contrata Estagiario de Engenharia de Dados. Presencial - Recife/PE. Bolsa-auxilio R$ 2.200. Estamos abertos a estudantes a partir do 4o periodo de Engenharia, Ciencia da Computacao ou Sistemas de Informacao."

JSON:
{"cargo": "Estagiario de Engenharia de Dados", "empresa": "TI Lopes", "localidade": "Recife/PE", "modalidade": "presencial", "nivel": "estagio", "salario": {"min": 2200, "max": null}, "requisitos": ["a partir do 4o periodo de engenharia, ciencia da computacao ou sistemas de informacao"], "beneficios": ["bolsa-auxilio"]}

Exemplo:
Anuncio: "Designer UX procurado pela startup BlueLab. Remoto. Sem informacao de salario. Necessario portfolio em Figma e experiencia com pesquisa de usuario."

JSON:
{"cargo": "Designer UX", "empresa": "BlueLab", "localidade": null, "modalidade": "remoto", "nivel": null, "salario": null, "requisitos": ["portfolio em figma", "experiencia com pesquisa de usuario"], "beneficios": []}

Exemplo:
Anuncio: "TechHub abre vaga de Engenheiro de Software Senior. Presencial em Sao Paulo - capital. Faixa salarial: ate R$ 18.000. Necessario experiencia com sistemas distribuidos, Kubernetes, AWS, e linguagens como Go ou Java. Plano de saude familiar."

JSON:
{"cargo": "Engenheiro de Software Senior", "empresa": "TechHub", "localidade": "Sao Paulo - capital", "modalidade": "presencial", "nivel": "senior", "salario": {"min": null, "max": 18000}, "requisitos": ["experiencia com sistemas distribuidos", "kubernetes", "aws", "go ou java"], "beneficios": ["plano de saude familiar"]}

Exemplo:
Anuncio: "Oportunidade Junior na DataSolutions. Cidade: Belo Horizonte/MG. Modalidade hibrida. Buscamos Analista de Dados em inicio de carreira. Salario a combinar. Conhecimentos desejados: SQL, Excel avancado, Python basico, Power BI. Oferecemos: vale-refeicao e plano odontologico."

JSON:
{"cargo": "Analista de Dados", "empresa": "DataSolutions", "localidade": "Belo Horizonte/MG", "modalidade": "hibrido", "nivel": "junior", "salario": null, "requisitos": ["sql", "excel avancado", "python basico", "power bi"], "beneficios": ["vale-refeicao", "plano odontologico"]}

Anuncio:
"__TEXTO_ANUNCIO__"

JSON:
"""


def montar_prompt(texto: str) -> str:
    """Monta o prompt final substituindo o texto do anuncio."""
    return PROMPT_BASE.replace("__TEXTO_ANUNCIO__", texto)
