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


resource "digitalocean_app" "helloworld-go" {
  spec {
    name   = "helloworld-go"
    region = "ams"

    service {
      name               = "helloworld-go"
      instance_size_slug = "basic-xxs"
      instance_count     = 1
      dockerfile_path = "dockerfile"

      github {
        repo = "AnnoX4uk/helloworld-go"
        branch         = "main"
        deploy_on_push = true
      }
    }
  }
}

output app_link {
  value       = digitalocean_app.helloworld-go.live_url
  description = "Live app link"
}
