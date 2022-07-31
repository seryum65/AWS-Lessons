data "aws_vpc" "selected" {
    default = true
}

data "aws_subnets" "example" {
  filter {
    name = "vpc-id"
    values = [data.aws_vpc.selected.id]
  }
}

data "aws_ami" "amazon-linux-2" {
  owners = ["amazon"]
  most_recent = true
  filter {
    name = "name"
    values = ["amzn2-ami-kernel-5.10*"]
  }
}

resource "aws_launch_template" "asg-lt" {
    name = "Roman-Numerals-Converter"
    image_id = data.aws_ami.amazon-linux-2.id
    instance_type = "t2.micro"
    key_name = "firstkey"
    vpc_security_group_ids = [aws_security_group.server-sg.id]
    user_data = filebase64("cli.sh")
    tag_specifications {
        resource_type = "instance"
        tags = {
            Name = "Web Server of Roman Numerals Converter"
        }
  }
  
}

resource "aws_alb_target_group" "app-lb-tg" {
  name = "Roman-Numerals-Converter-lb-tg"
  port = 80
  protocol = "HTTP"
  vpc_id = data.aws_vpc.selected.id
  target_type = "instance"
  health_check {
    healthy_threshold = 2
    unhealthy_threshold = 3
  }

}
resource "aws_alb" "app-lb" {
    name = "Roman-Numerals-Converter-lb-tf"
    ip_address_type = "ipv4"
    internal = false
    load_balancer_type = "application"
    security_groups = [ aws_security_group.alb-sg.id ]
    subnets = data.aws_subnets.example.ids
      
}

resource "aws_alb_listener" "app-listener" {
    load_balancer_arn = aws_alb.app-lb.arn
    port = 80
    protocol = "HTTP"
    default_action {
        type = "forward"
        target_group_arn = aws_alb_target_group.app-lb-tg.arn 
  }    
  
}

resource "aws_autoscaling_group" "app-asg" {
  name = "Roman-Numerals-Converter-asg"
  max_size = 3
  min_size = 1
  desired_capacity = 2
  health_check_grace_period = 300
  health_check_type = "ELB"
  target_group_arns = [aws_alb_target_group.app-lb-tg.arn]
  vpc_zone_identifier = aws_alb.app-lb.subnets

  launch_template {
    id = aws_launch_template.asg-lt.id
    version = aws_launch_template.asg-lt.latest_version
  }
}