import click
from todarith import create_app, db
from todarith.models import Skill, User, Problem
import random, time, os
from mathgenerator import mathgen
import sys

app = create_app()
app.app_context().push()

@click.group()
def cli():
    pass

@cli.command()
def empty_db():
    answer = input("This will completely remove and recreate the database. To confirm, type, \"confirm\": " )
    if answer != "confirm":
        print("Operation aborted")
        return 0
    """
    script_lines = ['sudo su',
                    'su - postgres',
                    'dropdb todarith',
                    'createdb todarith']
    script = '\n'.join(script_lines)
    os.system(script)
    """
    db.create_all(app=create_app())
    User.create(
        username="Anonymous",
        pw_hash="a;sfap3rbijsapvnioc3npas3r",
        email="anonymous@maildrop.cc"
    )
    Skill.create(
        skillName="Math"
    )
    Skill.create(
        skillName="generated"
    )


@cli.command()
def merge_css():
    base = "todarith/static/css/"
    endFile = "todarith/static/main.css"

    files = [
        "layout.css",
        "landing.css",
        "auth/loginregister.css",
        "db/add.css",
        "db/answer.css",
        "db/ask.css",
        "db/browse.css",
        "db/sort.css",
        "db/viewProb.css",
        "learn/practice.css"
    ]

    export = open(endFile, "r+")
    export.truncate(0)

    for file in files:
        filename = base+file
        f = open(filename, "r")
        export.write(f.read())
        f.close()

    export.close()


@cli.command()
def auto_generate():
    pigs_fly = False
    while pigs_fly == False:
        gen_id = random.randint(0, len(mathgen.getGenList())-1)
        try:
            p, a, s = generate_problem(gen_id)
            print(p)
        except Exception as e:
            with open("gen_errors.txt", "a") as myfile:
                myfile.write("GEN ID: " + str(gen_id) + ". ERROR: " + str(e)) 
        time.sleep(0.05)

def generate_problem(gen_id):
    poster = User.query.filter_by().first()
    gen_list = mathgen.getGenList()
    prob, ans = mathgen.genById(gen_id)
    generator_name = gen_list[gen_id][1]
    # If statement makes sure there isnt a duplicate
    if Problem.query.filter_by(question=prob).first() == None: 
        Problem.create(
            question=prob,
            answer=ans,
            poster_id=poster.id,
            correctnessRating=1,
            sortRating=1,
            difficultyLevel=None,
            expectedTime=None,
            hasSolution=True,
        )
        thisProb = Problem.query.filter_by(question=prob).first()
        # Add the math skill
        thisProb.skills.append(Skill.query.filter_by(id=1).first())
        # If generator_name skill doesn't yet exist, create it and then add it
        if Skill.query.filter_by(skillName=generator_name).first() == None:
            Skill.create(
                skillName = generator_name
            )
        thisProb.skills.append(Skill.query.filter_by(skillName=generator_name).first())
        # Add generated tag in order to prevent disaster if a bad generator is made
        thisProb.skills.append(Skill.query.filter_by(skillName="generated").first())
        db.session.commit()
        return prob, ans, generator_name
    else:
        return "Problem already exists", "N/A", "N/A"

if __name__ == "__main__":
    cli()
