terraform {
  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = "~> 1.0"
    }
  }
}

provider "databricks" {}

resource "databricks_job" "pratica_vendas_terraform" {
  name        = "job_pratica_vendas_terraform"
  description = "Job criado via Terraform, rodando o notebook pratica_vendas"

  task {
    task_key = "run_notebook"

    notebook_task {
      notebook_path = "/Workspace/Users/87arruda@gmail.com/pratica_vendas"
    }
  }
}
