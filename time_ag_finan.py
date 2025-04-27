import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Carrega o arquivo de variáveis de ambiente
load_dotenv(override=True)

# Verifica se a variável de ambiente da API foi carregada
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Nenhuma chave de API encontrada nas variáveis de ambiente")


# Inicializa as ferramentas básicas
search_tool = DuckDuckGoSearchRun()


# Inicializa os LLMs (agentes) específicos de função

# Define o LLM do Agente Estrategista de Conteúdo
estrategista_llm = ChatOpenAI(api_key=api_key,
                             model="gpt-4",
                             temperature=0.7)  # Mais criatividade

# Define o LLM do Agente Criador de Conteúdo Financeiro
criador_conteudo_llm = ChatOpenAI(api_key=api_key,
                                  model="gpt-4",
                                  temperature=0.2)  # Precisão e objetividade

# Define o LLM do Agente Especialista em SEO e Distribuição
especialista_seo_llm = ChatOpenAI(api_key=api_key,
                                   model="gpt-4",
                                   temperature=0.5)  # Equilíbrio entre criatividade e técnica

# Cria o Agente Estrategista de Conteúdo
estrategista = Agent(
    role='Estrategista de Conteúdo Sênior para o Mercado Financeiro',
    goal='Desenvolver estratégias de conteúdo eficazes e direcionadas para o público financeiro',
    backstory="""Você é um estrategista de conteúdo sênior com 15 anos de experiência em marketing digital no setor financeiro.
    Você possui mestrado em finanças e é especialista em comportamento do consumidor financeiro.
    Suas especialidades incluem:
    1.  Identificar tendências de mercado e oportunidades de conteúdo no setor financeiro
    2.  Definir personas de público-alvo e entender suas necessidades de informação
    3.  Planejar calendários editoriais e estratégias de distribuição de conteúdo
    4.  Analisar o desempenho do conteúdo e otimizar as estratégias com base em dados""",
    verbose=True,
    tools=[search_tool],
    allow_delegation=True,
    llm=estrategista_llm
)

# Cria o Agente Criador de Conteúdo Financeiro
criador_conteudo = Agent(
    role='Criador de Conteúdo Financeiro Especializado',
    goal='Produzir conteúdo de alta qualidade, informativo e engajador sobre temas financeiros',
    backstory="""Você é um criador de conteúdo financeiro experiente com foco em clareza, precisão e credibilidade.
    Você possui certificações financeiras (CFA, CFP, etc.) e tem experiência em redação técnica e jornalismo financeiro.
    Suas especialidades incluem:
    1.  Pesquisar e verificar informações financeiras complexas
    2.  Escrever artigos, blogs, e-books e outros formatos de conteúdo financeiro
    3.  Adaptar o tom e o estilo do conteúdo para diferentes públicos e canais
    4.  Garantir a conformidade do conteúdo com regulamentações do setor financeiro""",
    verbose=True,
    allow_delegation=True,
    llm=criador_conteudo_llm
)

# Cria o Agente Especialista em SEO e Distribuição
especialista_seo = Agent(
    role='Especialista em SEO e Distribuição de Conteúdo Financeiro',
    goal='Otimizar o conteúdo para mecanismos de busca e garantir sua ampla distribuição',
    backstory="""Você é um especialista em SEO e marketing de conteúdo com foco em aumentar a visibilidade e o alcance do conteúdo financeiro.
    Você possui experiência em otimização on-page e off-page, análise de palavras-chave e estratégias de distribuição multicanal.
    Suas especialidades incluem:
    1.  Realizar pesquisa de palavras-chave e otimizar o conteúdo para SEO
    2.  Gerenciar campanhas de marketing de conteúdo em diferentes canais (redes sociais, e-mail, etc.)
    3.  Analisar métricas de desempenho de SEO e tráfego do site
    4.  Implementar estratégias de link building e outreach para aumentar a autoridade do conteúdo""",
    verbose=True,
    allow_delegation=True,
    llm=especialista_seo_llm
)


