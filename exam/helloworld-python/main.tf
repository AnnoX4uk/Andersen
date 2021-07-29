terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

# Set the variable value in *.tfvars file
# or using -var="do_token=..." CLI option
variable "do_token" {}


provider "digitalocean" {
  token = var.do_token
}


resource "digitalocean_app" "helloworld-python" {
  spec {
    name   = "helloworld-python"
    region = "ams"

    service {
      name               = "helloworld-python"
      instance_size_slug = "basic-xxs"
      instance_count     = 1
      dockerfile_path = "dockerfile"

      github {
        repo = "AnnoX4uk/helloworld-python"
        branch         = "main"
        deploy_on_push = true
      }
    }
  }
}

output app_link {
  value       = digitalocean_app.helloworld-python.live_url
  description = "Live app link"
}
