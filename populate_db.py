import os
import django

# Set Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_backend.settings')
django.setup()

from portfolio_core.models import Achievement, Project, Skill

def populate_achievements():
    achievements = [
        {
            "title": "Internship at ISO-approved IT Company",
            "organization": "O7 Services",
            "year": "2023 - 2024",
            "category": "cert",
            "description": "Demonstrated expertise in designing distributed systems on Cloud, Streamlit, Flask, Python, and cloud-native architecture patterns.",
            "icon": "cloud",
            "order": 1
        },
        {
            "title": "AI Traffic Control System",
            "organization": "Project Milestone",
            "year": "2025",
            "category": "project",
            "description": "Architected an automated labeling system using AWS Rekognition and AWS Lambda, replacing manual classification with 95% accurate AI-based object detection.",
            "icon": "zap",
            "order": 2
        },
        {
            "title": "Best Innovation – College Hackathon",
            "organization": "University Tech Fest",
            "year": "2024",
            "category": "award",
            "description": "Awarded Best Innovation for designing an AI-powered smart queue management prototype that reduced average wait time by 40% in a 24-hour hackathon sprint.",
            "icon": "award",
            "order": 3
        },
        {
            "title": "Railway Queue Management System",
            "organization": "Java / DSA",
            "year": "2025",
            "category": "project",
            "description": "Built a full data-persistent passenger queue system using FIFO structures and file handling in Java, optimizing seating allocation across carriage sessions.",
            "icon": "train",
            "order": 4
        },
        {
            "title": "Machine Learning Specialization",
            "organization": "deeplearning.ai / Coursera",
            "year": "2024",
            "category": "cert",
            "description": "Completed AI & ML Specialization from ISO approved institution.",
            "icon": "cpu",
            "order": 5
        },
        {
            "title": "Computer Science Degree",
            "organization": "ISO-Approved Institution",
            "year": "2023 – 2025",
            "category": "academic",
            "description": "Gained experience in model training by handling real-world projects with Deep Learning models at an ISO-approved institution.",
            "icon": "graduation-cap",
            "order": 6
        },
        {
            "title": "Full-Stack Web Development",
            "organization": "The Odin Project / freeCodeCamp",
            "year": "2023",
            "category": "cert",
            "description": "Completed comprehensive curriculum covering HTML, CSS, JavaScript, Node.js, Express, React, and REST API design.",
            "icon": "globe",
            "order": 7
        },
        {
            "title": "Research Paper – AI in Traffic Management",
            "organization": "IEEE Student Conference",
            "year": "2025",
            "category": "academic",
            "description": "Authored and presented a research paper on AWS-driven AI traffic detection systems, exploring latency optimization and real-world deployment.",
            "icon": "file-text",
            "order": 8
        }
    ]
    for a in achievements:
        obj, created = Achievement.objects.get_or_create(title=a['title'], defaults=a)
        if not created:
            for key, value in a.items():
                setattr(obj, key, value)
            obj.save()

def populate_projects():
    projects = [
        {
            "title": "AI Traffic Control System",
            "subtitle": "AWS (Rekognition, Lambda, S3, API Gateway), Serverless, React • Jul 2025",
            "date": "Jul 2025",
            "description": "Architected an automated labeling system using AWS Rekognition and AWS Lambda, replacing manual classification with 95% accurate AI-based object detection.\n- Automated the backend pipeline using AWS Lambda, S3, and API Gateway.\n- Deployed and optimized a responsive frontend with Streamlit.",
            "tags": "AWS,AI,React",
            "order": 1
        },
        {
            "title": "Railway Queue Management",
            "subtitle": "Java, DSA, File Handling • Mar 2025",
            "date": "Mar 2025",
            "description": "Developed using IntelliJ IDEA to manage passenger waiting lists efficiently using Queue (FIFO) data structures.\n- Implemented File Handling systems to save and retrieve passenger details.\n- Optimized seating allocation algorithms to minimize wait times.",
            "tags": "Java,DSA",
            "order": 2
        },
        {
            "title": "AI Prediction Engine",
            "subtitle": "Python, ML",
            "date": "2025",
            "description": "Advanced predictive modeling system for financial data analysis using deep learning and custom neural architectures.",
            "tags": "Python,ML",
            "order": 3
        }
    ]
    for p in projects:
        obj, created = Project.objects.get_or_create(title=p['title'], defaults=p)
        if not created:
            for key, value in p.items():
                setattr(obj, key, value)
            obj.save()

