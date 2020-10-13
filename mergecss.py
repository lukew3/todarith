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
