# prompts.py

def generate_prompt(texto_latim: str) -> str:
    return f"""
Você é um filólogo latino com experiência em análise gramatical e estilística.  
Analise o seguinte trecho em latim:

"{texto_latim}"

## Instruções:
1. Forneça uma tradução literal.
2. Explique as estruturas gramaticais e sintáticas relevantes.
3. Destaque recursos estilísticos ou figuras de linguagem.
4. Baseado nesses elementos, indique o estilo literário e um autor provável (se aplicável).

## Formato da resposta:
- Tradução Literal:  
- Análise Gramatical e Sintática:  
- Observações Estilísticas:  
- Possível Autor ou Estilo:  
"""