def populate_skills():
    skills = [
        {"name": "TypeScript", "icon": "typescript", "description": "Strongly typed superset of JS for highly scalable apps", "energy": 92, "order": 1},
        {"name": "JavaScript", "icon": "javascript", "description": "Core programming language powering the dynamic web", "energy": 95, "order": 2},
        {"name": "Dart", "icon": "dart", "description": "Client-optimized language for fast apps on any platform", "energy": 80, "order": 3},
        {"name": "Java", "icon": "java", "description": "Robust object-oriented programming for enterprise backends", "energy": 85, "order": 4},
        {"name": "React", "icon": "react", "description": "Leading JavaScript library for building interactive UIs", "energy": 90, "order": 5},
        {"name": "Flutter", "icon": "flutter", "description": "Google's UI toolkit for natively compiled multi-platform apps", "energy": 82, "order": 6},
        {"name": "Android", "icon": "android", "description": "Open-source operating system for mobile applications", "energy": 75, "order": 7},
        {"name": "HTML5", "icon": "html5", "description": "Modern markup language for structuring web content", "energy": 98, "order": 8},
        {"name": "CSS3", "icon": "css3", "description": "Advanced style sheet language for responsive presentation", "energy": 95, "order": 9},
        {"name": "Node.js", "icon": "nodedotjs", "description": "High-performance JavaScript runtime built on Chrome's V8", "energy": 88, "order": 10},
        {"name": "Express", "icon": "express", "description": "Fast, unopinionated web framework for Node.js", "energy": 85, "order": 11},
        {"name": "Next.js", "icon": "nextdotjs", "description": "The React Framework for production-grade server rendering", "energy": 88, "order": 12},
        {"name": "Prisma", "icon": "prisma", "description": "Next-generation ORM wrapper for Node.js and TypeScript", "energy": 80, "order": 13},
        {"name": "AWS", "icon": "amazonaws", "description": "The world's most comprehensive and broadly adopted cloud", "energy": 90, "order": 14},
        {"name": "PostgreSQL", "icon": "postgresql", "description": "Highly advanced open-source relational database system", "energy": 85, "order": 15},
        {"name": "Firebase", "icon": "firebase", "description": "Google's platform for fast backend app development", "energy": 82, "order": 16},
        {"name": "NGINX", "icon": "nginx", "description": "High-performance HTTP server, reverse proxy, and load balancer", "energy": 78, "order": 17},
        {"name": "Vercel", "icon": "vercel", "description": "Premium cloud platform for lightning fast frontend deployment", "energy": 85, "order": 18},
        {"name": "Docker", "icon": "docker", "description": "OS-level virtualization to deliver software in secure containers", "energy": 80, "order": 19},
        {"name": "Git", "icon": "git", "description": "Open source distributed version control system for tracking changes", "energy": 92, "order": 20},
        {"name": "GitHub", "icon": "github", "description": "The ultimate developer platform to build, scale, and deliver", "energy": 95, "order": 21},
        {"name": "Figma", "icon": "figma", "description": "Collaborative web application for high-end UI/UX interface design", "energy": 85, "order": 22},
        {"name": "Django", "icon": "django", "description": "Powerful Python framework for backend development", "energy": 88, "order": 23},
        {"name": "Python", "icon": "python", "description": "Universal language for AI, ML and backend engineering", "energy": 95, "order": 24},
    ]
    for s in skills:
        obj, created = Skill.objects.get_or_create(name=s['name'], defaults=s)
        if not created:
            for key, value in s.items():
                setattr(obj, key, value)
            obj.save()

if __name__ == "__main__":
    print("Populating database with full portfolio data...")
    populate_achievements()
    populate_projects()
    populate_skills()
    print("Full migration complete!")
