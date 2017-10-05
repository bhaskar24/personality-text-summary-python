import os
import json

# Returns text summary of a given json personality profile
def getSummary(*args):
  # Arguments check
  if (len(args) != 1 and len(args) != 3):
    print('Error: Too little or too many arguments. See usage for getSummary().')
    exit()

  # Dumps personality profile into json file
  with open('./dependencies/result.json', 'w') as fp:
    json.dump(args[0], fp)
  
  # Change language and version if specified
  # If none specified, default is English and v3
  if (len(args) > 1):
    f = open("./dependencies/ps.js", "r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
      if (not ("var v3EnglishTextSummaries = new PersonalityTextSummaries" in i)):
        f.write(i)
      else:
        line = "var v3EnglishTextSummaries = new PersonalityTextSummaries({ locale: '%s', version: '%s' });\n" % (args[1], args[2])
        f.write(line)
    f.truncate()
    f.close()
  
  # Outputs personality text summary to text file
  os.system("node ./dependencies/ps.js > output.txt")

  # Reads text summary into variable
  g = open('output.txt', 'r')
  summary = g.read()
  g.close()

  # Cleanup
  os.remove('./dependencies/result.json')
  os.remove('output.txt')
  os.remove('personalitysummary.pyc')

  # Reverts back to default v3 English if changed at all
  if (len(args) > 1):
    f = open("./dependencies/ps.js", "r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
      if (not ("var v3EnglishTextSummaries = new PersonalityTextSummaries" in i)):
        f.write(i)
      else:
        line = "var v3EnglishTextSummaries = new PersonalityTextSummaries({ locale: '%s', version: '%s' });\n" % ('en', 'v3')
        f.write(line)
    f.truncate()
    f.close()

  # Returns summary
  return summary
