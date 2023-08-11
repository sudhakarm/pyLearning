contents = ["All carrots are to be sliced.",
            "The carrots were reportedly scliced",
            "The carrot is presened"]
filenames = ["doc.txt","report.txt","presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open (f"./Files/{filename}",'w')
    file.write(content)

