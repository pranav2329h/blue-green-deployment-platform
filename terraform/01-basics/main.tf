terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

provider "local" {}

resource "local_file" "project_note" {
  filename = "${path.module}/terraform-practice.txt"
  content  = "Terraform created this file."
}
