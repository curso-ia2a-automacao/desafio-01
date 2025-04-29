from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from prompts import generate_prompt
import json

# Suponha que você tenha funções realistas de chamada de API aqui
from llm_clients import call_openai, call_anthropic, call_cohere, call_mistral

default_args = {
    'start_date': datetime(2025, 4, 28),
    'retries': 1,
}

with DAG("comparacao_texto_latim", schedule_interval=None, default_args=default_args, catchup=False) as dag:

    def preparar_prompt(**kwargs):
        texto = "Quo usque tandem abutere, Catilina, patientia nostra?"
        prompt = generate_prompt(texto)
        kwargs['ti'].xcom_push(key='prompt', value=prompt)

    gerar_prompt = PythonOperator(
        task_id="gerar_prompt",
        python_callable=preparar_prompt,
        provide_context=True
    )

    def enviar_prompt_llm(provider: str, **kwargs):
        prompt = kwargs['ti'].xcom_pull(key='prompt', task_ids='gerar_prompt')
        if provider == "openai":
            response = call_openai(prompt)
        elif provider == "anthropic":
            response = call_anthropic(prompt)
        elif provider == "cohere":
            response = call_cohere(prompt)
        elif provider == "mistral":
            response = call_mistral(prompt)
        else:
            response = "Provider não suportado."

        print(f"Resposta de {provider}:\n{response}")
        kwargs['ti'].xcom_push(key=f"resposta_{provider}", value=response)

    for model in ["openai", "anthropic", "cohere", "mistral"]:
        PythonOperator(
            task_id=f"consultar_{model}",
            python_callable=enviar_prompt_llm,
            op_kwargs={"provider": model},
            provide_context=True
        ).set_upstream(gerar_prompt)