# Função para executar o time de agentes de marketing financeiro
def execute_time_marketing_financeiro(briefing_conteudo):
    try:
        tasks = [
            Task(
                description=f"""
                Analise o briefing de conteúdo: {briefing_conteudo}.
                Identifique o público-alvo, os objetivos de marketing e as principais mensagens.
                Realize uma pesquisa de mercado para encontrar tendências relevantes e lacunas de conteúdo.
                """,
                agent=estrategista
            ),
            Task(
                description=f"""
                Com base na estratégia definida, crie conteúdo financeiro de alta qualidade.
                Certifique-se de que o conteúdo seja preciso, informativo, envolvente e adequado ao público-alvo.
                O formato do conteúdo pode variar (artigo, blog, vídeo, infográfico, etc.).
                """,
                agent=criador_conteudo
            ),
            Task(
                description=f"""
                Otimize o conteúdo para mecanismos de busca (SEO) usando palavras-chave relevantes.
                Desenvolva uma estratégia de distribuição para maximizar o alcance e o engajamento.
                Monitore o desempenho do conteúdo e forneça recomendações para melhorias.
                """,
                agent=especialista_seo
            )
        ]

        time_marketing_financeiro = Crew(agents=[estrategista, criador_conteudo, especialista_seo],
                                          tasks=tasks,
                                          verbose=2)

        result = time_marketing_financeiro.kickoff()

        return result
    except Exception as e:
        return f"Ocorreu o erro: {str(e)}"


# Função para lidar com o clique do botão "Gerar Conteúdo"
def gerar_conteudo():
    briefing = entrada_briefing.get("1.0", tk.END)  # Pega o texto da área de entrada
    if not briefing.strip():  # Verifica se o briefing está vazio
        messagebox.showerror("Erro", "Por favor, insira um briefing de conteúdo.")
        return

    try:
        resultado = execute_time_marketing_financeiro(briefing)
        saida_conteudo.delete("1.0", tk.END)  # Limpa a área de saída
        saida_conteudo.insert("1.0", resultado)  # Insere o resultado na área de saída
    except Exception as e:
        saida_conteudo.delete("1.0", tk.END)
        saida_conteudo.insert("1.0", f"Ocorreu um erro durante a geração: {str(e)}")
        messagebox.showerror("Erro", "Erro ao gerar conteúdo. Verifique sua conexão e chave da API.")


# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Gerador de Conteúdo Financeiro com IA")
janela.geometry("800x600")  # Tamanho da janela

# Rótulo e Área de Entrada para o Briefing
tk.Label(janela, text="Insira o Briefing de Conteúdo:", font=("Arial", 12)).pack(pady=10)
entrada_briefing = scrolledtext.ScrolledText(janela, height=10, font=("Arial", 10))
entrada_briefing.pack(padx=20, fill=tk.X)

# Botão para Gerar Conteúdo
botao_gerar = tk.Button(janela, text="Gerar Conteúdo", command=gerar_conteudo, font=("Arial", 12, "bold"))
botao_gerar.pack(pady=20)

# Rótulo e Área de Saída para o Conteúdo Gerado
tk.Label(janela, text="Conteúdo Gerado:", font=("Arial", 12)).pack(pady=10)
saida_conteudo = scrolledtext.ScrolledText(janela, height=15, font=("Arial", 10))
saida_conteudo.pack(padx=20, fill=tk.BOTH, expand=True)

# Bloco de execução (dentro do arquivo único)
if __name__ == "__main__":
    # Carrega o arquivo de variáveis de ambiente (se estiver executando como script)
    if os.path.exists(".env"):
        load_dotenv(override=True)

    # Verifica se a variável de ambiente da API foi carregada
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        messagebox.showerror("Erro", "Nenhuma chave de API encontrada. Verifique o arquivo .env ou as variáveis de ambiente.")
    else:
        janela.mainloop()  # Inicia a GUI