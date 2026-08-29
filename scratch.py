import base64
import codecs

FLAG = "argon{test}"   # your flag here

def make_artifact(flag):
    """Take the flag, return the string a player will see.
    Apply rot13, then base64."""
    y = codecs.encode(flag, "rot-13")
    flag_encoded = base64.b64encode(y.encode()).decode()
    return(flag_encoded)

def solve(artifact):
    """Take ONLY the artifact string, return the flag.
    Never look at FLAG in here."""
    x = base64.b64decode(artifact.encode()).decode()
    flag_decoded = codecs.decode(x, "rot-13")
    return(flag_decoded)

artifact = make_artifact(FLAG)
print("artifact:", artifact)

recovered = solve(artifact)
print("recovered:", recovered)
print("match:", recovered == FLAG)