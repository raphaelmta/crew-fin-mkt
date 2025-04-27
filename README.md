# 🧪 Gerador de Conteúdo Financeiro com IA

Este projeto é um **aplicativo desktop** para gerar conteúdo financeiro de alta qualidade utilizando **agentes de IA especializados**.
Ele combina **CrewAI**, **LangChain**, **OpenAI GPT-4** e uma interface gráfica criada com **Tkinter** para entregar textos otimizados e prontos para publicação.

---

## 🔹 Funcionalidades
- Recebe um **briefing** de conteúdo financeiro via interface gráfica.
- Analisa o briefing para definir estratégia e oportunidades de mercado.
- Gera textos de alta qualidade, claros, informativos e adaptados ao público-alvo.
- Otimiza o conteúdo para SEO e define estratégias de distribuição multicanal.
- Exibe o conteúdo gerado na interface para copiar, revisar ou publicar.

---

## 🔹 Tecnologias Utilizadas
- [Python 3.10+](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Interface Gráfica
- [CrewAI](https://docs.crewai.com/) - Gerenciamento de times de agentes
- [LangChain](https://www.langchain.com/) - Cadeias de LLMs
- [OpenAI GPT-4](https://platform.openai.com/docs/models/gpt-4)
- [DuckDuckGo Search Tool (LangChain Community Tools)](https://python.langchain.com/docs/integrations/tools/ddg_search)
- [.env](https://pypi.org/project/python-dotenv/) para gestão de chaves de API

---

## 🔹 Instalação

1. Clone o repositório:
```bash
 git clone https://github.com/seuusuario/gerador-conteudo-financeiro-ia.git
 cd gerador-conteudo-financeiro-ia
```

2. Instale as dependências:
```bash
 pip install -r requirements.txt
```

3. Crie um arquivo `.env` com sua chave da OpenAI:
```bash
 OPENAI_API_KEY= "sua-chave-openai"
```

4. Execute o aplicativo:
```bash
 python time_ag_finan.py
```

---

## 🔹 Estrutura dos Agentes
| Agente | Função |
|:------|:---------------------------------------------------------|
| Estrategista de Conteúdo | Análise de briefing, definição de público e planejamento |
| Criador de Conteúdo Financeiro | Produção de artigos e materiais de alta qualidade |
| Especialista em SEO | Otimização para buscadores e estratégia de distribuição |


---

## 🔹 Exemplo de Uso
1. Abra o aplicativo.
2. Insira um briefing de conteúdo (por exemplo, "Artigo sobre Tendências de Investimento em 2025").
3. Clique em **"Gerar Conteúdo"**.
4. Veja o conteúdo gerado na área de resposta.

---

## 💬 Contribuições
Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de modificar.

---

## 💡 Ideias Futuras
- Integração com APIs de publicação direta (WordPress, Medium).
- Módulo para análise de performance de conteúdo.
- Personalização de estilo de escrita por usuário.


