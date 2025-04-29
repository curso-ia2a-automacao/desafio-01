import json
import os

def salvar_respostas(**kwargs):
    respostas = {}
    for model in ["openai", "anthropic", "cohere", "mistral"]:
        resposta = kwargs['ti'].xcom_pull(key=f"resposta_{model}", task_ids=f"consultar_{model}")
        respostas[model] = resposta

    file_path = f"/opt/airflow/output/respostas_latim_{datetime.now().strftime('%Y%m%d%H%M')}.json"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(respostas, f, ensure_ascii=False, indent=4)

    print(f"Respostas salvas em {file_path}")

salvar_json = PythonOperator(
    task_id="salvar_respostas",
    python_callable=salvar_respostas,
    provide_context=True
)

salvar_json.set_upstream([f"consultar_{model}" for model in ["openai", "anthropic", "cohere", "mistral"]])

